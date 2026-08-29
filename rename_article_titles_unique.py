import os
import re

base_dir = r"c:\Users\psyto\Desktop\vpnstuijian.net"
articles_dir = os.path.join(base_dir, "articles")

# Mapping of file to new unique title, excerpt, and keywords
titles_map = {
    "subscription-guide.html": {
        "title": "2026年失联与跑路机场黑名单警报：商家圈钱套路复盘与高可用避雷指南",
        "excerpt": "曝光神速云、大麦云、星河云、闪电云、泡芙云等 2026 年确认跑路失联的机场，剖析终身包套路与换皮重开二次收割特征，推荐平价稳定物理专线。",
        "keywords": "2026跑路机场黑名单, 机场失联警报, 换皮二次收割, 避雷指南, 极连云, 光年梯, 边缘节点",
        "description": "曝光神速云、大麦云、星河云、闪电云、泡芙云等 2026 年确认跑路失联的机场，剖析终身包套路与换皮重开二次收割特征，推荐平价稳定物理专线。"
    },
    "airport-runaway-warning-2026.html": {
        "title": "2026年失联与跑路机场黑名单警报：商家圈钱套路复盘与高可用避雷指南",
        "excerpt": "曝光神速云、大麦云、星河云、闪电云、泡芙云等 2026 年确认跑路失联的机场，剖析终身包套路与换皮重开二次收割特征，推荐平价稳定物理专线。",
        "keywords": "2026跑路机场黑名单, 机场失联警报, 换皮二次收割, 避雷指南, 极连云, 光年梯, 边缘节点",
        "description": "曝光神速云、大麦云、星河云、闪电云、泡芙云等 2026 年确认跑路失联的机场，剖析终身包套路与换皮重开二次收割特征，推荐平价稳定物理专线。"
    },
    "2026-august-airport-monthly-report.html": {
        "title": "2026年8月翻墙机场推荐与晚高峰抗封锁实测：8大专线机场稳定度对比",
        "excerpt": "2026年8月最新科学上网梯子与机场推荐选购指南。实时压测极连云、速界、边缘节点、光年梯等8大物理专线晚高峰丢包与连通性，教你避开低价虚标坑。",
        "keywords": "2026年8月机场推荐, 梯子晚高峰实测, 极连云, 速界, 边缘节点, 光年梯, 寰宇云, 物理专线",
        "description": "2026年8月最新科学上网梯子与机场推荐选购指南。实时压测极连云、速界、边缘节点、光年梯等8大物理专线晚高峰丢包与连通性，教你避开低价虚标坑。"
    },
    "ai-productivity-airport-guide.html": {
        "title": "AI开发与办公科学上网指南：搞定ChatGPT 4o与Claude 3.5账号风控的原生住宅IP节点选型",
        "excerpt": "深入分析使用 ChatGPT 4o 与 Claude 3.5 时触发 1020 报错与人机验证的根源，对比数据中心 IP 与真实住宅 IP 差异，推荐专线解封节点。",
        "keywords": "AI科学上网指南, ChatGPT4o风控, Claude3.5解锁, 住宅IP节点, 极连云, 边缘节点, 寰宇云",
        "description": "深入分析使用 ChatGPT 4o 与 Claude 3.5 时触发 1020 报错与人机验证的根源，对比数据中心 IP 与真实住宅 IP 差异，推荐专线解封节点。"
    },
    "hysteria2-vless-anytls-protocol-2026.html": {
        "title": "新一代梯子加密协议大打通：anytls防主动探测、REALITY免域名与Hysteria2极速提速深度拆解",
        "excerpt": "通俗拆解 2026 年主流代理加密协议 anytls、VLESS-REALITY 与 Hysteria 2 的防封锁机理，针对 UDP QoS 限速与网络丢包提供最佳客户端搭配方案。",
        "keywords": "梯子加密协议, anytls防探测, VLESS REALITY, Hysteria2, UDP QoS, Clash Verge, Shadowrocket",
        "description": "通俗拆解 2026 年主流代理加密协议 anytls、VLESS-REALITY 与 Hysteria 2 的防封锁机理，针对 UDP QoS 限速与网络丢包提供最佳客户端搭配方案。"
    },
    "cost-per-gb-buying-guide-2026.html": {
        "title": "买梯子如何不花冤枉钱？算清节点真实GB单价、看透倍率暗扣与便宜月付套餐推荐",
        "excerpt": "教你用简单公式计算机场套餐的实际流量单价，破解商家 3.0x 节点扣费陷阱，为重度追剧党、科研学生与低频用户提供资配建议。",
        "keywords": "买梯子不花冤枉钱, 真实GB单价, 倍率暗扣, 便宜月付机场, 极连云, 寰宇云, 光年梯",
        "description": "教你用简单公式计算机场套餐的实际流量单价，破解商家 3.0x 节点扣费陷阱，为重度追剧党、科研学生与低频用户提供资配建议。"
    }
}

