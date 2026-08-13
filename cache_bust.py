import os
import re
import time

site_dir = r'C:\Users\psyto\Desktop\vpnstuijian.net'
py_path = os.path.join(site_dir, 'generate_site.py')

with open(py_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Generate a unique timestamp for cache busting
version = int(time.time())
cache_buster = f"style.css?v={version}"

# Replace occurrences of style.css (and any old query strings) with the new one
new_content = re.sub(r'style\.css(\?v=\d+)?', cache_buster, content)

with open(py_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Added cache busting to style.css links in generate_site.py.")
