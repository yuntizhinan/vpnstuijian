import os
import re

site_dir = r'C:\Users\psyto\Desktop\vpnstuijian.net'
css_path = os.path.join(site_dir, 'css', 'style.css')
py_path = os.path.join(site_dir, 'generate_site.py')

# 1. Update style.css
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

new_sidebar_promo = """.sidebar-promo-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sidebar-promo-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 16px;
  border-radius: var(--radius-sm);
  text-decoration: none;
  transition: all var(--transition-fast);
  position: relative;
  overflow: hidden;
  box-shadow: none;
  border: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
}

.sidebar-promo-card:hover {
  background-color: var(--bg-primary);
  border-color: var(--border-hover);
}

.promo-card-left {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
  padding-right: 12px;
  z-index: 2;
}

.promo-card-title {
  font-size: 0.95rem;
  font-weight: 700;
  margin: 0;
  color: var(--text-primary);
}

.promo-card-desc {
  font-size: 0.75rem;
  margin: 0;
  line-height: 1.4;
  color: var(--text-secondary);
}

.promo-card-btn {
  align-self: flex-start;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 4px;
  margin-top: 6px;
  color: var(--accent-primary);
  background-color: var(--accent-soft);
  transition: background-color var(--transition-fast), color var(--transition-fast);
}

.sidebar-promo-card:hover .promo-card-btn {
  background-color: var(--accent-primary);
  color: #fff;
}
"""

css_content = re.sub(
    r'\.sidebar-promo-container\s*\{.*?(?=\.promo-card-right\s*\{)', 
    new_sidebar_promo, 
    css_content, 
    flags=re.DOTALL
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update generate_site.py
with open(py_path, 'r', encoding='utf-8') as f:
    py_content = f.read()

# Replace the HTML for promo card to remove inline styles and use simple class
old_promo_html = """            <a href="{prefix}{link_path}" class="sidebar-promo-card" style="background: {p['style']};">
              <div class="promo-card-left">
                <h4 class="promo-card-title">{p['name']} 机场</h4>
                <p class="promo-card-desc">{p['desc']}</p>
                <span class="promo-card-btn {p['btn_class']}">立即评测</span>
              </div>
              <div class="promo-card-right">
                <img src="{p['logo']}" alt="{p['name']}" class="promo-card-logo">
              </div>
            </a>"""

new_promo_html = """            <a href="{prefix}{link_path}" class="sidebar-promo-card">
              <div class="promo-card-left">
                <h4 class="promo-card-title">{p['name']} 机场</h4>
                <p class="promo-card-desc">{p['desc']}</p>
                <span class="promo-card-btn">立即评测</span>
              </div>
              <div class="promo-card-right">
                <img src="{p['logo']}" alt="{p['name']}" class="promo-card-logo">
              </div>
            </a>"""

py_content = py_content.replace(old_promo_html, new_promo_html)

with open(py_path, 'w', encoding='utf-8') as f:
    f.write(py_content)

print("Updated promo sidebar card styling to match minimalist design.")
