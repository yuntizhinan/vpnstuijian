import os
import re

filepath = r'c:\Users\psyto\Desktop\vpnstuijian.net\generate_site.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# First replace all back to depth=0
content = content.replace('{get_left_sidebar_html(depth=0, page_name="about")}', '{get_left_sidebar_html(depth=0)}')

# Then specifically for write_about, inject the page_name="about"
# In generate_site.py, write_about starts around line 1630.
# We can use regex to find write_about() and replace only inside it.

def replace_in_about(match):
    return match.group(0).replace('{get_left_sidebar_html(depth=0)}', '{get_left_sidebar_html(depth=0, page_name="about")}')

content = re.sub(r'def write_about\(\):.*?(?=print\("about\.html generated successfully\."\))', replace_in_about, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("generate_site.py fixed successfully.")
