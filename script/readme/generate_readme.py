#!/usr/bin/env python3
"""
生成 README.md 文件的脚本
读取 posts 目录下的所有 Markdown 文件，提取 front matter，
根据创建时间倒序排列，生成 README.md 文件
"""

import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import yaml
except ImportError:
    print("❌ 缺少 PyYAML 依赖，请运行: pip install PyYAML")
    sys.exit(1)


def extract_front_matter(content: str) -> Tuple[Optional[Dict], str]:
    """
    提取 Markdown 文件中的 front matter
    
    Args:
        content: 文件内容
        
    Returns:
        tuple: (front_matter_dict, content_without_front_matter)
    """
    # 匹配 YAML front matter 格式 (--- 开头和结尾)
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        return None, content
    
    try:
        front_matter = yaml.safe_load(match.group(1))
        content_without_front_matter = content[match.end():]
        return front_matter, content_without_front_matter
    except yaml.YAMLError:
        return None, content


def get_creation_date(front_matter: Optional[Dict]) -> Optional[datetime]:
    """
    从 front matter 中获取创建时间
    
    Args:
        front_matter: front matter 字典
        
    Returns:
        datetime 对象或 None
    """
    if not front_matter:
        return None
    
    # 尝试不同的时间字段名
    date_fields = ['created_at', 'date', 'created', 'publish_date']
    
    for field in date_fields:
        if field in front_matter:
            date_value = front_matter[field]
            if isinstance(date_value, datetime):
                return date_value
            elif isinstance(date_value, str):
                try:
                    # 尝试解析不同的日期格式
                    for fmt in [
                        '%Y-%m-%d %H:%M:%S',
                        '%Y-%m-%d %H:%M',
                        '%Y-%m-%d',
                        '%Y/%m/%d',
                        '%Y-%m-%dT%H:%M:%S',
                        '%Y-%m-%dT%H:%M:%SZ'
                    ]:
                        try:
                            return datetime.strptime(date_value, fmt)
                        except ValueError:
                            continue
                except Exception:
                    continue
    
    return None


def get_title(front_matter: Optional[Dict], file_path: Path) -> str:
    """
    从 front matter 中获取标题，如果没有则使用文件名
    
    Args:
        front_matter: front matter 字典
        file_path: 文件路径
        
    Returns:
        文章标题
    """
    if front_matter and 'title' in front_matter:
        return front_matter['title']
    
    # 使用文件名作为标题（去掉扩展名）
    return file_path.stem


def scan_posts_directory(posts_dir: Path) -> List[Dict]:
    """
    扫描 posts 目录，收集所有文章信息
    
    Args:
        posts_dir: posts 目录路径
        
    Returns:
        文章信息列表
    """
    articles = []
    
    # 递归遍历 posts 目录
    for md_file in posts_dir.rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            front_matter, _ = extract_front_matter(content)
            creation_date = get_creation_date(front_matter)
            title = get_title(front_matter, md_file)
            
            # 生成相对链接
            relative_path = md_file.relative_to(posts_dir.parent)
            
            articles.append({
                'title': title,
                'path': str(relative_path),
                'creation_date': creation_date,
                'year': creation_date.year if creation_date else None,
                'front_matter': front_matter
            })
            
        except Exception as e:
            print(f"处理文件 {md_file} 时出错: {e}")
            continue
    
    return articles


def generate_readme(articles: List[Dict]) -> str:
    """
    生成 README.md 内容
    
    Args:
        articles: 文章信息列表
        
    Returns:
        README.md 内容
    """
    # 过滤掉没有日期的文章
    valid_articles = [article for article in articles if article['creation_date']]
    
    # 按创建时间倒序排列
    valid_articles.sort(key=lambda x: x['creation_date'], reverse=True)
    
    # 按年份分组
    articles_by_year = {}
    for article in valid_articles:
        year = article['year']
        if year not in articles_by_year:
            articles_by_year[year] = []
        articles_by_year[year].append(article)
    
    # 生成 README 内容
    readme_content = [
        "# 我叫果冻\n",
        "[果冻的碎碎念 - zou8944.com](https://zou8944.com)\n",
    ]

    # 按年份倒序排列
    for year in sorted(articles_by_year.keys(), reverse=True):
        readme_content.append(f"## {year}\n")
        
        # 该年份的文章按时间倒序排列
        year_articles = articles_by_year[year]
        for article in year_articles:
            title = article['title']
            path = article['path']
            readme_content.append(f"- [{title}]({path})")
        
        readme_content.append("")  # 年份之间空一行
    
    return "\n".join(readme_content)


def main():
    """主函数"""
    # 获取当前脚本所在目录，向上两级到达项目根目录
    script_dir = Path(__file__).parent.parent.parent
    posts_dir = script_dir / 'posts'
    readme_path = script_dir / 'README.md'
    
    # 检查 posts 目录是否存在
    if not posts_dir.exists():
        print(f"❌ 错误: posts 目录不存在: {posts_dir}")
        return
    
    print(f"📚 正在扫描 posts 目录: {posts_dir}")
    
    # 扫描文章
    articles = scan_posts_directory(posts_dir)
    valid_articles = [a for a in articles if a['creation_date']]
    
    print("📊 扫描结果:")
    print(f"   总文章数: {len(articles)}")
    print(f"   有效文章数: {len(valid_articles)}")
    print(f"   无日期文章数: {len(articles) - len(valid_articles)}")
    
    # 按年份统计
    year_counts = {}
    for article in valid_articles:
        year = article['year']
        year_counts[year] = year_counts.get(year, 0) + 1
    
    print("📅 按年份统计:")
    for year in sorted(year_counts.keys(), reverse=True):
        print(f"   {year}: {year_counts[year]} 篇")
    
    # 生成 README
    readme_content = generate_readme(articles)
    
    # 写入 README.md
    try:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"✅ README.md 已生成: {readme_path}")
    except Exception as e:
        print(f"❌ 生成 README.md 时出错: {e}")


if __name__ == "__main__":
    main()
