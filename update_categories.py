import os
import re

filepath = r'c:\Users\psyto\Desktop\vpnstuijian.net\generate_site.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update science_articles categories
content = content.replace("'cat': 'speed'", "'cat': 'tech'")
content = content.replace("'cat': 'app'", "'cat': 'tech'")
content = content.replace("'cat': 'proto'", "'cat': 'tech'")
content = content.replace("'cat': 'op'", "'cat': 'guide'")
content = content.replace("'cat': 'cost'", "'cat': 'promo'")

# 2. Update cat_items (sidebar)
old_cat_items = """    cat_items = [
        {'name': '全部文章', 'slug': 'all'},
        {'name': '排行评测', 'slug': 'eval'},
        {'name': '便宜月付', 'slug': 'cost'},
        {'name': '游戏专线', 'slug': 'speed'},
        {'name': '流媒体/AI', 'slug': 'app'},
        {'name': '协议科普', 'slug': 'proto'},
        {'name': '导入配置', 'slug': 'op'}
    ]"""

new_cat_items = """    cat_items = [
        {'name': '全部文章', 'slug': 'all'},
        {'name': '机场评测', 'slug': 'eval'},
        {'name': '新手教程', 'slug': 'guide'},
        {'name': '技术进阶', 'slug': 'tech'},
        {'name': '优惠活动', 'slug': 'promo'}
    ]"""
content = content.replace(old_cat_items, new_cat_items)

# 3. Update categories in write_vpn_guide
old_categories = """    categories = [
        {'key': 'eval',  'icon': '🏆', 'label': '机场评测与横向排行', 'desc': '深度评测、性价比横向对比，帮你选出最适合自己的机场。'},
        {'key': 'cost',  'icon': '💰', 'label': '便宜月付与计费避坑', 'desc': '流量计费规则解析、低价高性价比套餐与订阅防跑路指南。'},
        {'key': 'speed', 'icon': '⚡', 'label': '专线科普与游戏加速', 'desc': 'IPLC/IEPL物理专线原理、游戏低延迟节点选择全攻略。'},
        {'key': 'app',   'icon': '🎬', 'label': '流媒体与AI工具解锁', 'desc': 'Netflix、Disney+、ChatGPT、TikTok等平台加速与解锁配置。'},
        {'key': 'proto', 'icon': '🔬', 'label': '底层协议技术科普', 'desc': 'Reality、Hysteria2、TUIC、Trojan等新一代协议原理深度解析。'},
        {'key': 'op',    'icon': '🛠️', 'label': '客户端配置实战教程', 'desc': 'Clash、Shadowrocket、V2RayNG、OpenWrt软路由一步一步实操。'},
    ]"""

new_categories = """    categories = [
        {'key': 'eval',  'icon': '🏆', 'label': '机场评测与横向排行', 'desc': '深度评测、性价比横向对比，帮你选出最适合自己的机场。'},
        {'key': 'guide', 'icon': '🛠️', 'label': '新手入门与配置教程', 'desc': 'Clash、Shadowrocket、V2RayNG等客户端一键导入配置实战。'},
        {'key': 'tech',  'icon': '🔬', 'label': '网络专线与技术进阶', 'desc': '专线科普、流媒体解锁、新一代协议原理深度解析。'},
        {'key': 'promo', 'icon': '💰', 'label': '高性价比与优惠活动', 'desc': '便宜月付方案、流量计费规则解析与高性价比套餐。'}
    ]"""
content = content.replace(old_categories, new_categories)

# 4. Update cat_labels in write_index
old_cat_labels = """        cat_labels = {
            'eval': '排行评测', 'cost': '便宜月付', 'speed': '游戏专线', 'app': '流媒体/AI', 'proto': '协议科普', 'op': '导入配置'
        }"""
new_cat_labels = """        cat_labels = {
            'eval': '机场评测', 'guide': '新手教程', 'tech': '技术进阶', 'promo': '优惠活动'
        }"""
content = content.replace(old_cat_labels, new_cat_labels)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("generate_site.py updated successfully.")
