import os
import re

filepath = r'c:\Users\psyto\Desktop\vpnstuijian.net\generate_site.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update get_left_sidebar_html signature
content = content.replace(
    'def get_left_sidebar_html(depth=0, toc_links_html="", cta_card_html="", article_tags=None, body_content=""):',
    'def get_left_sidebar_html(depth=0, toc_links_html="", cta_card_html="", article_tags=None, body_content="", page_name=""):')

# 2. Update logic inside depth == 0
old_sidebar_logic = """    # 主页 vs 文章页 侧边栏卡片输出差异
    if depth == 0:
        # 主页: 完整大侧栏
        sidebar_inner_html = f\"\"\"
        <div class="sidebar-card profile-card\">"""

new_sidebar_logic = """    # 主页 vs 文章页 侧边栏卡片输出差异
    if depth == 0:
        if page_name == "about":
            sidebar_inner_html = f\"\"\"
        <div class="sidebar-card profile-card">
          <div class="profile-avatar" style="width: 86px; height: 86px; margin: 0 auto 14px; border-radius: 50%; overflow: hidden; border: 3px solid var(--accent-primary); box-shadow: 0 4px 16px rgba(15, 82, 186, 0.25); background: #ffffff; padding: 3px;">
            <img src="{prefix}images/profile_avatar.png" alt="vpn推荐" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%; display: block;">
          </div>
          <h3 class="profile-name">vpn推荐</h3>
          <p class="profile-motto">vpnstuijian.net 专注于2026年最新、最稳的国际物理专线、BGP中继翻墙机场评测与科学上网客户端避坑科普。</p>
          <div class="profile-stats">
            <div class="stat-item">
              <span class="stat-value">{total_posts}</span>
              <span class="stat-label">文章数</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{total_tags}</span>
              <span class="stat-label">标签数</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{daily_views}</span>
              <span class="stat-label">日访问量</span>
            </div>
          </div>
          <div class="profile-buttons">
            <a href="{prefix}about.html" class="profile-btn profile-btn-primary">关于我们</a>
            <a href="{prefix}vpn-guide.html" class="profile-btn profile-btn-secondary">科普专栏</a>
          </div>
        </div>
        
        <div class="sidebar-card">
          <h3 class="toc-title">分类目录</h3>
          {categories_html}
        </div>

        {cta_widget_html}
        \"\"\"
        else:
            # 主页: 完整大侧栏
            sidebar_inner_html = f\"\"\"
        <div class="sidebar-card profile-card\">"""

content = content.replace(old_sidebar_logic, new_sidebar_logic)

# 3. Update write_about call
old_about_call = """      <!-- Left Column -->
      {get_left_sidebar_html(depth=0)}
      
      <!-- Middle Column -->"""

new_about_call = """      <!-- Left Column -->
      {get_left_sidebar_html(depth=0, page_name="about")}
      
      <!-- Middle Column -->"""

content = content.replace(old_about_call, new_about_call)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("generate_site.py updated successfully.")
