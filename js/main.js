/* ==========================================================================
   博客交互控制逻辑 - main.js
   功能：日夜主题切换、本地搜索、标签分类过滤、目录高亮、手风琴列表、移动端侧边栏
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initDropdowns();   // 下拉菜单悬浮优化（延迟关闭）
  initMobileMenu();
  initSearchAndFilter();
  initAccordion();
  initScrollSpy();
});

/* ==========================================================================
   0. 导航栏下拉菜单：延迟隐藏，修复"鼠标移入瞬间消失"问题
   ========================================================================== */
function initDropdowns() {
  const navItems = document.querySelectorAll('.nav-item');
  
  navItems.forEach(item => {
    let closeTimer = null;
    
    const showMenu = () => {
      clearTimeout(closeTimer);
      // 先关闭其他已打开的菜单
      navItems.forEach(other => {
        if (other !== item) other.classList.remove('open');
      });
      item.classList.add('open');
    };
    
    const hideMenu = () => {
      closeTimer = setTimeout(() => {
        item.classList.remove('open');
      }, 150); // 150ms 延迟，给鼠标移入菜单的时间
    };
    
    // 鼠标进入导航项 → 显示菜单
    item.addEventListener('mouseenter', showMenu);
    
    // 鼠标离开导航项 → 启动延迟关闭
    item.addEventListener('mouseleave', hideMenu);
    
    // 鼠标进入下拉菜单 → 取消关闭计时器（保持菜单开启）
    const menu = item.querySelector('.dropdown-menu');
    if (menu) {
      menu.addEventListener('mouseenter', () => clearTimeout(closeTimer));
      menu.addEventListener('mouseleave', hideMenu);
    }
    
    // 移动端/点击触发
    const toggle = item.querySelector('.dropdown-toggle');
    if (toggle) {
      toggle.addEventListener('click', e => {
        const href = toggle.getAttribute('href');
        if (!href || href === '#') {
          e.preventDefault();
          const isOpen = item.classList.contains('open');
          // 关闭所有
          navItems.forEach(ni => ni.classList.remove('open'));
          if (!isOpen) item.classList.add('open');
        }
      });
    }

    // 显式保证下拉菜单项点击 100% 顺利跳转
    const dropdownLinks = item.querySelectorAll('.dropdown-item');
    dropdownLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.stopPropagation();
        const targetUrl = link.getAttribute('href');
        if (targetUrl && targetUrl !== '#') {
          window.location.href = targetUrl;
        }
      });
    });
  });
  
  // 点击页面空白处关闭所有下拉菜单
  document.addEventListener('click', e => {
    if (!e.target.closest('.nav-item')) {
      navItems.forEach(ni => ni.classList.remove('open'));
    }
  });
}

/* ==========================================================================
   1. 白天/黑夜模式主题切换
   ========================================================================== */
function initTheme() {
  const themeToggle = document.getElementById('theme-toggle');
  if (!themeToggle) return;

  themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  });
}

/* ==========================================================================
   2. 手机端导航栏控制 (抽屉式滑动)
   ========================================================================== */
function initMobileMenu() {
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');
  
  if (!menuToggle || !navMenu) return;
  
  menuToggle.addEventListener('click', (e) => {
    e.stopPropagation();
    navMenu.classList.toggle('active');
    menuToggle.textContent = navMenu.classList.contains('active') ? '✕' : '☰';
  });
  
  document.addEventListener('click', (e) => {
    if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && e.target !== menuToggle) {
      navMenu.classList.remove('active');
      menuToggle.textContent = '☰';
    }
  });
}

/* ==========================================================================
   3. 全局搜索与分类/标签多维过滤系统 (首页专享)
   ========================================================================== */
let activeCategory = null;
let activeTag = null;
let searchQuery = '';

