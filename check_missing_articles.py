# -*- coding: utf-8 -*-
import os
import re

base_dir = r"d:\HuaweiMoveData\Users\psyto\Desktop\vpnstuijian.net"
articles_dir = os.path.join(base_dir, "articles")

art_files = set(f for f in os.listdir(articles_dir) if f.endswith(".html"))
print(f"Total HTML files in articles/ directory: {len(art_files)}")

with open(os.path.join(base_dir, "generate_site.py"), "r", encoding="utf-8") as f:
    gen_code = f.read()

# 匹配所有 slug
slugs = set(re.findall(r"'slug':\s*'([^']+)'", gen_code))
print(f"Total slugs in generate_site.py: {len(slugs)}")

missing_in_script = []
for f in sorted(art_files):
    slug = f[:-5] # remove .html
    if slug not in slugs:
        missing_in_script.append(f)

print(f"\nFound {len(missing_in_script)} articles present in articles/ but NOT in generate_site.py:")
for m in missing_in_script:
    # 获取文件的修改时间和标题
    fpath = os.path.join(articles_dir, m)
    mtime = os.path.getmtime(fpath)
    from datetime import datetime
    time_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    
    # 提取 <title>
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
        t_match = re.search(r'<title>(.*?)</title>', content)
        title = t_match.group(1) if t_match else "No title"
        
    print(f"- {m} (修改时间: {time_str}) -> 标题: {title[:50]}")
