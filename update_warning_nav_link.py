import os

base_dir = r"c:\Users\psyto\Desktop\vpnstuijian.net"

root_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
articles_dir = os.path.join(base_dir, "articles")
article_files = [f for f in os.listdir(articles_dir) if f.endswith(".html")]

updated_count = 0

# Update root files
for fname in root_files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_target = '<a href="articles/shandian-warning.html" class="dropdown-item">⚠️ 避雷指南</a>'
    new_target = '<a href="articles/subscription-guide.html" class="dropdown-item">⚠️ 避雷指南</a>'
    
    if old_target in content:
        content = content.replace(old_target, new_target)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1
        print(f"Updated nav in root file: {fname}")

# Update article files
for fname in article_files:
    fpath = os.path.join(articles_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    old_target = '<a href="shandian-warning.html" class="dropdown-item">⚠️ 避雷指南</a>'
    new_target = '<a href="subscription-guide.html" class="dropdown-item">⚠️ 避雷指南</a>'
    
    if old_target in content:
        content = content.replace(old_target, new_target)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1
        print(f"Updated nav in article file: {fname}")

# Also update python generator scripts
scripts = ["build_vpnstuijian_articles.py", "rewrite_vpnstuijian_unique.py"]
for sname in scripts:
    spath = os.path.join(base_dir, sname)
    if os.path.exists(spath):
        with open(spath, "r", encoding="utf-8") as f:
            content = f.read()
        old_target = '<a href="shandian-warning.html" class="dropdown-item">⚠️ 避雷指南</a>'
        new_target = '<a href="subscription-guide.html" class="dropdown-item">⚠️ 避雷指南</a>'
        if old_target in content:
            content = content.replace(old_target, new_target)
            with open(spath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated generator script: {sname}")

print(f"Total HTML/script files updated: {updated_count}")
