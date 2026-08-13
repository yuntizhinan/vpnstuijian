"""
封面图：INS 极简大字设计（第二版：更亮风景图背景 + 超显眼白字）
- 调亮背景：遮罩不透明度大幅调低，画面明亮通透
- 字体显眼：改用常规体（字重稍大），并使用柔和黑晕阴影（Drop Shadow）增强字体的对比度
- 经典磨砂半透明胶囊角标
"""
import os, io, urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_NORMAL = "C:/Windows/Fonts/msyh.ttc"
FONT_BOLD   = "C:/Windows/Fonts/msyhbd.ttc"
OUT_DIR     = r"C:\Users\psyto\Desktop\vpnstuijian.net\images\articles"
CACHE_DIR   = r"C:\Users\psyto\Desktop\vpnstuijian.net\images\articles\_bg_cache"
W, H = 560, 360

os.makedirs(OUT_DIR,   exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)

ARTICLES = {
    "airport-guide-2026":       ("机场排行榜",      "2026 高性价比精选",   "机场评测",  "alpine"),
    "ssr-airport-guide":        ("SSR 机场推荐",    "最稳 V2Ray 节点精选", "机场评测",  "ocean42"),
    "glados-review":            ("GLaDOS 机场",    "免费试用 · 教育优惠", "机场评测",  "forest77"),
    "lantern-alternative":      ("蓝灯替代方案",    "专线中转更稳定",      "机场评测",  "misty81"),
    "vps-vs-airport":           ("自建 vs 机场",   "新手避坑全对比",      "机场评测",  "desert55"),
    "blue-lantern-vpn":         ("蓝灯 VPN",       "老牌工具 连不上？",   "机场评测",  "lake99"),
    "iplc-guide":               ("IPLC/IEPL 专线", "4K不卡顿 低延迟",    "技术进阶",  "night10"),
    "iplc-vs-iepl":             ("IPLC vs IEPL",  "专线架构大科普",      "技术进阶",  "mountain3"),
    "streaming-ai-guide":       ("Netflix · ChatGPT","AI工具加速攻略",   "技术进阶",  "city22"),
    "streaming-unlock":         ("流媒体解锁",     "住宅IP 分流配置",     "技术进阶",  "sunset31"),
    "reality-protocol":         ("Reality 协议",  "最强伪装 防封锁",     "技术进阶",  "dark88"),
    "reality-vless-comparison": ("Reality vs VLESS","安全性横向对比",    "技术进阶",  "forest12"),
    "hysteria2-vs-tuic":        ("Hysteria2 vs Tuic","高丢包最佳协议",  "技术进阶",  "river44"),
    "hy2-performance":          ("Hysteria2 实测", "低带宽提速神器",      "技术进阶",  "snow77"),
    "tuic-latency":             ("Tuic 低延迟",   "游戏加速专题",        "技术进阶",  "cliff33"),
    "trojan-protocol":          ("Trojan 协议",   "TLS伪装 vs V2Ray",  "技术进阶",  "arch66"),
    "clash-tutorial":           ("Clash 配置教程", "节点导入完全指南",    "新手教程",  "road11"),
    "shadowrocket-setup":       ("小火箭 iOS",    "SS/SSR 订阅导入",     "新手教程",  "bay55"),
    "v2rayng-guide":            ("V2RayNG 安卓",  "一键导入订阅地址",     "新手教程",  "hill22"),
    "openwrt-router":           ("OpenWrt 软路由","Clash 节点配置",      "新手教程",  "autumn8"),
    "openwrt-singbox":          ("Sing-box 路由", "高吞吐专线分流",      "新手教程",  "cloud5"),
    "reality-vless-verge":      ("Clash Verge",  "VLESS · Reality 优化","新手教程", "fog99"),
    "shadowrocket-h2":          ("小火箭 + H2",  "UDP提速 晚高峰稳定",   "新手教程",  "valley6"),
    "router-firmware":          ("软路由固件对比", "OpenClash PassWall", "新手教程",  "stream4"),
    "android-vpn-guide":        ("安卓翻墙教程",  "V2RayNG 完全指南",    "新手教程",  "park77"),
    "clash-subscription":       ("订阅地址获取",  "防跑路避坑常识",       "新手教程",  "moon13"),
    "one-multiplier":           ("1倍率机场",     "计费规则 避坑指南",    "优惠活动",  "field2"),
    "free-vpn-risks":           ("免费VPN 隐患",  "七大风险全揭露",       "优惠活动",  "rain9"),
    "shandian-warning":         ("闪电机场 跑路", "Shandian VPN 失联警报","避雷指南",  "storm7"),
    "geeknet-warning":          ("极客网络 故障", "节点宕机 退款纠纷",    "避雷指南",  "fog88"),
    "feitian-warning":          ("飞天梯 停运",   "从盛极一时到关停",     "避雷指南",  "dark55"),
}

def download_bg(seed):
    cache_path = os.path.join(CACHE_DIR, f"{seed}.jpg")
    if os.path.exists(cache_path):
        return Image.open(cache_path).convert("RGB")
    url = f"https://picsum.photos/seed/{seed}/{W}/{H}"
    print(f"  Downloading: {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        img = Image.open(io.BytesIO(data)).convert("RGB").resize((W, H), Image.LANCZOS)
        img.save(cache_path, "JPEG", quality=90)
        return img
    except Exception as e:
        print(f"  WARN: {e}")
        return Image.new("RGB", (W, H), (45, 45, 55))

def text_center_x(draw, text, font):
    return (W - draw.textlength(text, font=font)) / 2

def wrap_line(text, font, draw, max_w):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=font) > max_w:
            lines.append(cur); cur = ch
        else:
            cur += ch
    if cur: lines.append(cur)
    return lines

