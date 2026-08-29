# -*- coding: utf-8 -*-
import os

base_dir = r"d:\HuaweiMoveData\Users\psyto\Desktop\vpnstuijian.net"
articles_dir = os.path.join(base_dir, "articles")

art_files = [f for f in os.listdir(articles_dir) if f.endswith(".html")]

bad_files = []
for f in art_files:
    fpath = os.path.join(articles_dir, f)
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
        c = content.count('<footer class="footer">')
        faq_c = content.count('❓ 常见问题 FAQ')
        if c != 1 or faq_c > 1:
            bad_files.append((f, c, faq_c))

print(f"Total articles checked: {len(art_files)}")
print(f"Problematic articles with duplicate footer/FAQ: {len(bad_files)}")
for bf in bad_files:
    print(f"- {bf[0]}: footer count={bf[1]}, FAQ count={bf[2]}")