function initSearchAndFilter() {
  const searchInput = document.getElementById('search-input');
  const navSearchInput = document.getElementById('nav-search-input');
  const filterInfoCard = document.getElementById('filter-info-card');
  const filterLabel = document.getElementById('filter-label');
  const clearFilterBtn = document.getElementById('clear-filter-btn');
  const emptyListIndicator = document.getElementById('empty-list-indicator');
  const articleCards = document.querySelectorAll('.article-card');
  const tagPills = document.querySelectorAll('.tag-pill, .sidebar-tag');
  const accordionItems = document.querySelectorAll('.accordion-item');

  // 如果不是主页（找不到文章卡片），退出过滤逻辑，但保留导航栏搜索跳转
  const isHomePage = articleCards.length > 0;

  function updateDisplay() {
    if (!isHomePage) return;

    let visibleCount = 0;
    
    articleCards.forEach(card => {
      const categories = (card.getAttribute('data-categories') || '').split(',');
      const tags = (card.getAttribute('data-tags') || '').split(',');
      const title = (card.querySelector('.article-card-title')?.textContent || '').toLowerCase();
      const excerpt = (card.querySelector('.article-card-excerpt')?.textContent || '').toLowerCase();
      
      const matchesCategory = !activeCategory || categories.includes(activeCategory);
      const matchesTag = !activeTag || tags.includes(activeTag);
      
      const cleanQuery = searchQuery.trim().toLowerCase();
      const matchesSearch = !cleanQuery || 
                            title.includes(cleanQuery) || 
                            excerpt.includes(cleanQuery) || 
                            tags.some(t => t.toLowerCase().includes(cleanQuery)) ||
                            categories.some(c => c.toLowerCase().includes(cleanQuery));

      if (matchesCategory && matchesTag && matchesSearch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    // 更新过滤状态栏
    if (activeCategory || activeTag || searchQuery) {
      filterInfoCard.style.display = 'flex';
      let labels = [];
      if (activeCategory) {
        // 翻译分类英文为中文显示
        const catMap = { 'science': '科普文章', 'airport': '机场评测', 'clash': 'Clash技术', 'shadowrocket': '小火箭配置', 'cheap': '性价比机场', 'premium': '专线高速', 'eval': '机场排行评测', 'cost': '便宜月付', 'speed': '专线游戏加速', 'app': '流媒体/AI', 'proto': '协议技术科普', 'op': '客户端配置教程' };
        labels.push(`分类: ${catMap[activeCategory] || activeCategory}`);
      }
      if (activeTag) labels.push(`标签: #${activeTag}`);
      if (searchQuery) labels.push(`搜索: "${searchQuery}"`);
      filterLabel.textContent = labels.join(' | ');
    } else {
      filterInfoCard.style.display = 'none';
    }

    // 显示/隐藏空列表提示
    if (visibleCount === 0) {
      emptyListIndicator.style.display = 'flex';
    } else {
      emptyListIndicator.style.display = 'none';
    }
  }

  // 绑定主页大搜索框
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      if (navSearchInput) navSearchInput.value = searchQuery; // 同步两个搜索框
      updateDisplay();
    });
  }

  // 绑定导航栏搜索框
  if (navSearchInput) {
    navSearchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      if (searchInput) searchInput.value = searchQuery; // 同步两个搜索框
      if (isHomePage) {
        updateDisplay();
      }
    });

    // 若在子页面中输入搜索并回车，自动携带参数跳回主页搜索
    navSearchInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter' && !isHomePage) {
        window.location.href = `${window.location.protocol}//${window.location.host}/index.html?search=${encodeURIComponent(navSearchInput.value)}`;
      }
    });
  }

  // 处理标签点击
  tagPills.forEach(pill => {
    pill.addEventListener('click', (e) => {
      if (!isHomePage) {
        // 子页面点击标签直接走默认 HTML 相对路径跳转
        return;
      }
      
      const href = pill.getAttribute('href');
      if (href && (href.includes('articles/') || (href.endsWith('.html') && !href.includes('index.html')))) {
        // 如果标签链接指向具体文章，不拦截跳转
        return;
      }
      
      e.preventDefault();
      
      const clickedTag = pill.getAttribute('data-tag') || pill.textContent.replace('#', '').trim();
      
      if (activeTag === clickedTag) {
        activeTag = null; // 重复点击取消过滤
        pill.classList.remove('active');
      } else {
        tagPills.forEach(t => t.classList.remove('active'));
        activeTag = clickedTag;
        pill.classList.add('active');
      }
      updateDisplay();
    });
  });

  // 处理手风琴里的分类点击
  accordionItems.forEach(item => {
    item.addEventListener('click', (e) => {
      if (!isHomePage) {
        // 子页面点击分类直接走默认 HTML 相对路径跳转
        return;
      }
      
      const href = item.getAttribute('href');
      if (href && (href.includes('articles/') || (href.endsWith('.html') && !href.includes('index.html')))) {
        // 如果分类链接指向具体文章，不拦截跳转
        return;
      }
      
      e.preventDefault();
      const cat = item.getAttribute('data-category');
      
      if (activeCategory === cat) {
        activeCategory = null;
        item.style.backgroundColor = '';
        item.style.color = '';
      } else {
        accordionItems.forEach(ai => {
          ai.style.backgroundColor = '';
          ai.style.color = '';
        });
        activeCategory = cat;
        item.style.backgroundColor = 'var(--accent-soft)';
        item.style.color = 'var(--accent-primary)';
      }
      updateDisplay();
    });
  });

  // 清除过滤按钮
  if (clearFilterBtn) {
    clearFilterBtn.addEventListener('click', (e) => {
      e.preventDefault();
      resetAllFilters();
    });
  }

  function resetAllFilters() {
    activeCategory = null;
    activeTag = null;
    searchQuery = '';
    if (searchInput) searchInput.value = '';
    if (navSearchInput) navSearchInput.value = '';
    tagPills.forEach(t => t.classList.remove('active'));
    accordionItems.forEach(ai => {
      ai.style.backgroundColor = '';
      ai.style.color = '';
    });
    updateDisplay();
  }

  // 挂载全局重置，以便 LOGO 点击时重置过滤
  window.resetFilters = resetAllFilters;

  // 页面加载时解析 URL 参数以继承过滤条件
  const urlParams = new URLSearchParams(window.location.search);
  const paramSearch = urlParams.get('search');
  const paramTag = urlParams.get('tag');
  const paramCategory = urlParams.get('category');

  if (paramSearch) {
    searchQuery = paramSearch;
    if (searchInput) searchInput.value = searchQuery;
    if (navSearchInput) navSearchInput.value = searchQuery;
  }
  if (paramTag) {
    activeTag = paramTag;
    tagPills.forEach(pill => {
      const tagText = pill.getAttribute('data-tag') || pill.textContent.replace('#', '').trim();
      if (tagText === activeTag) pill.classList.add('active');
    });
  }
  if (paramCategory) {
    activeCategory = paramCategory;
    accordionItems.forEach(ai => {
      if (ai.getAttribute('data-category') === activeCategory) {
        ai.style.backgroundColor = 'var(--accent-soft)';
        ai.style.color = 'var(--accent-primary)';
        // 自动展开包含该项的父 accordion
        const parentContent = ai.closest('.accordion-content');
        if (parentContent) {
          parentContent.style.display = 'flex';
          const header = parentContent.previousElementSibling;
          if (header) header.classList.add('active');
        }
      }
    });
  }

  if (paramSearch || paramTag || paramCategory) {
    updateDisplay();
  }
}

