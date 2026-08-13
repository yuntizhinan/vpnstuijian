import os
import re

filepath = r'c:\Users\psyto\Desktop\vpnstuijian.net\generate_site.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update archives call
old_archives_call = """      <!-- Left Column -->
      {get_left_sidebar_html(depth=0)}"""

new_archives_call = """      <!-- Left Column -->
      {get_left_sidebar_html(depth=0, page_name="archives")}"""

# Use regex to just replace inside write_archives
def replace_in_archives(match):
    return match.group(0).replace(old_archives_call, new_archives_call)

content = re.sub(r'def write_archives\(\):.*?(?=print\("archives\.html generated successfully\."\))', replace_in_archives, content, flags=re.DOTALL)

# 2. Modify the `else:` branch of `if depth == 0:` to conditionally omit `promo_widget_html`
old_else_block = """        else:
            # 主页: 完整大侧栏
            sidebar_inner_html = f\"\"\"
        <div class="sidebar-card profile-card\">"""

new_else_block = """        else:
            # 主页: 完整大侧栏
            promo_section = "" if page_name == "archives" else promo_widget_html
            sidebar_inner_html = f\"\"\"
        <div class="sidebar-card profile-card\">"""

content = content.replace(old_else_block, new_else_block)

old_promo_placeholder = """        {hot_widget_html}
        {promo_widget_html}
        \"\"\""""

new_promo_placeholder = """        {hot_widget_html}
        {promo_section}
        \"\"\""""

# Only replace the one in the `else` block we care about
# We know it's right before `else:` of `if depth == 0:`... wait, it's before `else:` of `if depth == 0:` is closed.
# It's at the end of the `if depth == 0:` block.
content = content.replace(old_promo_placeholder, new_promo_placeholder)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("generate_site.py updated successfully for archives sidebar.")
