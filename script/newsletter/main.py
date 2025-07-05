"""
新闻聚合主程序
运行所有新闻源的抓取和总结
"""

import asyncio
import signal
import sys

from apscheduler.events import EVENT_JOB_ERROR, EVENT_JOB_EXECUTED
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

import news_utils
import newsletter

logger = news_utils.setup_logger(__name__)

# 全局调度器变量，用于信号处理器访问
scheduler = None


def signal_handler(signum, frame):
    logger.info(f"接收到信号 {signum}，正在安全退出...")
    if scheduler:
        scheduler.shutdown(wait=False)
    sys.exit(0)


async def job_listener(event):
    """任务执行监听器"""
    if event.exception:
        logger.error(f"任务执行失败: {event.exception}")
    else:
        logger.info(f"任务执行成功: {event.job_id}")


async def main():
    """主函数，设置定时任务"""
    global scheduler

    # 注册信号处理器
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # 创建调度器，指定时区
    scheduler = AsyncIOScheduler(timezone='Asia/Shanghai')
    
    # 添加任务监听器
    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    # 添加定时任务：从上午9点到中午12点，每小时执行一次
    scheduler.add_job(
        func=newsletter.try_generate_newsletter,
        trigger=CronTrigger(
            hour="9-12",  # 9点到12点
            minute="0",  # 每小时的0分执行
            timezone='Asia/Shanghai'  # 明确指定时区
        ),
        id="newsletter_job",
        name="生成每日技术newsletter",
        max_instances=1,  # 最多同时运行1个实例
        coalesce=True,  # 如果有多个任务在等待，合并为一个
        misfire_grace_time=30,  # 30秒的宽限时间
    )

    # 启动调度器
    scheduler.start()

    logger.info("定时任务已启动")
    logger.info("将在每天上午9点、10点、11点、12点执行newsletter生成任务")
    logger.info("按 Ctrl+C 退出程序")

    # 打印任务的下次执行时间
    next_run_time = scheduler.get_job("newsletter_job").next_run_time  # type: ignore
    if next_run_time:
        logger.info(f"下次执行时间: {next_run_time.strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # 保持程序运行
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        logger.info("程序正在退出...")
        scheduler.shutdown(wait=True)


if __name__ == "__main__":
    asyncio.run(main())