// 供热门标签和气泡标签调用的函数
window.performNavSearch = function(kw) {
  const isHomePage = document.querySelectorAll('.article-card').length > 0;
  if (isHomePage) {
    const navSearchInput = document.getElementById('nav-search-input');
    const searchInput = document.getElementById('search-input');
    if (navSearchInput) navSearchInput.value = kw;
    if (searchInput) searchInput.value = kw;
    searchQuery = kw;
    window.resetFilters(); // 先清空分类/标签标签，纯靠文本匹配
    searchQuery = kw;
    if (searchInput) searchInput.value = kw;
    if (navSearchInput) navSearchInput.value = kw;
    // 强制过滤
    const articleCards = document.querySelectorAll('.article-card');
    const emptyListIndicator = document.getElementById('empty-list-indicator');
    const filterInfoCard = document.getElementById('filter-info-card');
    const filterLabel = document.getElementById('filter-label');
    
    let visibleCount = 0;
    articleCards.forEach(card => {
      const title = (card.querySelector('.article-card-title')?.textContent || '').toLowerCase();
      const excerpt = (card.querySelector('.article-card-excerpt')?.textContent || '').toLowerCase();
      if (title.includes(kw.toLowerCase()) || excerpt.includes(kw.toLowerCase())) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });
    filterInfoCard.style.display = 'flex';
    filterLabel.textContent = `搜索: "${kw}"`;
    emptyListIndicator.style.display = visibleCount === 0 ? 'flex' : 'none';
  } else {
    window.location.href = `${window.location.protocol}//${window.location.host}/index.html?search=${encodeURIComponent(kw)}`;
  }
};

