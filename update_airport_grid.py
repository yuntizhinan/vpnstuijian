import os
import re

site_dir = r'C:\Users\psyto\Desktop\vpnstuijian.net'
css_path = os.path.join(site_dir, 'css', 'style.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace the styles for airport-card, airport-card::after, airport-card:hover, and airport-btn-link
new_airport_card_css = """.airport-card {
  background-color: transparent;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 20px;
  box-shadow: none;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
  transition: background-color var(--transition-fast), border-color var(--transition-fast);
  min-height: 220px;
}

.airport-card:hover {
  background-color: var(--bg-tertiary);
  border-color: var(--border-hover);
  transform: none;
  box-shadow: none;
}

/* 移除渐变装饰条以保持极简 */
.airport-card::after {
  display: none;
}
"""

css_content = re.sub(
    r'\.airport-card\s*\{.*?(?=\.airport-card-header)', 
    new_airport_card_css, 
    css_content, 
    flags=re.DOTALL
)

new_btn_css = """.airport-btn-review {
  background-color: var(--bg-tertiary);
  color: var(--text-secondary);
  border: 1px solid transparent;
}

.airport-btn-review:hover {
  background-color: var(--border-color);
  color: var(--text-primary);
}

.airport-btn-link {
  background-color: var(--accent-primary);
  color: #ffffff;
  border: 1px solid var(--accent-primary);
}

.airport-btn-link:hover {
  background-color: var(--text-primary);
  border-color: var(--text-primary);
}
"""

css_content = re.sub(
    r'\.airport-btn-review\s*\{.*?(?=\/\* ==========================================================================)', 
    new_btn_css + "\n", 
    css_content, 
    flags=re.DOTALL
)

# Fix feature items svg color to match the text or be a subtle blue
css_content = css_content.replace('fill: #0f52ba;', 'fill: var(--accent-primary); opacity: 0.8;')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated airport grid styles.")
