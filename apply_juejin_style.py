import os
import re

site_dir = r'C:\Users\psyto\Desktop\vpnstuijian.net'
css_path = os.path.join(site_dir, 'css', 'style.css')
py_path = os.path.join(site_dir, 'generate_site.py')

# 1. Update style.css
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace .article-card styles
new_article_card_css = """
.article-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
  background-color: transparent;
  border: none;
  border-bottom: 1px solid var(--border-color);
  border-radius: 0;
  padding: 20px 24px;
  box-shadow: none;
  transition: background-color var(--transition-fast);
}

.article-card:hover {
  background-color: var(--bg-tertiary);
  transform: none;
  border-color: var(--border-color);
  box-shadow: none;
}

.article-card-cover {
  width: 200px;
  height: 130px;
  border-radius: var(--radius-sm);
  background-color: var(--bg-tertiary);
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-family: 'Outfit', sans-serif;
  font-size: 1.15rem;
  font-weight: 800;
  border: 1px solid var(--border-color);
  overflow: hidden;
  text-align: center;
  padding: 10px;
}

.article-card-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  flex: 1;
}

.article-card-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 8px;
}

.article-card-title {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 6px;
  line-height: 1.4;
}

.article-card-title a {
  color: var(--text-primary);
  text-decoration: none;
}

.article-card-title a:hover {
  color: var(--accent-primary);
}

.article-card-excerpt {
  font-size: 0.9rem;
  color: var(--text-secondary);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  margin-bottom: 12px;
}

.article-card-footer {
  display: flex;
  align-items: center;
  gap: 12px;
}
"""

