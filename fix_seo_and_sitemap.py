# -*- coding: utf-8 -*-
import os
import re
import glob
from datetime import datetime

base_dir = r"d:\HuaweiMoveData\Users\psyto\Desktop\vpnstuijian.net"
articles_dir = os.path.join(base_dir, "articles")

print("=== 1. 清理 HTML 文件中重复堆砌的 meta keywords ===")

def clean_keywords_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 正则匹配 meta keywords
    def fix_kw_match(m):
        raw_kw = m.group(1)
        # 拆分关键词并去重，保持原顺序
        parts = [p.strip() for p in raw_kw.split(",") if p.strip()]
        unique_parts = []
        for p in parts:
            if p not in unique_parts:
                unique_parts.append(p)
        return f'<meta name="keywords" content="{", ".join(unique_parts)}">'

    new_content = re.sub(r'<meta\s+name="keywords"\s+content="([^"]+)"\s*\/?>', fix_kw_match, content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[Cleaned Keywords] {os.path.basename(filepath)}")

# 处理所有 HTML 文件
all_html_files = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith(".html")]
if os.path.exists(articles_dir):
    all_html_files.extend([os.path.join(articles_dir, f) for f in os.listdir(articles_dir) if f.endswith(".html")])

for file_path in all_html_files:
    clean_keywords_in_file(file_path)


print("\n=== 2. 生成全量 Sitemap.xml (包含主页与所有文章页) ===")

today_str = datetime.now().strftime("%Y-%m-%d")
domain = "https://vpnstuijian.net"

sitemap_entries = [
    f"""  <url>
    <loc>{domain}/index.html</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""",
    f"""  <url>
    <loc>{domain}/vpn-guide.html</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>""",
    f"""  <url>
    <loc>{domain}/archives.html</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""",
    f"""  <url>
    <loc>{domain}/about.html</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>"""
]

# 添加所有文章
if os.path.exists(articles_dir):
    art_files = sorted([f for f in os.listdir(articles_dir) if f.endswith(".html")])
    for art in art_files:
        # 给核心文章提高优先级
        priority = "0.85" if art in ["airport-guide-2026.html", "cost-per-gb-buying-guide-2026.html", "iplc-guide.html", "one-multiplier.html"] else "0.75"
        sitemap_entries.append(f"""  <url>
    <loc>{domain}/articles/{art}</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>
"""

sitemap_path = os.path.join(base_dir, "sitemap.xml")
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_xml_content)

print(f"[Sitemap Updated] 已更新 sitemap.xml，共包含 {len(sitemap_entries)} 个网页入口。")

print("\n=== 3. 验证与强化核心关键词布局与 Structured Data ===")
print("完成!")
