# -*- coding: utf-8 -*-
import os
import re

base_dir = r"d:\HuaweiMoveData\Users\psyto\Desktop\vpnstuijian.net"
articles_dir = os.path.join(base_dir, "articles")

# 4个Bing被标红页面的精心长文本描述（80-110汉字 / 150-160字符）
meta_replacements = {
    "index.html": "vpn推荐专注于2026年中国真正好用的电脑VPN、便宜高性价比梯子与顶级IPLC专线机场推荐评测。为您提供极连云、速界、边缘节点、快狸、光年梯、瞬云、寰宇云等主力加速官网订阅入口、1倍率扣费算盘与客户端避坑指南。",
    "streaming-ai-guide.html": "2026年解锁Netflix与ChatGPT等AI工具最佳机场节点选择指南。针对Netflix/Disney+流媒体4K画质解锁，以及ChatGPT 4o、Claude 3.5、TikTok、GitHub、Steam等应用防风控封号提供住宅IP节点分流配置与高速专线机场推荐。",
    "shadowrocket-setup.html": "2026年最新iOS苹果手机Shadowrocket（小火箭）客户端完全配置教程。手把手教您在美区Apple ID购买下载小火箭软件、一键拉取机场节点订阅地址、开启分流与SS/SSR/V2Ray/Hysteria2专线导入，助您实现稳定高速科学上网。",
    "geeknet-warning.html": "2026年极客网络（Geek Net）机场避雷警告与跑路事件全记录。深度拆解极客网络节点重度故障、大面积宕机以及用户退款纠纷始末，并提供识别高风险跑路机场的实用防骗技巧与高可用替代专线机场推荐。"
}

print("=== 开始检查与优化 Bing 提示的所有元描述 (Meta Descriptions) ===")

def process_file(filepath, page_key):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 获取现有描述
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"\s*\/?>', content, re.IGNORECASE)
    if not m:
        print(f"[No Meta Description Found] {os.path.basename(filepath)}")
        return

    curr_desc = m.group(1)
    
    # 如果在特定替换清单中
    if page_key in meta_replacements:
        new_desc = meta_replacements[page_key]
    else:
        # 如果长度不足 75 个汉字（约 150 个字符），进行扩展补全
        if len(curr_desc) < 75:
            new_desc = curr_desc.rstrip("。") + "。提供2026年最新稳定专线机场节点推荐、价格单价换算及各终端科学上网客户端下载与避坑指南。"
        else:
            new_desc = curr_desc

    if new_desc != curr_desc:
        new_content = re.sub(
            r'<meta\s+name="description"\s+content="([^"]+)"\s*\/?>',
            f'<meta name="description" content="{new_desc}">',
            content,
            flags=re.IGNORECASE
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"[Optimized] {page_key} (新长度: {len(new_desc)} 字 / {len(new_desc.encode('utf-8'))} 字节)")
    else:
        print(f"[Pass] {page_key} (长度符合标准: {len(curr_desc)} 字)")

# 处理 index.html
process_file(os.path.join(base_dir, "index.html"), "index.html")

# 处理 articles 目录下的所有文章
if os.path.exists(articles_dir):
    for fname in os.listdir(articles_dir):
        if fname.endswith(".html"):
            fpath = os.path.join(articles_dir, fname)
            process_file(fpath, fname)

print("\n=== 元描述优化完成！===")
