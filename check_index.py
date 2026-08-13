import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', encoding='utf-8') as f:
    content = f.read()
print('articles-feed found:', 'articles-feed' in content)
print('article-card count:', content.count('class="article-card'))
print('pagination found:', 'pagination' in content)
idx = content.find('articles-feed')
if idx != -1:
    print('Context:')
    print(content[idx-50:idx+300])
