pagination_css = """
/* ==========================================================================
   文章列表分页导航 (pagination-nav)
   ========================================================================== */
.pagination-nav {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 24px 0 8px;
  flex-wrap: wrap;
}

.page-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 38px;
  height: 38px;
  padding: 0 10px;
  border-radius: var(--radius-md);
  font-size: 0.88rem;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  cursor: pointer;
  border: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
  color: var(--text-secondary);
  transition: all var(--transition-fast);
  user-select: none;
  box-shadow: var(--shadow-sm);
}

.page-btn:hover:not(:disabled) {
  border-color: var(--accent-primary);
  color: var(--accent-primary);
  background-color: var(--accent-soft);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.page-btn.active {
  background-color: var(--accent-primary);
  color: #ffffff;
  border-color: var(--accent-primary);
  box-shadow: 0 4px 12px rgba(130, 158, 201, 0.35);
  pointer-events: none;
}

.page-btn:disabled {
  opacity: 0.38;
  cursor: not-allowed;
  transform: none;
}

.page-btn-prev,
.page-btn-next {
  padding: 0 14px;
  font-size: 0.82rem;
  letter-spacing: 0.01em;
}

.page-dots {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 38px;
  color: var(--text-muted);
  font-weight: 700;
  letter-spacing: 0.1em;
  pointer-events: none;
  user-select: none;
}
"""

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(pagination_css)

print('Pagination CSS appended successfully.')
