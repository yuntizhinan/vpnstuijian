import os
import re

base_dir = r"c:\Users\psyto\Desktop\vpnstuijian.net"
guide_path = os.path.join(base_dir, "vpn-guide.html")
archives_path = os.path.join(base_dir, "archives.html")

# 1. Update vpn-guide.html
with open(guide_path, "r", encoding="utf-8") as f:
    guide_content = f.read()

# Update count in summary text
guide_content = re.sub(r'收录 <strong>\d+</strong> 篇', '收录 <strong>36</strong> 篇', guide_content)

# Insert into 🏆 机场评测与横向排行
item_monthly = """          <a href="articles/2026-august-airport-monthly-report.html" class="guide-article-item">
            <span class="guide-article-index">01</span>
            <div class="guide-article-body">
              <span class="guide-article-title">2026年8月全球科学上网风向标：晚高峰骨干网压测报告与跑路黑名单防坑指南</span>
              <span class="guide-article-excerpt">针对8月骨干网波动，实测极连云、速界、边缘节点、光年梯、寰宇云等晚高峰表现，并提供防跑路实用技巧。...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-08-27</span>
              <span class="guide-article-views">👁 1840</span>
            </div>
          </a>
"""

# Insert into 🛠️ 新手入门与配置教程
item_ai = """          <a href="articles/ai-productivity-airport-guide.html" class="guide-article-item">
            <span class="guide-article-index">01</span>
            <div class="guide-article-body">
              <span class="guide-article-title">2026 ChatGPT 4o 与 Claude 3.5 极速加速攻略：如何挑选原生住宅 IP 节点与防 1020 报错</span>
              <span class="guide-article-excerpt">详解 ChatGPT 4o 与 Claude 3.5 报错 1020 的根本原因。对比数据中心 IP 与原生住宅 IP 差异，推荐全绿解锁机场...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-08-27</span>
              <span class="guide-article-views">👁 2310</span>
            </div>
          </a>
"""

# Insert into 🔬 网络专线与技术进阶
item_protocol = """          <a href="articles/hysteria2-vless-anytls-protocol-2026.html" class="guide-article-item">
            <span class="guide-article-index">01</span>
            <div class="guide-article-body">
              <span class="guide-article-title">2026网络翻墙黑科技解析：Hysteria 2 拥塞提速、VLESS-REALITY 伪装与 anytls 防封锁深度对比</span>
              <span class="guide-article-excerpt">深入剖析 2026 年三大新一代翻墙协议 Hysteria 2、VLESS-REALITY 与 anytls 的底层技术差异，提供 UDP QoS 解法...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-08-27</span>
              <span class="guide-article-views">👁 2150</span>
            </div>
          </a>
"""

# Insert into 💰 高性价比与优惠活动
item_cost = """          <a href="articles/cost-per-gb-buying-guide-2026.html" class="guide-article-item">
            <span class="guide-article-index">01</span>
            <div class="guide-article-body">
              <span class="guide-article-title">2026科学上网避坑指南：看破节点高倍率陷阱、计算机场真实性价比与套餐搭配</span>
              <span class="guide-article-excerpt">教您如何在买机场时拆解 3x~5x 扣费倍率陷阱。提供实际 GB 单价换算公式，对比月付套餐与不限时流量包的划算程度...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-08-27</span>
              <span class="guide-article-views">👁 1980</span>
            </div>
          </a>
"""

# New Category Block for 🛡️ 避雷指南与跑路黑名单
block_warning = """        <div class="guide-category-block">
          <div class="guide-category-header">
            <span class="guide-category-icon">🛡️</span>
            <div>
              <h2 class="guide-category-title">避雷预警与跑路黑名单</h2>
              <p class="guide-category-desc">曝光跑路失联机场，深度拆解黑灰产套路与防跑路原则。</p>
            </div>
            <span class="guide-category-count">4 篇</span>
          </div>
          <div class="guide-articles-list">
            
          <a href="articles/subscription-guide.html" class="guide-article-item">
            <span class="guide-article-index">01</span>
            <div class="guide-article-body">
              <span class="guide-article-title">2026年VPN机场跑路名单汇总 | 机场跑路黑名单、跑路原因与避坑指南</span>
              <span class="guide-article-excerpt">曝光神速云、大麦云、星河云、闪电云、泡芙云、三番云等失联跑路服务商，拆解换皮洗库二次收费套路，推荐高可用专线标杆。...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-08-27</span>
              <span class="guide-article-views">👁 3181</span>
            </div>
          </a>
          <a href="articles/shandian-warning.html" class="guide-article-item">
            <span class="guide-article-index">02</span>
            <div class="guide-article-body">
              <span class="guide-article-title">闪电机场跑路避雷：Shandian VPN失联始末与高风险机场识别指南</span>
              <span class="guide-article-excerpt">闪电机场（Shandian VPN）跑路避雷警报，深度揭露其失联始末、用户损失及识别高风险机场的实用防骗技巧。...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-07-28</span>
              <span class="guide-article-views">👁 1420</span>
            </div>
          </a>
          <a href="articles/geeknet-warning.html" class="guide-article-item">
            <span class="guide-article-index">03</span>
            <div class="guide-article-body">
              <span class="guide-article-title">极客网络避雷警告：Geek Net节点重度故障与用户退款纠纷全记录</span>
              <span class="guide-article-excerpt">记录极客网络节点大面积故障与用户退款纠纷始末，为选择避坑机场提供防骗警示。...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-07-26</span>
              <span class="guide-article-views">👁 1180</span>
            </div>
          </a>
          <a href="articles/feitian-warning.html" class="guide-article-item">
            <span class="guide-article-index">04</span>
            <div class="guide-article-body">
              <span class="guide-article-title">飞天梯停止运营避雷：Feitian从盛极一时到突然关停的全过程复盘</span>
              <span class="guide-article-excerpt">复盘飞天梯关停始末，剖析小机场资金链断裂根源，提供防范长周期套餐跑路建议。...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 2026-07-25</span>
              <span class="guide-article-views">👁 1250</span>
            </div>
          </a>
          </div>
        </div>
"""

