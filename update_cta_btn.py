import os
import re

site_dir = r'C:\Users\psyto\Desktop\vpnstuijian.net'
css_path = os.path.join(site_dir, 'css', 'style.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace block 1 (around 1312)
css_content = re.sub(
    r'\.cta-btn\s*\{\s*background:\s*var\(--accent-gold-gradient\)[^}]*\}',
    '.cta-btn {\n  background-color: var(--accent-soft);\n  color: var(--accent-primary);\n  font-weight: 700;\n  padding: 10px 24px;\n  border-radius: var(--radius-sm);\n  white-space: nowrap;\n  font-size: 0.9rem;\n  box-shadow: none;\n  border: 1px solid transparent;\n  transition: all var(--transition-fast);\n}',
    css_content
)

css_content = re.sub(
    r'\.cta-btn:hover\s*\{\s*transform:\s*translateY\(-2px\)[^}]*\}',
    '.cta-btn:hover {\n  background-color: var(--accent-primary);\n  color: #ffffff;\n  transform: translateY(-2px);\n  box-shadow: var(--shadow-sm);\n}',
    css_content
)

# Replace block 2 (around 1939)
css_content = re.sub(
    r'\.cta-btn\s*\{\s*flex-shrink:\s*0;\s*background-color:\s*var\(--accent-secondary\)[^}]*\}',
    '.cta-btn {\n  flex-shrink: 0;\n  background-color: var(--accent-soft);\n  color: var(--accent-primary);\n  border: 1px solid transparent;\n  font-size: 0.85rem;\n  font-weight: 700;\n  padding: 10px 20px;\n  border-radius: var(--radius-sm);\n  transition: all var(--transition-fast);\n  white-space: nowrap;\n}',
    css_content
)

css_content = re.sub(
    r'\.cta-btn:hover\s*\{\s*opacity:\s*0\.88;\s*\}',
    '.cta-btn:hover {\n  background-color: var(--accent-primary);\n  color: #ffffff;\n}',
    css_content
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated cta button styles.")