css_content = re.sub(
    r'\.article-card\s*\{.*?(?=\.article-card-tags)', 
    new_article_card_css, 
    css_content, 
    flags=re.DOTALL
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update generate_site.py
with open(py_path, 'r', encoding='utf-8') as f:
    py_content = f.read()

# Replace build_article_card_cover_html function
old_build_cover = re.search(r'def build_article_card_cover_html.*?return f"""(.*?)"""\n', py_content, re.DOTALL)
if old_build_cover:
    new_build_cover = """def build_article_card_cover_html(title, cat, slug, tags_list):
    img_url = f"https://picsum.photos/seed/{slug}/140/90"
    return f\"\"\"
        <a href="articles/{slug}.html" class="article-card-cover-graphic" style="flex-shrink: 0; width: 140px; height: 90px; border-radius: 4px; overflow: hidden; display: block; background: var(--bg-tertiary); margin-left: 20px;">
          <img src="{img_url}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" alt="{title}" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </a>
    \"\"\"
"""
    py_content = py_content[:old_build_cover.start()] + new_build_cover + py_content[old_build_cover.end():]

old_science_card_code = """      <article class="article-card" data-categories="science,{sa['cat']}" data-tags="科学上网,科学加速,{tag_label}">
        {build_article_card_cover_html(sa['title'], sa['cat'], sa['slug'], [tag_label, '科普指南'])}
        <div class="article-card-content">
          <div>
            <div class="article-card-meta">
              <span>📅 {sa['date']}</span>
              <span>👁 {sa['views']} 阅读</span>
              <span class="airport-badge" style="background-color: var(--accent-soft); color: var(--accent-primary); border: none;">{tag_label}</span>
            </div>
            <h3 class="article-card-title"><a href="articles/{sa['slug']}.html">{sa['title']}</a></h3>
            <p class="article-card-excerpt">{sa['excerpt']}</p>
          </div>
          <div class="article-card-footer">
            <div class="article-card-tags">
              <span class="tag-pill"># 科学上网</span>
              <span class="tag-pill"># {tag_label}</span>
            </div>
            <a href="articles/{sa['slug'].replace('wavetrans-review', 'naixi-review').replace('guangshuyun-review', 'huacloud-review')}.html" class="read-more-link">
              阅读全文 
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>"""

new_science_card_code = """      <article class="article-card" data-categories="science,{sa['cat']}" data-tags="科学上网,科学加速,{tag_label}">
        <div class="article-card-content">
          <div class="article-card-meta">
            <span style="color: var(--accent-primary); font-weight: 600;">{tag_label}</span>
            <span style="color: var(--border-hover);">|</span>
            <span>{sa['date']}</span>
            <span style="color: var(--border-hover);">|</span>
            <span>{sa['views']} 阅读</span>
          </div>
          <h3 class="article-card-title"><a href="articles/{sa['slug']}.html" style="color: inherit; text-decoration: none;">{sa['title']}</a></h3>
          <p class="article-card-excerpt">{sa['excerpt']}</p>
          <div class="article-card-footer" style="display: flex; gap: 12px;">
            <a href="articles/{sa['slug']}.html" style="font-size: 0.8rem; color: var(--text-muted); text-decoration: none; display: flex; align-items: center; gap: 4px;">
              <svg viewBox="0 0 24 24" style="width: 14px; height: 14px; fill: currentColor;"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg> 阅读全文
            </a>
          </div>
        </div>
        {build_article_card_cover_html(sa['title'], sa['cat'], sa['slug'], [tag_label, '科普指南'])}
      </article>"""

py_content = py_content.replace(old_science_card_code, new_science_card_code)

old_airport_card_code = """      <article class="article-card" data-categories="airport" data-tags="机场推荐,专线节点,稳定高速">
        {build_article_card_cover_html(ap['name'] + ' 测评', 'airport', ap['slug'], ['机场推荐', '专线节点'])}
        <div class="article-card-content">
          <div>
            <div class="article-card-meta">
              <span>📅 {date_val}</span>
              <span>👁 {views_val} 阅读</span>
              <span class="airport-badge" style="background-color: var(--success-soft); color: #166534; border: none;">机场推荐</span>
            </div>
            <h3 class="article-card-title"><a href="articles/{ap['slug']}.html">{ap['name']} 机场评测：高稳定性与极速专线节点官网订阅推荐</a></h3>
            <p class="article-card-excerpt">详细对 {ap['name']} 机场进行多节点速度实测、晚高峰延迟丢包连通监控及套餐资费比对。为希望寻找稳定科学上网梯子的用户提供客观的购买建议和使用体验总结。</p>
          </div>
          <div class="article-card-footer">
            <div class="article-card-tags">
              <span class="tag-pill"># {ap['name']}</span>
              <span class="tag-pill"># 专线机场</span>
            </div>
            <a href="articles/{ap['slug']}.html" class="read-more-link">
              阅读全文
              <svg viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
            </a>
          </div>
        </div>
      </article>"""

new_airport_card_code = """      <article class="article-card" data-categories="airport" data-tags="机场推荐,专线节点,稳定高速">
        <div class="article-card-content">
          <div class="article-card-meta">
            <span style="color: var(--accent-primary); font-weight: 600;">机场推荐</span>
            <span style="color: var(--border-hover);">|</span>
            <span>{date_val}</span>
            <span style="color: var(--border-hover);">|</span>
            <span>{views_val} 阅读</span>
          </div>
          <h3 class="article-card-title"><a href="articles/{ap['slug']}.html" style="color: inherit; text-decoration: none;">{ap['name']} 机场评测：高稳定性与极速专线节点官网订阅推荐</a></h3>
          <p class="article-card-excerpt">详细对 {ap['name']} 机场进行多节点速度实测、晚高峰延迟丢包连通监控及套餐资费比对。为希望寻找稳定科学上网梯子的用户提供客观的购买建议和使用体验总结。</p>
          <div class="article-card-footer" style="display: flex; gap: 12px;">
            <a href="articles/{ap['slug']}.html" style="font-size: 0.8rem; color: var(--text-muted); text-decoration: none; display: flex; align-items: center; gap: 4px;">
              <svg viewBox="0 0 24 24" style="width: 14px; height: 14px; fill: currentColor;"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg> 阅读全文
            </a>
          </div>
        </div>
        {build_article_card_cover_html(ap['name'] + ' 测评', 'airport', ap['slug'], ['机场推荐', '专线节点'])}
      </article>"""

py_content = py_content.replace(old_airport_card_code, new_airport_card_code)

with open(py_path, 'w', encoding='utf-8') as f:
    f.write(py_content)
    
print("Updated CSS and Python template logic.")