# Insert monthly report into category 1
if "2026-august-airport-monthly-report.html" not in guide_content:
    cat1_marker = '<h2 class="guide-category-title">机场评测与横向排行</h2>'
    cat1_pos = guide_content.find(cat1_marker)
    if cat1_pos != -1:
        list_start = guide_content.find('<div class="guide-articles-list">', cat1_pos)
        if list_start != -1:
            insert_point = list_start + len('<div class="guide-articles-list">\n            \n')
            guide_content = guide_content[:insert_point] + item_monthly + guide_content[insert_point:]

# Insert AI guide into category 2
if "ai-productivity-airport-guide.html" not in guide_content:
    cat2_marker = '<h2 class="guide-category-title">新手入门与配置教程</h2>'
    cat2_pos = guide_content.find(cat2_marker)
    if cat2_pos != -1:
        list_start = guide_content.find('<div class="guide-articles-list">', cat2_pos)
        if list_start != -1:
            insert_point = list_start + len('<div class="guide-articles-list">\n            \n')
            guide_content = guide_content[:insert_point] + item_ai + guide_content[insert_point:]

# Insert protocol into category 3
if "hysteria2-vless-anytls-protocol-2026.html" not in guide_content:
    cat3_marker = '<h2 class="guide-category-title">网络专线与技术进阶</h2>'
    cat3_pos = guide_content.find(cat3_marker)
    if cat3_pos != -1:
        list_start = guide_content.find('<div class="guide-articles-list">', cat3_pos)
        if list_start != -1:
            insert_point = list_start + len('<div class="guide-articles-list">\n            \n')
            guide_content = guide_content[:insert_point] + item_protocol + guide_content[insert_point:]

# Insert cost into category 4
if "cost-per-gb-buying-guide-2026.html" not in guide_content:
    cat4_marker = '<h2 class="guide-category-title">高性价比与优惠活动</h2>'
    cat4_pos = guide_content.find(cat4_marker)
    if cat4_pos != -1:
        list_start = guide_content.find('<div class="guide-articles-list">', cat4_pos)
        if list_start != -1:
            insert_point = list_start + len('<div class="guide-articles-list">\n            \n')
            guide_content = guide_content[:insert_point] + item_cost + guide_content[insert_point:]

# Append block_warning before </article>
if "避雷预警与跑路黑名单" not in guide_content:
    article_end = guide_content.find('</article>')
    if article_end != -1:
        guide_content = guide_content[:article_end] + block_warning + guide_content[article_end:]

with open(guide_path, "w", encoding="utf-8") as f:
    f.write(guide_content)

print("Updated vpn-guide.html (干货分享) successfully!")

# 2. Check and verify archives.html
with open(archives_path, "r", encoding="utf-8") as f:
    archives_content = f.read()

# Make sure 2026-august-airport-monthly-report.html is present in archives.html
assert "2026-august-airport-monthly-report.html" in archives_content, "Missing monthly report in archives.html"
assert "subscription-guide.html" in archives_content, "Missing subscription-guide.html in archives.html"
assert "ai-productivity-airport-guide.html" in archives_content, "Missing ai guide in archives.html"
assert "hysteria2-vless-anytls-protocol-2026.html" in archives_content, "Missing protocol in archives.html"
assert "cost-per-gb-buying-guide-2026.html" in archives_content, "Missing cost guide in archives.html"

print("Verified archives.html (文章归档) - all 5 new articles are present and indexed!")