/* ==========================================================================
   4. 手风琴菜单控制 (左侧分类导航)
   ========================================================================== */
function initAccordion() {
  const headers = document.querySelectorAll('.accordion-header');
  headers.forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      const isActive = header.classList.contains('active');
      
      // 折叠所有其他项
      headers.forEach(otherHeader => {
        otherHeader.classList.remove('active');
        otherHeader.nextElementSibling.style.display = 'none';
      });
      
      if (!isActive) {
        header.classList.add('active');
        content.style.display = 'flex';
      }
    });
  });
}

/* ==========================================================================
   5. 目录滚动联动追踪高亮 (Table of Contents Scroll Spy)
   ========================================================================== */
function initScrollSpy() {
  const tocLinks = document.querySelectorAll('.toc-link');
  const headings = document.querySelectorAll('.article-body h2, .article-body h3');
  
  if (tocLinks.length === 0 || headings.length === 0) return;
  
  const options = {
    root: null,
    rootMargin: '0px 0px -60% 0px', // 当标题滚动到屏幕中上部时激活
    threshold: 0.1
  };
  
  let activeId = '';
  
  const observer = new IntersectionObserver(entries => {
    // 找出当前在视口内的标题
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        activeId = entry.target.id;
      }
    });
    
    // 如果有活跃标题，则高亮目录中对应的链接
    if (activeId) {
      tocLinks.forEach(link => {
        link.classList.remove('active');
        const href = link.getAttribute('href');
        if (href === `#${activeId}`) {
          link.classList.add('active');
        }
      });
    }
  }, options);
  
  headings.forEach(heading => {
    // 为没有 ID 的标题自动分配拼音/拼字 ID 供锚点跳转
    if (!heading.id) {
      heading.id = 'heading-' + encodeURIComponent(heading.textContent.trim().substring(0, 10));
    }
    observer.observe(heading);
  });
}

/* ==========================================================================
   6. 文章列表分页 (Pagination) — 每页 6 篇，与搜索/过滤系统联动
   ========================================================================== */
const ARTICLES_PER_PAGE = 6;
let currentPage = 1;

