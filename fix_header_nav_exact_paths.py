import re

gen_path = r"c:\Users\psyto\Desktop\vpnstuijian.net\generate_site.py"

with open(gen_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 在 generate_site.py 中修改 get_header_html 的科普文章下拉菜单生成逻辑

old_header_func = '''# 统一生成公共 Header (深度 depth=0 表示根目录，depth=1 表示 articles 文件夹内)
def get_header_html(depth=0):
    prefix = "" if depth == 0 else "../"
    
    # 机场推荐下拉单列表
    airport_dropdown = ""
    for ap in airports:
        link_val = f"articles/{ap['slug']}.html" if depth == 0 else f"{ap['slug']}.html"
        airport_dropdown += f'<a href="{prefix}{link_val}" class="dropdown-item">{ap[\'name\']} 测评</a>\\n' '''

new_header_func = '''# 辅助获取文章跳转相对路径
def get_article_link(slug, depth=0):
    return f"articles/{slug}.html" if depth == 0 else f"{slug}.html"

# 统一生成公共 Header (深度 depth=0 表示根目录，depth=1 表示 articles 文件夹内)
def get_header_html(depth=0):
    prefix = "" if depth == 0 else "../"
    
    # 机场推荐下拉单列表
    airport_dropdown = ""
    for ap in airports:
        link_val = get_article_link(ap['slug'], depth)
        airport_dropdown += f'<a href="{link_val}" class="dropdown-item">{ap[\'name\']} 测评</a>\\n' '''

content = re.sub(r'# 统一生成公共 Header.*?(?=html = f"""|\Z)', '''# 辅助获取文章跳转相对路径
def get_article_link(slug, depth=0):
    return f"articles/{slug}.html" if depth == 0 else f"{slug}.html"

# 统一生成公共 Header (深度 depth=0 表示根目录，depth=1 表示 articles 文件夹内)
def get_header_html(depth=0):
    prefix = "" if depth == 0 else "../"
    
    # 机场推荐下拉单列表
    airport_dropdown = ""
    for ap in airports:
        link_val = get_article_link(ap['slug'], depth)
        airport_dropdown += f'<a href="{link_val}" class="dropdown-item">{ap["name"]} 测评</a>\\n'
''', content, flags=re.DOTALL)

# 替换 科普文章 下拉菜单部分
old_science_block = '''        <!-- 科普文章 (下拉式，支持主标题与子项直接精准跳转文章) -->
        <div class="nav-item">
          <a href="{prefix}vpn-guide.html" class="nav-link dropdown-toggle">科普文章 <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="{prefix}{'articles/' if depth == 0 else ''}airport-guide-2026.html" class="dropdown-item">机场排行与评测</a>
            <a href="{prefix}{'articles/' if depth == 0 else ''}one-multiplier.html" class="dropdown-item">便宜月付推荐</a>
            <a href="{prefix}{'articles/' if depth == 0 else ''}iplc-guide.html" class="dropdown-item">专线与游戏加速</a>
            <a href="{prefix}{'articles/' if depth == 0 else ''}streaming-ai-guide.html" class="dropdown-item">流媒体/AI解锁</a>
            <a href="{prefix}{'articles/' if depth == 0 else ''}reality-protocol.html" class="dropdown-item">底层协议技术</a>
            <a href="{prefix}{'articles/' if depth == 0 else ''}clash-tutorial.html" class="dropdown-item">客户端导入教程</a>
          </div>
        </div>'''

new_science_block = '''        <!-- 科普文章 (下拉式，支持主标题与子项直接精准跳转文章) -->
        <div class="nav-item">
          <a href="{prefix}vpn-guide.html" class="nav-link dropdown-toggle">科普文章 <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="{get_article_link('airport-guide-2026', depth)}" class="dropdown-item">机场排行与评测</a>
            <a href="{get_article_link('one-multiplier', depth)}" class="dropdown-item">便宜月付推荐</a>
            <a href="{get_article_link('iplc-guide', depth)}" class="dropdown-item">专线与游戏加速</a>
            <a href="{get_article_link('streaming-ai-guide', depth)}" class="dropdown-item">流媒体/AI解锁</a>
            <a href="{get_article_link('reality-protocol', depth)}" class="dropdown-item">底层协议技术</a>
            <a href="{get_article_link('clash-tutorial', depth)}" class="dropdown-item">客户端导入教程</a>
          </div>
        </div>'''

content = content.replace(old_science_block, new_science_block)

with open(gen_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("generate_site.py updated with get_article_link.")