# 1. Update article HTML files
for filename, info in titles_map.items():
    filepath = os.path.join(articles_dir, filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Update <title>
    html = re.sub(r'<title>.*?</title>', f'<title>{info["title"]} - vpn推荐</title>', html)
    # Update <h1 class="article-title-large">
    html = re.sub(r'<h1 class="article-title-large">.*?</h1>', f'<h1 class="article-title-large">{info["title"]}</h1>', html)
    # Update <meta name="description">
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{info["description"]}">', html)
    # Update <meta name="keywords">
    html = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{info["keywords"]}, vpn推荐, 科学上网, vpnstuijian.net">', html)
    # Update AI Summary title reference
    html = re.sub(r'<strong>本章速览（核心结论）：</strong>针对 <strong>.*?</strong>', f'<strong>本章速览（核心结论）：</strong>针对 <strong>{info["title"]}</strong>', html)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated titles in {filename}")

# 2. Update index.html
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

for filename, info in titles_map.items():
    if filename == "airport-runaway-warning-2026.html":
        continue
    # Replace links and titles
    old_title_pattern = rf'<a href="articles/{filename}".*?>(.*?)</a>'
    # Find matching card in index
    pos = index_html.find(f'articles/{filename}')
    if pos != -1:
        # replace title
        title_start = index_html.find('<h3 class="article-card-title">', max(0, pos-200))
        if title_start != -1:
            title_end = index_html.find('</h3>', title_start)
            old_h3 = index_html[title_start:title_end+5]
            new_h3 = f'<h3 class="article-card-title"><a href="articles/{filename}" style="color: inherit; text-decoration: none;">{info["title"]}</a></h3>'
            index_html = index_html.replace(old_h3, new_h3)
            
            # replace excerpt
            p_start = index_html.find('<p class="article-card-excerpt">', title_end)
            if p_start != -1 and p_start < title_end + 300:
                p_end = index_html.find('</p>', p_start)
                old_p = index_html[p_start:p_end+4]
                new_p = f'<p class="article-card-excerpt">{info["excerpt"]}</p>'
                index_html = index_html.replace(old_p, new_p)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
print("Updated index.html card titles and excerpts successfully!")

# 3. Update archives.html
archives_path = os.path.join(base_dir, "archives.html")
with open(archives_path, "r", encoding="utf-8") as f:
    archives_html = f.read()

for filename, info in titles_map.items():
    if filename == "airport-runaway-warning-2026.html":
        continue
    pattern = rf'<a href="articles/{filename}" class="archive-item-title">.*?</a>'
    replacement = f'<a href="articles/{filename}" class="archive-item-title">{info["title"]}</a>'
    archives_html = re.sub(pattern, replacement, archives_html)

with open(archives_path, "w", encoding="utf-8") as f:
    f.write(archives_html)
print("Updated archives.html timeline titles successfully!")

# 4. Update vpn-guide.html
guide_path = os.path.join(base_dir, "vpn-guide.html")
with open(guide_path, "r", encoding="utf-8") as f:
    guide_html = f.read()

for filename, info in titles_map.items():
    if filename == "airport-runaway-warning-2026.html":
        continue
    pos = guide_html.find(f'articles/{filename}')
    if pos != -1:
        title_start = guide_html.find('<span class="guide-article-title">', max(0, pos-100))
        if title_start != -1:
            title_end = guide_html.find('</span>', title_start)
            old_title = guide_html[title_start:title_end+7]
            new_title = f'<span class="guide-article-title">{info["title"]}</span>'
            guide_html = guide_html.replace(old_title, new_title)
            
            excerpt_start = guide_html.find('<span class="guide-article-excerpt">', title_end)
            if excerpt_start != -1 and excerpt_start < title_end + 200:
                excerpt_end = guide_html.find('</span>', excerpt_start)
                old_ex = guide_html[excerpt_start:excerpt_end+7]
                new_ex = f'<span class="guide-article-excerpt">{info["excerpt"]}</span>'
                guide_html = guide_html.replace(old_ex, new_ex)

with open(guide_path, "w", encoding="utf-8") as f:
    f.write(guide_html)
print("Updated vpn-guide.html card titles and excerpts successfully!")