function initPagination() {
  const paginationNav = document.getElementById('pagination-nav');
  const articlesFeed = document.querySelector('.articles-feed');
  if (!paginationNav || !articlesFeed) return;

  // 渲染指定页的文章，并更新分页按钮
  function renderPage(page) {
    // 仅统计"当前可见"的文章卡片（尊重过滤器隐藏状态）
    const allCards = Array.from(articlesFeed.querySelectorAll('.article-card'));
    // 先把所有非 display:none 的过滤隐藏的卡片记录下来（即当前过滤结果）
    const visibleCards = allCards.filter(c => c.getAttribute('data-filtered') !== 'hidden');

    const totalPages = Math.max(1, Math.ceil(visibleCards.length / ARTICLES_PER_PAGE));
    page = Math.min(Math.max(1, page), totalPages);
    currentPage = page;

    const startIdx = (page - 1) * ARTICLES_PER_PAGE;
    const endIdx = startIdx + ARTICLES_PER_PAGE;

    // 控制每张卡片的显/隐（分页隐藏不同于过滤隐藏，用 data-paged 标记区分）
    visibleCards.forEach((card, i) => {
      card.style.display = (i >= startIdx && i < endIdx) ? 'flex' : 'none';
    });

    // 隐藏所有过滤隐藏的卡片
    allCards.forEach(card => {
      if (card.getAttribute('data-filtered') === 'hidden') {
        card.style.display = 'none';
      }
    });

    // 更新分页 UI
    renderPaginationBtns(page, totalPages);

    // 翻页后自动滚回文章列表顶部
    const feedTop = articlesFeed.getBoundingClientRect().top + window.scrollY - 80;
    window.scrollTo({ top: feedTop, behavior: 'smooth' });
  }

  // 生成分页按钮 HTML
  function renderPaginationBtns(current, total) {
    if (total <= 1) {
      paginationNav.innerHTML = '';
      return;
    }

    let buttons = '';
    const prevDisabled = current <= 1 ? 'disabled' : '';
    const nextDisabled = current >= total ? 'disabled' : '';

    buttons += `<button class="page-btn page-btn-prev" data-page="${current - 1}" ${prevDisabled} aria-label="上一页">← 上一页</button>`;

    // 页码逻辑：始终显示首尾页，中间用省略号压缩
    const range = buildPageRange(current, total);
    range.forEach(item => {
      if (item === '...') {
        buttons += `<span class="page-dots">···</span>`;
      } else {
        const isActive = item === current ? 'active' : '';
        buttons += `<button class="page-btn ${isActive}" data-page="${item}" aria-label="第${item}页">${item}</button>`;
      }
    });

    buttons += `<button class="page-btn page-btn-next" data-page="${current + 1}" ${nextDisabled} aria-label="下一页">下一页 →</button>`;

    paginationNav.innerHTML = buttons;

    // 绑定点击事件
    paginationNav.querySelectorAll('.page-btn:not(:disabled)').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetPage = parseInt(btn.getAttribute('data-page'), 10);
        if (!isNaN(targetPage)) renderPage(targetPage);
      });
    });
  }

  // 构建页码序列（最多显示 7 个元素）
  function buildPageRange(current, total) {
    if (total <= 7) return Array.from({ length: total }, (_, i) => i + 1);

    const pages = [1];
    if (current > 3) pages.push('...');

    const start = Math.max(2, current - 1);
    const end = Math.min(total - 1, current + 1);
    for (let i = start; i <= end; i++) pages.push(i);

    if (current < total - 2) pages.push('...');
    pages.push(total);
    return pages;
  }

  // 将此模块的 renderPage 暴露出去，供过滤系统调用
  window.__paginationRender = renderPage;

  // 初次渲染
  renderPage(1);
}

// 在 DOM 就绪时初始化（追加到已有的 DOMContentLoaded 初始化链末尾）
document.addEventListener('DOMContentLoaded', () => {
  initPagination();
});

// ——— 集成: 重写 updateDisplay 后重置分页 ———
// 为过滤系统打补丁：过滤结果改变时重置到第1页
(function patchFilterForPagination() {
  // 等 DOM 和 main 初始化完成后再打补丁
  setTimeout(() => {
    const articlesFeed = document.querySelector('.articles-feed');
    if (!articlesFeed) return;

    // 重写全局 resetFilters：同时重置分页
    const origReset = window.resetFilters;
    if (origReset) {
      window.resetFilters = function() {
        origReset();
        // 清除过滤标记后重新渲染分页
        articlesFeed.querySelectorAll('.article-card').forEach(c => {
          c.removeAttribute('data-filtered');
        });
        if (window.__paginationRender) window.__paginationRender(1);
      };
    }

    // MutationObserver 监听卡片 display 变化 → 同步更新分页状态
    const observer = new MutationObserver(() => {
      // 将过滤系统设置为 display:none 的卡片标记为 data-filtered=hidden
      articlesFeed.querySelectorAll('.article-card').forEach(card => {
        if (card.style.display === 'none') {
          card.setAttribute('data-filtered', 'hidden');
        } else {
          card.removeAttribute('data-filtered');
        }
      });
      if (window.__paginationRender) window.__paginationRender(1);
    });

    // 只在用户主动触发搜索/过滤时才响应（防循环）
    const searchInput = document.getElementById('search-input');
    const navSearch = document.getElementById('nav-search-input');
    const clearBtn = document.getElementById('clear-filter-btn');
    const tagPills = document.querySelectorAll('.tag-pill, .sidebar-tag');
    const accordionItems = document.querySelectorAll('.accordion-item');

    const onFilterChange = () => {
      setTimeout(() => {
        if (window.__paginationRender) window.__paginationRender(1);
      }, 30);
    };

    if (searchInput) searchInput.addEventListener('input', onFilterChange);
    if (navSearch) navSearch.addEventListener('input', onFilterChange);
    if (clearBtn) clearBtn.addEventListener('click', onFilterChange);
    tagPills.forEach(p => p.addEventListener('click', onFilterChange));
    accordionItems.forEach(a => a.addEventListener('click', onFilterChange));
  }, 200);
})();

