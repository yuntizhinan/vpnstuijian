import os

filepath = r'c:\Users\psyto\Desktop\vpnstuijian.net\generate_site.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1 & 2: Pass page_name=slug to get_left_sidebar_html calls in article loops
content = content.replace(
    '{get_left_sidebar_html(depth=1, toc_links_html=toc_html, cta_card_html=cta_html, article_tags=extracted_tags, body_content=body_content)}',
    '{get_left_sidebar_html(depth=1, toc_links_html=toc_html, cta_card_html=cta_html, article_tags=extracted_tags, body_content=body_content, page_name=slug)}'
)
content = content.replace(
    '{get_left_sidebar_html(depth=1, toc_links_html=toc_html, cta_card_html=article_cta_html, article_tags=extracted_tags, body_content=body_content)}',
    '{get_left_sidebar_html(depth=1, toc_links_html=toc_html, cta_card_html=article_cta_html, article_tags=extracted_tags, body_content=body_content, page_name=slug)}'
)

# 3: Add hot_widget_html at the end for depth=1 if page_name == "airport-guide-2026"
old_else_block = """    else:
        # 文章页: 精简轻量侧栏 (优先展示大纲, 避免拉长超标，左右对齐)
        tags_title = "本文标签" if article_tags else "热门标签\""""
        
new_else_block = """    else:
        # 文章页: 精简轻量侧栏 (优先展示大纲, 避免拉长超标，左右对齐)
        tags_title = "本文标签" if article_tags else "热门标签"
        hot_section = hot_widget_html if page_name == "airport-guide-2026" else \"\"\"\""""

content = content.replace(old_else_block, new_else_block)

old_promo_widget = """        <div class="sidebar-card">
          <h3 class="toc-title">{tags_title}</h3>
          <div class="tags-cloud">
            {tags_content}
          </div>
        </div>

        {promo_widget_html}
        \"\"\""""

new_promo_widget = """        <div class="sidebar-card">
          <h3 class="toc-title">{tags_title}</h3>
          <div class="tags-cloud">
            {tags_content}
          </div>
        </div>

        {promo_widget_html}
        {hot_section}
        \"\"\""""

content = content.replace(old_promo_widget, new_promo_widget)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("generate_site.py updated successfully for hot widget on airport-guide-2026.")
