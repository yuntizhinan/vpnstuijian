import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', encoding='utf-8') as f:
    c = f.read()
cnt = c.count('<article class="article-card"')
print('Total article cards:', cnt)
empty = c.find('empty-list-indicator')
print('empty-list-indicator at:', empty)
start = c.find('<div class="articles-feed">')
print('articles-feed starts at:', start)
