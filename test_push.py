# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import urllib.request
import json
import ssl

base_dir = r"d:\HuaweiMoveData\Users\psyto\Desktop\vpnstuijian.net"
sitemap_path = os.path.join(base_dir, "sitemap.xml")
key = "b003561552074f139948d5e6f24f6dc8"

urls = []
if os.path.exists(sitemap_path):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    ns = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    for loc in root.findall('.//ns:loc', ns):
        urls.append(loc.text)

print(f"Total URLs to push: {len(urls)}")

payload = {
    "host": "vpnstuijian.net",
    "key": key,
    "keyLocation": f"https://vpnstuijian.net/{key}.txt",
    "urlList": urls
}

data = json.dumps(payload, indent=2).encode('utf-8')

# Save payload to json file for reference
with open(os.path.join(base_dir, "indexnow_payload.json"), "w", encoding="utf-8") as f:
    f.write(json.dumps(payload, indent=2, ensure_ascii=False))

headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow"
]

for ep in endpoints:
    print(f"\nSending POST request to: {ep}")
    try:
        req = urllib.request.Request(ep, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            print(f"[SUCCESS!] HTTP Status: {resp.status} - Message: {resp.read().decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"[HTTP Error] Status: {e.code} - Reason: {e.reason}")
        print("Response body:", e.read().decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"[Error] {e}")
