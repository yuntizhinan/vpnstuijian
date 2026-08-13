import os
import re

site_dir = r'C:\Users\psyto\Desktop\vpnstuijian.net'
css_path = os.path.join(site_dir, 'css', 'style.css')

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace block 1 (around line 516)
css_content = re.sub(
    r'\.profile-btn-primary\s*\{[^}]*\}',
    '.profile-btn-primary {\n  background-color: var(--accent-soft);\n  color: var(--accent-primary);\n  border: 1px solid transparent;\n}',
    css_content
)

css_content = re.sub(
    r'\.profile-btn-primary:hover\s*\{[^}]*\}',
    '.profile-btn-primary:hover {\n  background-color: var(--accent-primary);\n  color: #ffffff;\n}',
    css_content
)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated profile button styles.")
