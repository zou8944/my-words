import news_utils
import newsletter
import push

logger = news_utils.setup_logger(__name__)


def main():
    try:
        newsletter.try_generate_newsletter()
        push.push_deer("今日技术 newsletter 已生成")
    except Exception as e:
        logger.error(f"生成 newsletter 过程中发生错误: {e}")
        push.push_deer(f"生成 newsletter 失败: {e}")
        raise e


if __name__ == "__main__":
    main()