def draw_text_with_drop_shadow(img, text, font, x, y, fill=(255, 255, 255), shadow_opacity=150, shadow_blur=4):
    """绘制带高品质柔和模糊投影（Drop Shadow）的白色大字，使得在亮背景下依然极其显眼"""
    # 1. 创建临时的 RGBA 阴影画布
    shadow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    # 用纯黑色在相同位置（稍微往右下方偏 2 像素）绘制文字作为阴影基础
    s_draw.text((x + 1, y + 2), text, font=font, fill=(0, 0, 0, shadow_opacity))
    # 2. 高斯模糊阴影层，形成极其自然的文字晕影
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=shadow_blur))
    # 3. 将阴影贴回主图
    img.paste(shadow_layer, (0, 0), shadow_layer)
    
    # 4. 在原位置绘制亮白色的实体字
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, font=font, fill=fill)

try:
    # 选用常规体 (msyh.ttc)，使字面更饱满，白字面积变大，从而更加清晰显眼
    font_title  = ImageFont.truetype(FONT_NORMAL, 56)
    font_sub    = ImageFont.truetype(FONT_NORMAL, 26)
    font_badge  = ImageFont.truetype(FONT_NORMAL, 17)
except Exception as e:
    print(f"Font error: {e}"); raise

for slug, (title_raw, sub_raw, badge, bg_seed) in ARTICLES.items():
    print(f"Building {slug}...")

    # ── 1. 风景背景（去除模糊，直接还原高清亮色风景）
    bg = download_bg(bg_seed)

    # ── 2. 更加轻薄、透亮的暗色遮罩（降低不透明度 alpha，使图片整体显得非常明亮）
    overlay = Image.new("RGBA", (W, H), (0,0,0,0))
    ov = ImageDraw.Draw(overlay)
    for y_px in range(H):
        t = y_px / H
        # 大幅降低遮罩浓度：从原来的 90-160 降低到 50-100，让风景图的亮度和鲜明度最大化还原
        alpha = int(50 + 55 * t)
        ov.line([(0, y_px), (W, y_px)], fill=(0, 0, 0, alpha))

    # ── 3. Vignette（晕影也相应调弱调亮）
    vig = Image.new("RGBA", (W, H), (0,0,0,0))
    vd  = ImageDraw.Draw(vig)
    for i in range(50):
        a = int(35 * ((1 - i/50) ** 2))
        vd.rectangle([i, i, W-i, H-i], outline=(0, 0, 0, a))

    img = Image.alpha_composite(bg.convert("RGBA"), overlay)
    img = Image.alpha_composite(img, vig).convert("RGB")

    # ── 4. 角标 — 半透明磨砂胶囊，背景稍微加深一点点以在亮风景图中更加凸显
    draw = ImageDraw.Draw(img)
    tw_b = int(draw.textlength(badge, font=font_badge))
    bpx, bpy = 12, 5
    bw, bh = tw_b + bpx*2, 26
    badge_img = Image.new("RGBA", (bw + 2, bh + 2), (0,0,0,0))
    bd = ImageDraw.Draw(badge_img)
    bd.rounded_rectangle([0, 0, bw, bh], radius=13, fill=(0, 0, 0, 80)) # 改用暗磨砂，搭配亮色背景
    bd.rounded_rectangle([0, 0, bw, bh], radius=13, outline=(255, 255, 255, 100), width=1)
    
    img.paste(badge_img, (16, 16), badge_img)
    
    draw = ImageDraw.Draw(img)
    draw.text((16+bpx, 16+bpy), badge, font=font_badge, fill=(255, 255, 255, 220))

    # ── 5. 换行计算
    lines = wrap_line(title_raw, font_title, draw, W - 60)

    line_h  = 68
    sub_gap = 14
    sub_lh  = 34
    sep_h   = 16

    total_h = len(lines[:2]) * line_h + sep_h + sub_lh
    y = (H - total_h) // 2

    # ── 6. 大标题：使用 Drop Shadow 晕影技术渲染，实现白字无比显眼但边缘自然
    for line in lines[:2]:
        tw = draw.textlength(line, font=font_title)
        x  = (W - tw) / 2
        draw_text_with_drop_shadow(img, line, font_title, x, y, fill=(255, 255, 255), shadow_opacity=180, shadow_blur=4)
        y += line_h

    # ── 7. 细分割线
    draw = ImageDraw.Draw(img)
    y += 2
    lw = 40
    lx = (W - lw) // 2
    draw.line([(lx, y), (lx+lw, y)], fill=(255, 255, 255, 140), width=1)
    y += sep_h

    # ── 8. 副标题：同样用微投影，提升亮背景下的显眼度
    sub_lines = wrap_line(sub_raw, font_sub, draw, W - 80)
    for line in sub_lines[:2]:
        tw = draw.textlength(line, font=font_sub)
        x  = (W - tw) / 2
        draw_text_with_drop_shadow(img, line, font_sub, x, y, fill=(240, 240, 240), shadow_opacity=160, shadow_blur=3)
        y += sub_lh

    # ── 9. 保存
    img.save(os.path.join(OUT_DIR, f"{slug}.jpg"), "JPEG", quality=92)

print(f"\nAll done! {len(ARTICLES)} covers generated.")
