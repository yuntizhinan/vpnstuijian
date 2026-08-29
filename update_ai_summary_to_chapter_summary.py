# -*- coding: utf-8 -*-
import os
import re

base_dir = r"d:\HuaweiMoveData\Users\psyto\Desktop\vpnstuijian.net"
articles_dir = os.path.join(base_dir, "articles")

print("=== 批量将 '本章速览' 修改为 '本章速览' ===")

# 1. 替换所有的 Python 脚本
py_files = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith(".py")]
for py_path in py_files:
    with open(py_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "本章速览" in content:
        new_content = content.replace("本章速览", "本章速览")
        with open(py_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[Updated Py Script] {os.path.basename(py_path)}")

# 2. 替换所有的 HTML 页面
all_html_files = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith(".html")]
if os.path.exists(articles_dir):
    all_html_files.extend([os.path.join(articles_dir, f) for f in os.listdir(articles_dir) if f.endswith(".html")])

replaced_count = 0
for html_path in all_html_files:
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
    if "本章速览" in content:
        new_content = content.replace("本章速览", "本章速览")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        replaced_count += 1
        print(f"[Updated HTML] {os.path.basename(html_path)}")

print(f"\n替换完成，共更新了 {replaced_count} 个 HTML 页面！")