// ==========================================================================
// 轮播图交互逻辑 (Carousel)
// ==========================================================================
function initCarousel() {
  console.log("[Carousel] initCarousel starting...");
  const container = document.querySelector('.carousel-container');
  if (!container) {
    console.log("[Carousel] Container not found, skipping initialization.");
    return;
  }

  const slides = container.querySelectorAll('.carousel-slide');
  const prevBtn = container.querySelector('.carousel-prev');
  const nextBtn = container.querySelector('.carousel-next');
  const dots = container.querySelectorAll('.carousel-dot');
  
  if (slides.length === 0) {
    console.log("[Carousel] No slides found in container!");
    return;
  }

  console.log(`[Carousel] Initialized successfully with ${slides.length} slides.`);

  let currentIndex = 0;
  let autoplayTimer = null;
  const intervalTime = 2500; // 2.5秒自动播放

  function showSlide(index) {
    if (index >= slides.length) index = 0;
    if (index < 0) index = slides.length - 1;

    currentIndex = index;
    console.log(`[Carousel] Active slide index: ${currentIndex}`);

    slides.forEach((slide, i) => {
      if (i === currentIndex) {
        slide.classList.add('active');
      } else {
        slide.classList.remove('active');
      }
    });

    dots.forEach((dot, i) => {
      if (i === currentIndex) {
        dot.classList.add('active');
      } else {
        dot.classList.remove('active');
      }
    });
  }

  function startAutoplay() {
    stopAutoplay();
    console.log("[Carousel] Autoplay timer started.");
    autoplayTimer = setInterval(() => {
      showSlide(currentIndex + 1);
    }, intervalTime);
  }

  function stopAutoplay() {
    if (autoplayTimer) {
      console.log("[Carousel] Autoplay timer stopped.");
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showSlide(currentIndex - 1);
      startAutoplay();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', (e) => {
      e.preventDefault();
      showSlide(currentIndex + 1);
      startAutoplay();
    });
  }

  dots.forEach(dot => {
    dot.addEventListener('click', (e) => {
      e.preventDefault();
      const targetIndex = parseInt(dot.getAttribute('data-index'), 10);
      if (!isNaN(targetIndex)) {
        showSlide(targetIndex);
        startAutoplay();
      }
    });
  });

  // 触摸手势支持
  let touchStartX = 0;
  let touchEndX = 0;
  
  container.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    stopAutoplay();
  }, { passive: true });

  container.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    handleGesture();
    startAutoplay();
  }, { passive: true });

  function handleGesture() {
    if (touchStartX - touchEndX > 50) {
      showSlide(currentIndex + 1);
    } else if (touchEndX - touchStartX > 50) {
      showSlide(currentIndex - 1);
    }
  }

  container.addEventListener('mouseenter', stopAutoplay);
  container.addEventListener('mouseleave', startAutoplay);

  // 初始化
  showSlide(0);
  startAutoplay();
}

document.addEventListener('DOMContentLoaded', initCarousel);
