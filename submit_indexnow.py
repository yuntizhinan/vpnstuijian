# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import urllib.request
import json

base_dir = r"d:\HuaweiMoveData\Users\psyto\Desktop\vpnstuijian.net"
sitemap_path = os.path.join(base_dir, "sitemap.xml")

# API Keys (用户提供的密钥及其变体)
primary_key = "b003561552074f139948d5e6f24f6dc8"
alt_key = "4be524dee1ae400c86d5fb3c724ef3c3c3"

# 1. 写入 API 密钥验证文件到网站根目录
for k in [primary_key, alt_key]:
    txt_path = os.path.join(base_dir, f"{k}.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(k)
    print(f"[Key File Created] {k}.txt")

# 2. 从 sitemap.xml 读取所有 URL
urls = []
if os.path.exists(sitemap_path):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    # 命名空间处理
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in root.findall('.//ns:loc', ns):
        urls.append(loc.text)

print(f"[URLs Loaded] 共提取出 {len(urls)} 个网站 URL 准备推送给 IndexNow。")

# 3. 构造并发送 IndexNow 推送请求
endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow"
]

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) IndexNowNotifier/1.0"
}

def submit_key(key):
    payload = {
        "host": "vpnstuijian.net",
        "key": key,
        "keyLocation": f"https://vpnstuijian.net/{key}.txt",
        "urlList": urls
    }

    data = json.dumps(payload).encode('utf-8')
    print(f"\n--- Submitting URLs to IndexNow for Key: {key} ---")

    for ep in endpoints:
        try:
            req = urllib.request.Request(ep, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"[SUCCESS] Submitted to {ep} - Status Code: {resp.status}")
        except Exception as e:
            print(f"[RESPONSE] {ep}: {e}")

submit_key(primary_key)
if primary_key != alt_key:
    submit_key(alt_key)

print("\n=== IndexNow 极速收录推送完毕！===")
