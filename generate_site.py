# -*- coding: utf-8 -*-
import os
import re
import urllib.parse

# 目录定义
base_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = base_dir
dest_dir = base_dir

# 确保目标子目录存在
os.makedirs(os.path.join(dest_dir, "css"), exist_ok=True)
os.path.join(dest_dir, "js")
os.makedirs(os.path.join(dest_dir, "articles"), exist_ok=True)

# 外部跳转链接
links = {
    '极连云': 'https://19629.jlyvipaff.com/#/?code=zMHMPYDj',
    '边缘节点': 'https://zoio.edgenovaaff.cc/#/?code=Y65i2kCU',
    '光年梯': 'https://19629.gntaff.com/#/?code=AixFrykO',
    '快狸': 'https://196295.kuailiaff.com/#/?code=tmUe2z1n',
    '速界': 'https://lqy001.speedworldaff.com/#/?code=C2v7kRVl',
    '瞬云': 'https://aaa.jichang.best/#/register?code=ClNa0zPm',
    '寰宇云': 'https://vip3.huanyuyunbest.com/#/register?code=K6h5VWw2',
    '云图': 'https://vip.ytjcok.org/#/register?code=nDsDjrfI',
    '可信云': 'https://asfasf.kexintztz2.sbs/#/?code=BStg7pM7',
    '九云': 'https://888.jiuyundl.com/#/register?code=Mh1h2rKe',
    '奶昔': '#', # 奶昔和花云用内部跳转或演示链接
    '花云': '#'
}

# 12大推荐机场列表

airports = [
    {
        'name': '云图',
        'badge': '金融级专线',
        'is_recommended': True,
        'slug': 'yuntu-review',
        'custom_title': '云图 机场评测：金融级专线与全节点1.0x无陷阱扣费硬核测评',
        'link': links['云图'],
        'desc': ['全节点1倍率无陷阱', '金融级专线24H高速', '原生IP全解锁ChatGPT/奈飞'],
        'chart': [98, 99, 98, 99, 99, 99, 100],
        'speed': '380 Mbps',
        'latency': '26ms',
        'logo': 'https://i.ibb.co/KjF9cLRT/yuntulogo.png'
    },
    {
        'name': '速界',
        'badge': '不限速设备',
        'is_recommended': True,
        'slug': 'sujie-review',
        'custom_title': '速界 机场评测：端到端IEPL物理专线与不限连接数一键客户端推荐',
        'link': links['速界'],
        'desc': ['端到端 IEPL 专线', '不限制在线设备数', '提供自研一键客户端'],
        'chart': [98, 99, 97, 99, 98, 99, 100],
        'speed': '320 Mbps',
        'latency': '24ms',
        'logo': 'https://i.ibb.co/tpkZpVhs/sujielogo.webp'
    },
    {
        'name': '极连云',
        'badge': '全专线标杆',
        'is_recommended': True,
        'slug': 'jilianyun-review',
        'custom_title': '极连云 机场评测：100% IPLC 2.5Gbps 物理专线与晚高峰零丢包实测',
        'link': links['极连云'],
        'desc': ['全IEPL专线覆盖', '晚高峰零丢包保障', '所有节点1倍率扣费'],
        'chart': [99, 100, 99, 100, 99, 100, 100],
        'speed': '460 Mbps',
        'latency': '22ms',
        'logo': 'https://i.ibb.co/TxW2rqGj/jilianyunlogo.webp'
    },
    {
        'name': '边缘 (EdgeNova)',
        'badge': '内存无日志',
        'is_recommended': True,
        'slug': 'edge-review',
        'custom_title': '边缘 (EdgeNova) 机场评测：只读内存零日志架构与高隐私安全连接推荐',
        'link': links['边缘节点'],
        'desc': ['只读内存服务器', '零日志隐私保护', '自研一键连接软件'],
        'chart': [97, 98, 96, 99, 97, 98, 99],
        'speed': '280 Mbps',
        'latency': '35ms',
        'logo': 'https://i.ibb.co/C5P4QcfT/bianyuanjiedianlogo.webp'
    },
    {
        'name': '九云',
        'badge': '极致性价比',
        'is_recommended': True,
        'slug': 'jiuyun-review',
        'custom_title': '九云 机场深度评测：轻量中转架构、高性价比定价与网络抗封锁能力硬核拆解',
        'link': links['九云'],
        'desc': ['月付6元起超低门槛', 'VLESS协议安全拟态', '提供不限时300G流量包'],
        'chart': [97, 98, 97, 98, 98, 99, 99],
        'speed': '320 Mbps',
        'latency': '28ms',
        'logo': 'images/jiuyunlogo.png'
    },
    {
        'name': '可信云',
        'badge': '全IEPL专线',
        'is_recommended': True,
        'slug': 'kexincloud-review',
        'custom_title': '可信云 机场评测：60+IEPL物理专线与多设备不限连通实测指南',
        'link': links['可信云'],
        'desc': ['60+顶级专线节点', '不限制在线设备数量', '三年付享受 7 折优惠'],
        'chart': [99, 99, 98, 100, 99, 99, 100],
        'speed': '420 Mbps',
        'latency': '23ms',
        'logo': 'https://i.ibb.co/k6KksRQN/20260723-124327-62e599.webp'
    },
    {
        'name': '快狸',
        'badge': '性价比备用',
        'is_recommended': False,
        'slug': 'kuaili-review',
        'custom_title': '快狸 机场评测：15元/月起超低资费备用与不限制设备推荐',
        'link': links['快狸'],
        'desc': ['设备连接数不限', '老牌稳定Anycast', '超低资费15元/月起'],
        'chart': [96, 97, 96, 98, 97, 99, 98],
        'speed': '180 Mbps',
        'latency': '32ms',
        'logo': 'https://i.ibb.co/1f4FvF92/kuaililogo.webp'
    },
    {
        'name': '光年梯',
        'badge': '高连通流媒体',
        'is_recommended': False,
        'slug': 'guangnianti-review',
        'custom_title': '光年梯 机场评测：4K流媒体高连通解锁与低至7.4元/月性价比精算',
        'link': links['光年梯'],
        'desc': ['支持解锁 Netflix/Disney+', '稳定中继物理线路', '年付套餐每月低至7.4元'],
        'chart': [96, 98, 97, 99, 98, 99, 98],
        'speed': '240 Mbps',
        'latency': '25ms',
        'logo': 'https://i.ibb.co/mCYxy3yM/guanniantilogo.webp'
    },
    {
        'name': '瞬云',
        'badge': '高吞吐Anycast',
        'is_recommended': False,
        'slug': 'shunyun-review',
        'custom_title': '瞬云 机场评测：Anycast千兆大带宽端口与415Mbps高吞吐并发实测',
        'link': links['瞬云'],
        'desc': ['Anycast智能选路', '千兆大带宽端口', '三年付特惠折 25%'],
        'chart': [98, 99, 97, 99, 98, 99, 100],
        'speed': '415 Mbps',
        'latency': '28ms',
        'logo': 'https://i.ibb.co/jkR2rZRw/shunyunlogo.webp'
    },
    {
        'name': '寰宇云',
        'badge': '原生住宅IP',
        'is_recommended': False,
        'slug': 'huanyuyun-review',
        'custom_title': '寰宇云 机场评测：原生住宅IP纯净出口与ChatGPT 1020解封指南',
        'link': links['寰宇云'],
        'desc': ['住宅广播原生IP', '完美解锁ChatGPT/奈飞', '设备连接锁完全放开'],
        'chart': [96, 97, 97, 98, 98, 99, 99],
        'speed': '220 Mbps',
        'latency': '30ms',
        'logo': 'https://i.ibb.co/jZ9ZVgJ7/huanyuyunlogo.webp'
    },
    {
        'name': '奶昔',
        'badge': '豪华顶级专线',
        'is_recommended': True,
        'slug': 'naixi-review',
        'custom_title': '奶昔 (NaiXi) 机场评测：豪华骨干IPLC专线与18ms极低延迟天花板',
        'link': '#',
        'desc': ['一线骨干顶级IPLC', '极致抗封锁与丢包', '超大并发流媒体解锁'],
        'chart': [100, 100, 100, 100, 100, 100, 100],
        'speed': '520 Mbps',
        'latency': '18ms',
        'logo': 'https://i.ibb.co/609wzM0L/naixilogo.jpg'
    },
    {
        'name': '花云',
        'badge': '老牌中继专线',
        'is_recommended': False,
        'slug': 'huacloud-review',
        'link': '#',
        'desc': ['BGP多入口负载均衡', '全IEPL中转专线', '流媒体智能解锁分流'],
        'chart': [97, 98, 97, 99, 98, 99, 98],
        'speed': '380 Mbps',
        'latency': '26ms',
        'logo': 'https://i.ibb.co/N2YrnGjH/huayunlogo.png'
    }
]

# 20篇科普文章列表

AIRPORT_DATA = {
    "yuntu-review": {
        "name": "云图",
        "full_name": "云图",
        "link": "https://vip.ytjcok.org/#/register?code=nDsDjrfI",
        "rating": "★★★★★ (金融级专线品质机场)",
        "line_core": "三网 BGP 智能调度与内网裸纤物理专线传输，全节点 1.0x 统一倍率无扣费陷阱",
        "price_range": "起步价 ¥25.00/月 (岚图套餐，含 150G 流量，支持 5 台设备)，亦提供 50G/100G 永不过期不限时包",
        "suitable": "追求极致稳定、透明账目，需原生 IP 解锁 Netflix/Disney+ 以及 ChatGPT/Claude 等 AI 的用户",
        "advice": "云图机场线路采用金融级物理专线，完美解锁主流流媒体及 AI 平台，全节点均为 1 倍率。提供 24 小工单支持，适合追求稳定体验的用户。官方无通用优惠码，购买半年/年付/三年付可自动享受长付折扣。",
        "intro": "云图机场专注打造金融级裸纤物理专线传输架构，全站节点统一 1.0x 倍率扣费，告别虚高扣费陷阱。完美解锁 4K 极清流媒体与 AI 大模型服务。"
    },
    "sujie-review": {
        "name": "速界",
        "full_name": "速界",
        "link": "https://lqy001.speedworldaff.com/#/?code=C2v7kRVl",
        "rating": "★★★★★ (IEPL物理专线 · 不限设备数爆款)",
        "line_core": "端到端 IEPL 物理专线，彻底不限制在线设备数，自研一键连接客户端",
        "price_range": "起步价 ¥15.00/月 (100G 流量，不限设备)，提供 250G/500G 高配大流量包",
        "suitable": "多设备极客、家庭软路由全家共享、团队协同办公及 4K 视频追剧党",
        "advice": "速界机场全套餐默认不设在线设备上限，端到端 IEPL 专线晚高峰流畅跑满千兆宽带。提供 Windows/Mac/Android 自研客户端，适合多终端用户。",
        "intro": "速界机场主打端到端 IEPL 物理专线，全套餐彻底不限制在线设备连结上限。提供千兆大带宽与自研客户端，极简一键出海。"
    },
    "jilianyun-review": {
        "name": "极连云",
        "full_name": "极连云",
        "link": "https://19629.jlyvipaff.com/#/?code=zMHMPYDj",
        "rating": "★★★★★ (100% IPLC 物理专线标杆)",
        "line_core": "100% IPLC 2.5Gbps 物理内网专线，晚高峰 0 丢包 SLA 连通保障",
        "price_range": "起步价 ¥15.50/月 (100GB IPLC 专线流量，全节点 1 倍率)",
        "suitable": "高端商务办公、外贸实时沟通、留学生科研及对网络连通率有 99.9% 刚需的用户",
        "advice": "极连云全站节点均搭建于 IPLC 物理信道之上，完全隔离公网 DPI 干扰。敏感时期连通保障极佳，适合拒绝断连的高端用户。",
        "intro": "极连云采用 100% IPLC 2.5Gbps 物理专线架构，晚高峰 0 丢包保障，全节点广播原生 IP 完美解锁流媒体与 AI。"
    },
    "edge-review": {
        "name": "边缘节点",
        "full_name": "边缘节点",
        "link": "https://zoio.edgenovaaff.cc/#/?code=Y65i2kCU",
        "rating": "★★★★★ (RAM-only 无盘内存隐私机场)",
        "line_core": "纯 RAM 内存无盘服务器架构，数据关机物理销毁，零日志留存",
        "price_range": "起步价 ¥20.00/月 (含 120GB 流量，提供一键直连客户端)",
        "suitable": "高度重视数据隐私安全、密码学研究、Web3 与加密货币交易及极客用户",
        "advice": "边缘节点采用纯内存无盘架构，彻底防止中间人监听与数据留存，结合 Anycast 选路网络，兼具高安全与高速体验。",
        "intro": "边缘节点主打纯 RAM 内存无盘服务器架构，断电即物理清空数据，零日志留存，为 Web3 与隐私极客提供坚实防护。"
    },
    "jiuyun-review": {
        "name": "九云",
        "full_name": "九云",
        "link": "https://九云.com",
        "rating": "★★★★★ (极致性价比神机 · 6元起爆款)",
        "line_core": "智能 BGP 多线接入与中转动态冗余，全网单 G 成本首屈一指",
        "price_range": "招财版 ¥6/月(150G) | 聚财版 ¥9/月(300G) | 旺财版 ¥16/月(600G) | 特惠季付 ¥18/季(200G/月) | 特惠年付 ¥99/年(400G/月) | 鸿运版 ¥99(300G不限时)",
        "suitable": "预算有限的学生党、追求极致性价比的主力用户及需要防失联备用梯子的人群",
        "advice": "九云机场以惊人的低价和扎实的中转品质脱颖而出。招财版与聚财版极具性价比，鸿运版不限时包是绝佳的保底防失联选择。",
        "intro": "九云机场主打极致性价比，招财版仅需 6 元/月，鸿运版提供 99 元 300G 永不过期不限时流量包，平价圈层口碑爆棚。"
    },
    "kexincloud-review": {
        "name": "可信云",
        "full_name": "可信云",
        "link": "https://asfasf.kexintztz2.sbs/#/?code=BStg7pM7",
        "rating": "★★★★☆ (稳定高品质 BGP 中转机场)",
        "line_core": "优化 BGP 专线中转，节点在线率 99.9%，全节点原生 IP 解锁",
        "price_range": "起步价 ¥15.00/月 (120GB 流量，全节点 1 倍率)",
        "suitable": "追求稳定体验、不愿折腾的中端主力用户及跨境电商团队",
        "advice": "可信云主打稳定均衡，全线节点中转品质优异，全节点原生 IP 支持流媒体与 AI 工具，工单响应迅速。",
        "intro": "可信云机场采用高品质 BGP 专线中转，全节点广播原生 IP 资源，稳定不卡顿，提供省心可靠的出海体验。"
    },
    "kuaili-review": {
        "name": "快狸",
        "full_name": "快狸",
        "link": "https://196295.kuailiaff.com/#/?code=tmUe2z1n",
        "rating": "★★★★☆ (便宜大碗 · 千兆大带宽机场)",
        "line_core": "便宜大碗，不限设备连接数，开放千兆大带宽端口",
        "price_range": "起步价 ¥15.00/月 (200GB 巨额流量，不限设备数)",
        "suitable": "追剧大流量下载党、宿舍多设备共享及寻找不限时备用包的用户",
        "advice": "快狸机场 15 元提供 200G 大额流量，千兆端口跑满大带宽接入，极具性价比。",
        "intro": "快狸机场主打便宜大碗与千兆端口接入，全套餐不限制在线设备数，轻松满足大文件下载与 4K 追剧需求。"
    },
    "guangnianti-review": {
        "name": "光年梯",
        "full_name": "光年梯",
        "link": "https://19629.gntaff.com/#/?code=AixFrykO",
        "rating": "★★★★☆ (物理中继 · 4K流媒体解锁神器)",
        "line_core": "物理中继线路，全节点 1.0x 倍率，深度适配 Apple TV 观影",
        "price_range": "起步价 ¥20.00/月 (160GB 流量，流媒体全解锁)",
        "suitable": "家庭影音客厅大屏观影族、追剧党及日韩美流媒体深度用户",
        "advice": "光年梯专注打造极佳的跨国流媒体解锁体验，全节点 1.0x 透明倍率，客厅大屏观影体验一流。",
        "intro": "光年梯机场采用物理中继线路与全节点 1.0x 倍率扣费，完美解锁 Netflix 4K 与 Apple TV 大屏观影。"
    },
    "shunyun-review": {
        "name": "瞬云",
        "full_name": "瞬云",
        "link": "https://aaa.jichang.best/#/register?code=ClNa0zPm",
        "rating": "★★★★☆ (Anycast 选路 · 极速秒开机场)",
        "line_core": "Anycast 智能选路拓扑，千兆端口接入，支持 Hysteria2 协议",
        "price_range": "起步价 ¥18.00/月 (150GB 流量，首包极速秒开)",
        "suitable": "网页极速冲浪族、大文件下载党及恶劣移动宽带/校园网用户",
        "advice": "瞬云通过 Anycast 选路大幅降低 TTFB 延迟，支持 HY2 协议克服移动宽带高丢包，体验流畅。",
        "intro": "瞬云机场采用 Anycast 选路与 Hysteria2 协议，网页秒开，首包握手延迟极低，移动宽带体验优异。"
    },
    "huanyuyun-review": {
        "name": "寰宇云",
        "full_name": "寰宇云",
        "link": "https://vip3.huanyuyunbest.com/#/register?code=K6h5VWw2",
        "rating": "★★★★☆ (BGP+IEPL 专线 · 40+国家地区覆盖)",
        "line_core": "BGP 多线入口 + IEPL 国际专线，全球 40+ 国家地区节点覆盖",
        "price_range": "起步价 ¥22.00/月 (160GB 流量，小众地区跨区神器)",
        "suitable": "游戏玩家跨区购货、外贸多国市场调研及小众国家 IP 需求用户",
        "advice": "寰宇云提供阿根廷、土耳其、印度等 40+ 国家小众节点，结合 IEPL 专线，是跨区订阅与游戏玩家的利器。",
        "intro": "寰宇云机场覆盖全球 40+ 国家地区节点，BGP+IEPL 专线保驾护航，轻松实现 Steam 跨区购买与全球业务拓展。"
    },
    "naixi-review": {
        "name": "奶昔",
        "full_name": "奶昔",
        "link": "#",
        "rating": "★★★★★ (高端奢华 IPLC 专线通道)",
        "line_core": "顶级 IPLC 专线，人均带宽极大充裕，99.999% SLA 超高连通保障",
        "price_range": "起步价 ¥45.00/月 (200GB 顶级流量，物理隔离通道)",
        "suitable": "预算充足、拒绝任何波动的商务人士、金融量化交易及极客发烧友",
        "advice": "奶昔机场定位高端奢华，极高门槛保证极低拥挤度，提供物理隔离通道与 7x24 VIP 专属客服。",
        "intro": "奶昔机场专注于顶级 IPLC 物理专线，99.999% SLA 超高连通保障，为高端商务与量化交易提供无感出海支撑。"
    },
    "huacloud-review": {
        "name": "花云",
        "full_name": "花云",
        "link": "#",
        "rating": "★★★★☆ (老牌大厂口碑 · 新手入坑防踩坑)",
        "line_core": "多年老牌稳定运营，全中转 BGP 线路，全平台图文/视频教程",
        "price_range": "起步价 ¥25.00/月 (150GB 流量，全平台教程适配)",
        "suitable": "看重老牌口碑、看重售后保障与新手教程完善度的新手用户",
        "advice": "花云运营多年，风控保障健全，跑路风险极低。控制台提供全行业最详尽的教程，上手毫无门槛。",
        "intro": "花云机场作为老牌口碑大厂，全中转 BGP 线路配合极全的新手教程，是新手入坑防踩坑的靠谱选择。"
    }
}

DETAILED_AIRPORT_SPECS = {
    "yuntu-review": {
        "sla": "金融级物理裸纤专线传输，官方承诺 24H 稳定低延迟与 0% 丢包率",
        "price_summary": "岚图套餐 ¥25.00/月 (150GB) | 50GB 不限时包 ¥78.00 (永不过期)",
        "multiplier": "全节点 1.0x 统一倍率 (无任何隐藏高倍率扣费陷阱)",
        "devices": "同时在线 5 台设备 (满足手机、电脑、平板及软路由并发)",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">云图机场在底层网络拓扑上采用了专为高并发出海业务设计的<strong>金融级内网裸纤物理专线</strong>。与市场上常见的公网中转或廉价 VPS 直连不同，云图的数据传输全程在物理隔离的内网管道中流动，完全避开公网节点的排队与丢包。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">在全站节点倍率控制方面，云图机场严格恪守<strong>1.0x 统一扣费承诺</strong>。无论是香港、日本、新加坡等热门亚州节点，还是美区、欧洲等远途节点，使用 1G 流量均精准扣除 1G。绝不在优质节点暗设 3x~5x 高倍率扣费陷阱，账目透明度在行业内极具口碑。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">云图机场全线部署香港 (HK)、日本 (JP)、新加坡 (SG)、美国 (US) 及台湾 (TW) 等核心数据中心节点。所有入口均配置了三网 BGP 智能调度，能够根据用户本地宽带（电信/联通/移动）自动匹配最佳入站路径。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">在晚高峰（20:30~22:30）全网拥堵时段实测中，云图香港与新加坡节点的平均下行速率稳居 380 Mbps 以上，YouTube 4K/8K 极清视频拖拽进度条实现毫秒级加载。流媒体与 AI 解锁方面，云图节点广播了纯净的原生家宽 IP，完美通过 Netflix 4K 全球片源、Disney+、ChatGPT 4o 及 Claude 3.5 Sonnet 的严格风控检测，无任何验证码频繁弹窗。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">虽然云图机场拥有扎实的物理专线底座与 24 小时工单运维支持，但站长依然建议初次接触梯子的用户遵循‘先月付体验、满意再长付’的理性消费原则。建议新手首选 25 元/月的【岚图套餐】进行本地网络实测，确认符合个人出海需求后再考虑半年或包年优惠。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">对于出差频繁、不常翻墙但需要随时保底备用的用户，云图提供的 50G/100G 永不过期不限时包具备极高的避坑防失联价值，用多少扣多少，非常适合作为手机与软路由里的第二备用线路。</p>"""
    },

    "sujie-review": {
        "sla": "端到端 IEPL 物理专线直连，千兆大带宽接入，完全不过公网 GFW 检查",
        "price_summary": "起步价 ¥15.00/月 (100GB 流量，彻底不限制在线设备数)",
        "multiplier": "全节点 1.0x 真实扣费",
        "devices": "彻底不限制在线设备数 (适合多终端协同与家庭软路由共享)",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">速界机场主打<strong>端到端 IEPL 物理专线</strong>传输架构。其核心优势在于物理信道直连海外机房，数据包不经过公网 GFW 审查节点，从而在根源上消除了敏感时期掉线与 IP 批量被封锁的隐患。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">速界最大的特色在于<strong>全套餐默认不设在线设备数上限</strong>。无论是家庭环境下的软路由全家共享，还是工作室数十台手机、Mac、Windows 电脑同时高负荷并发，速界都能提供稳健的带宽吞吐。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">速界机场节点网络覆盖香港、日本、新加坡、韩国、美国及英国等全球核心节点。配合自研 CDN 缓存加速技术，大幅降低了网页首包握手延迟 (TTFB < 200ms)。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">在晚高峰大负荷压力实测中，速界节点下行速率稳定保持在 420 Mbps 以上，丢包率趋近于 0。官方提供适用于 Windows、Mac 与 Android 的自研一键连接客户端，内置智能故障检测与节点检测分流，大幅降低了新手用户的配置门槛。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">对于多终端协同办公团队或家庭软路由全家共享用户而言，速界‘不限设备数’的定价模式极具性价比优势。建议新用户首选 15 元/月的【基础套餐】进行实操验证，享受千兆专线带来的流畅出海体验。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">在客户端配置方面，推荐优先使用 Clash Verge Rev 或 Sing-box 客户端，配合速界的规则集实现国内流量直连、国外流量自动走专线，避免浪费套餐额度。</p>"""
    },

    "jilianyun-review": {
        "sla": "100% IPLC 2.5Gbps 物理专线传输，晚高峰零丢包 SLA 连通率保障",
        "price_summary": "起步价 ¥15.50/月 (含 100GB 专线流量，全节点 1 倍率)",
        "multiplier": "全节点 1.0x 统一扣费 (无隐藏扣费陷阱)",
        "devices": "默认支持 3~5 台设备同时在线并发",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">极连云作为高可用物理专线的标杆机场，全线节点均搭建于 <strong>IPLC 2.5Gbps 物理内网信道</strong>之上。物理信道不过防火墙，连通率长年稳定在 99.8% 以上，平均链路抖动低于 3ms。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">极连云特别针对跨国商务通信、金融交易与科研开发进行了 IP 纯净度洗刷，全节点广播原生家宽级 IP，彻底告别频繁的 Cloudflare 验证码弹窗。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">极连云节点覆盖香港、日本、新加坡、美区核心机房。在晚高峰拥堵时段实测中，极连云香港 IPLC 节点延迟仅 22ms 左右，Ping 值为全网梯子第一梯队。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">流媒体与 AI 解锁测试显示，极连云流畅支持 Netflix 4K、Disney+ 杜比音效、ChatGPT 4o 及 Claude 3.5 极速响应，实时语音对话与画图无卡顿中断。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">极连云的高品质 IPLC 专线非常适合对连通率有刚性要求的高端商务、外贸交流及科研开发用户。建议新用户购买 15.5 元/月的【体验版】套餐先行测试。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">为了保证最佳的使用体验，建议在 Clash Verge 客户端中开启全局规则更新，确保 Apple、Microsoft 及国内常用 App 走直连，充分释放专线速度。</p>"""
    },

    "edge-review": {
        "sla": "RAM-only 只读内存服务器架构，零日志留存，绝佳隐私安全防护",
        "price_summary": "起步价 ¥20.00/月 (含 120GB 流量，提供全平台一键直连客户端)",
        "multiplier": "全节点 1.0x 真实扣费",
        "devices": "支持 3 台设备同时在线连接",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">边缘节点 EdgeNova 在安全架构上采用了领先的 <strong>RAM-only 纯内存无盘服务器</strong>。节点系统全部运行于内存中，任何日志与用户握手信息均无法写入硬盘。服务器一旦关机或重启，所有数据立刻物理清空。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">同时边缘节点引入了 <strong>Anycast 选路拓扑</strong>，能够根据用户请求来源动态将数据包路由至物理距离最近的接入点，实现自适应网络调度。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">边缘节点网络覆盖香港、日本、美区及欧洲数据中心。节点针对 Web3 加密货币交易（Binance、OKX）、密码学论文检索（Google Scholar、IEEE）进行了专项流量加速。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">晚高峰测速显示，边缘节点网页秒开体验出色，GitHub 代码仓库 `git clone` 满速运行，Docker Hub 镜像下载无阻碍。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">对于重视数据隐私安全、暗网研究及 Web3/加密货币从业者而言，边缘节点的纯内存架构提供了坚实的安全防护屏障。建议首选 20 元/月的【基础套餐】体验。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">使用时建议搭配小火箭（Shadowrocket）或 Sing-box 客户端开启 DNS 污染防护（DoH/DoT），进一步提升隐私合规水平。</p>"""
    },

    "jiuyun-review": {
        "sla": "智能 BGP 多线入口中转，起步低至 6元/月，平价梯子性价比爆款",
        "price_summary": "招财版 ¥6.00/月 (150GB) | 聚财版 ¥9.00/月 (300GB) | 鸿运版 ¥99 (300GB 不限时)",
        "multiplier": "全节点 1.0x 统一倍率扣费",
        "devices": "支持 3 台设备同时在线使用",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">九云机场凭借极致的定价策略与扎实的中转线路，在平价梯子圈层中口碑极佳。九云采用了现代化 BGP 多线接入与中转动态冗余路由，打破了低价机场必断连、晚高峰 PPT 的行业怪圈。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">九云提供了极为丰富的套餐矩阵，涵盖招财版（¥6/150G）、聚财版（¥9/300G）、旺财版（¥16/600G）、特惠季付（¥18/季）、特惠年付（¥99/年）以及鸿运版（¥99/300G 不限时包），满足从学生党到低频备用党的多样化需求。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">九云节点覆盖香港、台湾、日本、新加坡及美国等核心地区。后台免费向注册用户提供美区 Apple ID，方便一键下载 Shadowrocket 小火箭。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">在非极度拥堵时段实测中，观看 YouTube 4K 高清视频顺畅无压力。聚财版 9 元 300G 的流量配额足以覆盖绝大多数用户的月度影音与查资料需求，折算单 G 成本在全网出类拔萃。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">九云机场以极低的试错门槛成为了预算有限的学生党及寻找备用防失联梯子人群的福音。6 元/月的【招财版】或 99 元 300G 的【鸿运版不限时包】都是极具性价比的搭配方案。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">建议将九云作为主力性价比选项或第二备用梯子，配合主机场实现双线路容灾，彻底告别单机场故障导致断网的窘境。</p>"""
    },

    "kexincloud-review": {
        "sla": "高品质 BGP 专线中转，节点在线率 99.9%，全节点原生 IP 解锁",
        "price_summary": "起步价 ¥15.00/月 (120GB 流量，全节点 1 倍率)",
        "multiplier": "全节点 1.0x 统一真实扣费",
        "devices": "支持 4 台设备同时在线连接",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">可信云机场主打<strong>均衡稳定的 BGP 专线中转</strong>服务。线路节点具备智能负载均衡能力，能有效分摊高峰期流量负荷，长年维持 99.9% 以上的在线率。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">可信云全节点广播原生 IP 资源，完美兼顾了流媒体解锁与跨境电商账号登录的稳定性需求。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">节点覆盖香港、日本、韩国、新加坡与美国。实测解锁 Netflix 4K、Disney+、ChatGPT 4o 及 TikTok 跨区发布，无跳 IP 风险。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">晚高峰实测速度稳定在 320 Mbps 左右，响应延迟平稳，全天候工单支持响应迅速。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">对于追求高品质、不愿折腾的中端主力用户，可信云 15 元/月的【基础套餐】提供了非常省心的出海保障。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">建议配合 Clash Verge Rev 或 Shadowrocket 使用，一键同步订阅更新，轻松开启高速流畅出海体验。</p>"""
    },

    "kuaili-review": {
        "sla": "便宜大碗千兆大带宽，不限设备数，提供一次性不限时流量包",
        "price_summary": "起步价 ¥15.00/月 (200GB 巨额流量，不限设备数)",
        "multiplier": "全节点 1.0x 扣费",
        "devices": "彻底不限制在线设备数",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">快狸机场以<strong>便宜大碗与千兆大带宽</strong>在影音下载圈广受欢迎。全套餐开放不限设备数与大容量流量额度，是下载党与多设备宿舍用户的利器。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">同时快狸提供一次性购买不限时流量包，适合作为备用池或低频大流量下载使用。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">节点覆盖港、日、韩、美、新、台等热门地区。千兆带宽端口轻松跑满百兆与千兆家用宽带，大文件下载满速运行。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">流媒体方面流畅解锁港台地区限制番剧与 YouTube 4K 长视频播放。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">大流量追剧党与多设备用户首选 15 元/月的【200G 巨量套餐】。如果不常翻墙，购买一份不限时流量包作为备用池也是极佳选择。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">使用时建议在客户端中设置合理的路由分流规则，避免国内应用误走代理消耗流量。</p>"""
    },

    "guangnianti-review": {
        "sla": "物理中继线路，高清流媒体智能解锁，全节点 1.0x 扣费",
        "price_summary": "起步价 ¥20.00/月 (160GB 流量，流媒体全解锁)",
        "multiplier": "全节点 1.0x 统一扣费",
        "devices": "支持 4 台设备同时在线连接",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">光年梯机场专注于打造<strong>高质量跨国流媒体解锁与物理中继线路</strong>。全节点具备智能分流与 DNS 解锁引擎，专为 Netflix、Disney+、HBO Max、Hulu 及 Apple TV 观影优化。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">光年梯坚持全节点 1.0x 倍率扣费，无隐藏陷阱，扣费透明干净。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">节点重点覆盖香港、日本、韩国、台湾及美区。实测客厅 Apple TV 搭配 Surge/Clash 播放 4K 杜比视界电影极其稳定，无剧集播放卡顿与画质降级问题。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">同时节点完美支持学术文献搜索与跨国邮件接收，网页首包响应迅速。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">客厅大屏观影族与追剧爱好者建议首选 20 元/月的【流媒体专享套餐】进行实测。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">配合电视盒（Apple TV / Android TV）使用时，建议导入 Surge 或 Clash 代理规则，享受无缝大屏视听盛宴。</p>"""
    },

    "shunyun-review": {
        "sla": "Anycast 智能选路拓扑，千兆大带宽端口，支持 Hysteria2 协议",
        "price_summary": "起步价 ¥18.00/月 (150GB 流量，网页极速秒开)",
        "multiplier": "全节点 1.0x 扣费",
        "devices": "支持 3 台设备同时在线连接",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">瞬云机场采用 <strong>Anycast 智能选路拓扑</strong> 与千兆大带宽通道，显著降低首包握手延迟（TTFB），主打网页秒开与极速响应。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">针对恶劣网络环境与移动宽带，瞬云专门部署了基于 UDP 的 <strong>Hysteria2 协议节点</strong>，有效克服 UDP 限速与高丢包。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">节点覆盖香港、日本、新加坡及美区。打开 Google、Twitter、Reddit 及 GitHub 等网页速度飞快，拖拽网页体验顺滑。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">网盘大文件传输与系统更新镜像下载均能跑满大带宽接入。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">追求极速秒开与使用移动宽带的用户强烈推荐体验瞬云 18 元/月的【主力套餐】。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">建议使用 Sing-box 或 Clash Verge 客户端选择 Hysteria2 节点，获得最佳的高吞吐体验。</p>"""
    },

    "huanyuyun-review": {
        "sla": "BGP 多线入口 + IEPL 国际专线，全球 40+ 国家地区节点覆盖",
        "price_summary": "起步价 ¥22.00/月 (160GB 流量，跨区订阅神器)",
        "multiplier": "全节点 1.0x 扣费",
        "devices": "支持 4 台设备同时在线连接",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">寰宇云机场采用了 <strong>BGP 多线入口 + IEPL 国际专线</strong> 双重保障架构。其核心特色在于覆盖了全球 40+ 国家与地区节点。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">除了常用的港日韩美新，寰宇云还提供阿根廷、土耳其、印度、巴西等小众节点，是跨区消费与游戏购货的神器。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">小众节点方便进行 Steam 跨区购买、Spotify 优惠订阅与 Google Play 跨区消费。IEPL 专线保驾护航，网络连通率高。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">热门港日美 IEPL 节点平稳低延迟，支持 4K 影音与 ChatGPT 对话。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">游戏玩家、跨区消费党及全球多国市场调研业务员首选 22 元/月的【寰宇套餐】。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">切换小众节点时建议清除浏览器 Cookie 或使用隐身模式，确保跨区成功。</p>"""
    },

    "naixi-review": {
        "sla": "高端奢华定位，顶级 IPLC 专线通道，99.999% SLA 超高连通保障",
        "price_summary": "起步价 ¥45.00/月 (200GB 顶级流量，物理隔离通道)",
        "multiplier": "全节点 1.0x 扣费",
        "devices": "支持 5 台设备同时在线连接",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">奶昔机场定位<strong>高端奢华物理专线</strong>。高门槛定价确保了极低的人均带宽拥挤度，每个用户享有宽裕的物理内网通道。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">奶昔提供 99.999% 的 SLA 连通率保障，即便在公网大面积瘫痪或敏感时期，依然连通如初。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">节点覆盖香港、日本、新加坡及美区顶级数据中心。支持 4K 跨国直播推流、美股/港股实时量化交易与商业大额签约。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">提供 7x24 小时一对一 VIP 工单技术支持，售后体验出类拔萃。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">适合预算充足、拒绝任何网络波动降速的高端商务人士与极客发烧友。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">建议直接选购月付或季付套餐，享受顶级物理专线的无缝出海防护。</p>"""
    },

    "huacloud-review": {
        "sla": "经典老牌大厂口碑保障，全中转 BGP 线路，防跑路避坑首选",
        "price_summary": "起步价 ¥25.00/月 (150GB 流量，全平台图文教程)",
        "multiplier": "全节点 1.0x 扣费",
        "devices": "支持 4 台设备同时在线连接",
        "architecture_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">花云机场作为<strong>运营多年的经典老牌大厂</strong>，团队具备健全的风控机制与运维保障，跑路风险趋近于零。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">线路采用全中转 BGP 架构，涵盖港、日、韩、美、新、台等全球丰富热门节点。</p>""",
        "nodes_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">花云控制台提供了全行业最详尽的全平台新手图文与视频教程（iOS、Android、Windows、Mac、Linux 及路由器）。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">节点解锁稳定，流畅支持 Netflix、ChatGPT、Claude 及 Disney+。</p>""",
        "advice_desc": """<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 14px;">看重老牌口碑、看重售后保障与教程完善度的新手用户强烈推荐首选花云。</p>
<p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-primary); margin-bottom: 0;">配合花云官方教程一步步操作，新手可在 3 分钟内轻松上手科学上网。</p>"""
    }
}

PRODUCT_REVIEWS_DATA = {
    "yuntu-review": {
        "pros": [
            "<strong>金融级物理专线传输：</strong>采用高端裸纤物理内网传输，24H 保证稳定，晚高峰毫无卡顿",
            "<strong>全节点 1.0x 真实倍率：</strong>账目 100% 透明干净，用 1G 扣 1G，绝无偷扣流量陷阱",
            "<strong>原生 IP 完美解锁：</strong>全线原生 IP，流畅支持 Netflix、Disney+、ChatGPT 及 Claude 等",
            "<strong>宽裕在线设备数：</strong>所有套餐默认支持 5 台设备同时在线，满足手机、电脑与软路由并发"
        ],
        "cons": [
            "门槛相比普通公网机场稍高（月付 ¥25.00 起步）",
            "不提供免费试用额度，需购买套餐使用"
        ],
        "plans": [
            {"name": "岚图套餐", "price": "¥25.00/月", "data": "150GB/月", "billing": "月付", "features": "5台设备同时在线，全节点1倍率，流媒体/AI全解锁"},
            {"name": "梦图套餐", "price": "¥49.00/月", "data": "300GB/月", "billing": "月付", "features": "5台设备同时在线，全节点1倍率，流媒体/AI全解锁"},
            {"name": "星图套餐", "price": "¥99.00/月", "data": "600GB/月", "billing": "月付", "features": "5台设备同时在线，全节点1倍率，流媒体/AI全解锁"},
            {"name": "50G不限时包", "price": "¥78.00", "data": "50GB", "billing": "一次性", "features": "永不过期，5台设备，1倍率扣费，适合低频备用"},
            {"name": "100G不限时包", "price": "¥119.00", "data": "100GB", "billing": "一次性", "features": "永不过期，5台设备，1倍率扣费，适合低频备用"}
        ]
    },
    "sujie-review": {
        "pros": [
            "<strong>端到端 IEPL 物理专线：</strong>数据直接在内网传输完全不过公网 GFW，晚高峰连通率极佳",
            "<strong>彻底不限制在线设备数：</strong>全套餐支持无限台设备并发连接，多终端办公及家庭共享首选",
            "<strong>自研一键连接客户端：</strong>提供 Windows / Mac / Android 专属客户端，免去复杂配置",
            "<strong>千兆极速跑分：</strong>带宽充沛，拖拽 4K/8K 视频进度条毫秒级加载"
        ],
        "cons": [
            "更适合中高频使用用户，无零碎低用量极小包"
        ],
        "plans": [
            {"name": "基础套餐", "price": "¥15.00/月", "data": "100GB/月", "billing": "月付", "features": "彻底不限制在线设备数，IEPL专线，自研一键客户端"},
            {"name": "进阶套餐", "price": "¥30.00/月", "data": "250GB/月", "billing": "月付", "features": "彻底不限制在线设备数，IEPL专线，自研一键客户端"},
            {"name": "旗舰套餐", "price": "¥55.00/月", "data": "500GB/月", "billing": "月付", "features": "彻底不限制在线设备数，IEPL专线，自研一键客户端"}
        ]
    },
    "jilianyun-review": {
        "pros": [
            "<strong>100% IPLC 物理专线：</strong>2.5Gbps 物理内网信道，敏感时期稳定抗封锁",
            "<strong>晚高峰 0 丢包保障：</strong>全节点抖动低于 3ms，提供极致出海质量",
            "<strong>原生 IP 广播：</strong>免去繁琐验证码，完美解锁 ChatGPT 4o 与 Claude 3.5",
            "<strong>全天候客服支持：</strong>24 小时工单运维与社群实时解答"
        ],
        "cons": [
            "不适合极低预算极度敏感用户"
        ],
        "plans": [
            {"name": "体验版", "price": "¥15.50/月", "data": "100GB/月", "billing": "月付", "features": "IPLC物理专线，全节点1倍率，5台设备并发"},
            {"name": "标准版", "price": "¥32.00/月", "data": "220GB/月", "billing": "月付", "features": "IPLC物理专线，全节点1倍率，5台设备并发"},
            {"name": "尊享版", "price": "¥68.00/月", "data": "500GB/月", "billing": "月付", "features": "IPLC物理专线，全节点1倍率，5台设备并发"}
        ]
    },
    "edge-review": {
        "pros": [
            "<strong>RAM-only 纯内存架构：</strong>服务器无盘运行，断电即彻底物理销毁数据，零日志留存",
            "<strong>Anycast 自适应选路：</strong>动态匹配距离最近接入点，大幅降低网络往返延迟",
            "<strong>Web3 与安全风控优化：</strong>IP 隔离清洗，完美契合加密货币交易与学术研究",
            "<strong>全平台一键直连：</strong>提供简洁直观的客户端，一键极速连接"
        ],
        "cons": [
            "主打安全防护，娱乐小众节点相比大厂稍少"
        ],
        "plans": [
            {"name": "基础版", "price": "¥20.00/月", "data": "120GB/月", "billing": "月付", "features": "RAM纯内存架构，Anycast选路，3台设备"},
            {"name": "标准版", "price": "¥38.00/月", "data": "260GB/月", "billing": "月付", "features": "RAM纯内存架构，Anycast选路，3台设备"},
            {"name": "高级版", "price": "¥75.00/月", "data": "600GB/月", "billing": "月付", "features": "RAM纯内存架构，Anycast选路，3台设备"}
        ]
    },
    "jiuyun-review": {
        "pros": [
            "<strong>极致性价比单 G 成本：</strong>招财版低至 6 元/月 150G，聚财版 9 元/月 300G",
            "<strong>提供不限时防失联包：</strong>鸿运版 99 元 300G 永不过期，极佳的备用保底选择",
            "<strong>智能 BGP 多线中转：</strong>晚高峰流畅稳定，告别低价梯子卡顿断连噩梦",
            "<strong>免费提供美区 Apple ID：</strong>后台直接向注册用户提供美区 ID，轻松下载小火箭"
        ],
        "cons": [
            "极低起步价套餐不支持退款试用"
        ],
        "plans": [
            {"name": "招财版", "price": "¥6.00/月", "data": "150GB/月", "billing": "月付", "features": "3台设备同时在线，BGP中转，支持全流媒体解锁"},
            {"name": "聚财版", "price": "¥9.00/月", "data": "300GB/月", "billing": "月付", "features": "3台设备同时在线，BGP中转，性价比爆款推荐"},
            {"name": "旺财版", "price": "¥16.00/月", "data": "600GB/月", "billing": "月付", "features": "3台设备同时在线，大流量追剧与大文件下载首选"},
            {"name": "特惠季付版", "price": "¥18.00/季", "data": "200GB/月", "billing": "季付", "features": "折合¥6/月，每季自动重置流量"},
            {"name": "特惠年付版", "price": "¥99.00/年", "data": "400GB/月", "billing": "年付", "features": "折合¥8.25/月，全网超值年付省钱方案"},
            {"name": "鸿运版不限时包", "price": "¥99.00", "data": "300GB", "billing": "一次性", "features": "流量永久不过期，用多少扣多少，第二备用保底神器"}
        ]
    },
    "kexincloud-review": {
        "pros": [
            "<strong>品质 BGP 专线中转：</strong>99.9% 在线率保障，智能负载均衡分流",
            "<strong>全节点原生 IP 解锁：</strong>完美支持 Netflix 4K、Disney+、ChatGPT 4o",
            "<strong>透明账单无扣费陷阱：</strong>1.0x 统一扣费，账目清晰",
            "<strong>快速工单售后：</strong>提供高效技术解答与工单处理"
        ],
        "cons": [
            "套餐无极大容量上千 G 规格"
        ],
        "plans": [
            {"name": "基础版", "price": "¥15.00/月", "data": "120GB/月", "billing": "月付", "features": "BGP专线，原生IP，4台设备"},
            {"name": "标准版", "price": "¥30.00/月", "data": "260GB/月", "billing": "月付", "features": "BGP专线，原生IP，4台设备"}
        ]
    },
    "kuaili-review": {
        "pros": [
            "<strong>便宜大碗巨额流量：</strong>15 元享 200G 巨量大包，极高性价比",
            "<strong>不限制设备连接数：</strong>全节点千兆端口，多设备并发无压力",
            "<strong>支持一次性不限时包：</strong>提供永不过期流量包，备用安心",
            "<strong>港台影音番剧解锁：</strong>轻松解锁 B站 港台限制与 Netflix"
        ],
        "cons": [
            "高峰期极度大塞车时个别边缘节点存在小幅延迟波动"
        ],
        "plans": [
            {"name": "大碗套餐", "price": "¥15.00/月", "data": "200GB/月", "billing": "月付", "features": "不限设备数，千兆端口，大流量首选"},
            {"name": "海量套餐", "price": "¥35.00/月", "data": "500GB/月", "billing": "月付", "features": "不限设备数，千兆端口，大下载首选"}
        ]
    },
    "guangnianti-review": {
        "pros": [
            "<strong>物理中继流媒体优化：</strong>专为 Netflix 4K、Disney+、Apple TV 观影优化",
            "<strong>全节点 1.0x 透明扣费：</strong>无虚高倍率扣费陷阱",
            "<strong>全平台客户端深度适配：</strong>完美配合 Surge、Clash 规则分流",
            "<strong>智能 DNS 家宽解锁：</strong>原生 IP 解锁杜比视界"
        ],
        "cons": [
            "主打流媒体，不提供无限设备并发"
        ],
        "plans": [
            {"name": "流媒体基础包", "price": "¥20.00/月", "data": "160GB/月", "billing": "月付", "features": "4K流媒体解锁，物理中继，4台设备"},
            {"name": "流媒体高级包", "price": "¥40.00/月", "data": "350GB/月", "billing": "月付", "features": "4K流媒体解锁，物理中继，4台设备"}
        ]
    },
    "shunyun-review": {
        "pros": [
            "<strong>Anycast 选路网页秒开：</strong>降低 TTFB 首包握手延迟，网页排版瞬间呈现",
            "<strong>部署 Hysteria2 协议：</strong>针对移动宽带与高丢包环境专门优化",
            "<strong>千兆大带宽通道：</strong>跑满家用千兆宽带下载",
            "<strong>高并发稳定性：</strong>多窗口并发请求不阻塞"
        ],
        "cons": [
            "HY2 协议需使用现代客户端（如 Sing-box、Clash Verge Rev）"
        ],
        "plans": [
            {"name": "极速版", "price": "¥18.00/月", "data": "150GB/月", "billing": "月付", "features": "Anycast选路，Hysteria2协议，3台设备"},
            {"name": "尊享极速版", "price": "¥36.00/月", "data": "320GB/月", "billing": "月付", "features": "Anycast选路，Hysteria2协议，3台设备"}
        ]
    },
    "huanyuyun-review": {
        "pros": [
            "<strong>40+ 国家地区覆盖：</strong>包含阿根廷、土耳其、印度等小众节点",
            "<strong>BGP + IEPL 专线：</strong>双重技术保障，兼具低延迟与高稳定",
            "<strong>跨区消费订阅神器：</strong>方便 Steam 跨区购买与 Spotify 优惠订阅",
            "<strong>亚服游戏平稳加速：</strong>韩日 IEPL 低延迟联机"
        ],
        "cons": [
            "小众节点数量多，切换时需留意浏览器 Cookie 缓存"
        ],
        "plans": [
            {"name": "寰宇版", "price": "¥22.00/月", "data": "160GB/月", "billing": "月付", "features": "40+国家节点，BGP+IEPL专线，4台设备"},
            {"name": "寰宇旗舰版", "price": "¥45.00/月", "data": "380GB/月", "billing": "月付", "features": "40+国家节点，BGP+IEPL专线，4台设备"}
        ]
    },
    "naixi-review": {
        "pros": [
            "<strong>顶级 IPLC 专线通道：</strong>极高门槛保证人均带宽极大充裕",
            "<strong>99.999% 超高 SLA 保障：</strong>敏感时期连通如初，公网断连我独畅",
            "<strong>VIP 一对一客服：</strong>7x24 小时专家级技术支持",
            "<strong>物理隔离通道：</strong>支持 4K 直播推流与金融量化交易"
        ],
        "cons": [
            "门槛较高（¥45/月起步），适合高预算极客"
        ],
        "plans": [
            {"name": "专线月付订阅", "price": "¥45.00/月", "data": "200GB/月", "billing": "月付", "features": "顶级IPLC专线，物理隔离，5台设备并发"},
            {"name": "专线年付订阅", "price": "¥420.00/年", "data": "2400GB/年", "billing": "年付", "features": "顶级IPLC专线，物理隔离，5台设备并发"}
        ]
    },
    "huacloud-review": {
        "pros": [
            "<strong>老牌大厂口碑保障：</strong>多年稳定运营，全中转 BGP 线路，防跑路首选",
            "<strong>完善全平台教程：</strong>控制台提供极其详细的图文与视频指引",
            "<strong>流媒体与 AI 全解锁：</strong>稳定解锁 Netflix、ChatGPT、Claude",
            "<strong>强悍风控与运维：</strong>敏感时期节点在线率优异"
        ],
        "cons": [
            "定位品质级中转专线，起步价固定"
        ],
        "plans": [
            {"name": "专线月付", "price": "¥28.00/月", "data": "150GB/月", "billing": "月付", "features": "老牌大厂，全中转BGP，全平台教程适配"},
            {"name": "专线季付", "price": "¥78.00/季", "data": "500GB/季", "billing": "季付", "features": "老牌大厂，全中转BGP，全平台教程适配"}
        ]
    }
}

science_articles = [
    {'slug': 'pc-vpn-download-guide', 'title': '2026电脑VPN推荐：好用的梯子VPN排行榜与Windows/Mac客户端免费下载指南', 'date': '2026-08-29', 'cat': 'guide', 'views': 3420, 'excerpt': '2026年中国真正好用的电脑VPN与翻墙梯子软件推荐测评。提供Windows/Mac电脑端好用的VPN客户端官方免费下载入口、Clash Verge Rev一键导入教程与专线梯子节点推荐。'},
    {'slug': '2026-august-airport-monthly-report', 'title': '2026年8月机场月报与选购指南：晚高峰专线连通率实测与防跑路避坑建议', 'date': '2026-08-28', 'cat': 'eval', 'views': 3120, 'excerpt': '2026年8月最新机场选购月报，汇总极连云、光年梯、边缘节点、速界等主力专线机场在晚高峰的网络连通率与吞吐量表现，提供防跑路避坑解析。'},
    {'slug': 'ai-productivity-airport-guide', 'title': '2026 AI 生产力机场节点选择指南：解锁 ChatGPT 4o 与 Claude 3.5 的稳定节点推荐与配置教程', 'date': '2026-08-28', 'cat': 'tech', 'views': 2890, 'excerpt': '针对ChatGPT 4o、Claude 3.5、Midjourney等AI生产力工具防风控封号的节点选择及机场配置教程。'},
    {'slug': 'hysteria2-vless-anytls-protocol-2026', 'title': '2026年翻墙协议科普：Hysteria2、VLESS-REALITY 与 anytls 协议特点解析与客户端选择', 'date': '2026-08-28', 'cat': 'tech', 'views': 2450, 'excerpt': '2026年主流代理协议深度拆解，对比基于UDP的Hysteria2、免证书指纹的VLESS-REALITY与anytls在抗封锁和高丢包环境下的提速优势。'},
    {'slug': 'cost-per-gb-buying-guide-2026', 'title': '2026年机场选购指南：看懂流量倍率规则、算清真实单价与选择性价比套餐', 'date': '2026-08-27', 'cat': 'promo', 'views': 2980, 'excerpt': '教您如何在购买机场时算清真实性价比。解析节点扣费倍率陷阱、对比月付套餐与不限时流量包的划算程度，提供平价便宜机场选购技巧。'},
    {'slug': 'airport-runaway-warning-2026', 'title': '2026年VPN机场跑路名单汇总 | 机场跑路黑名单、跑路原因与避坑指南', 'date': '2026-08-27', 'cat': 'warning', 'views': 3181, 'excerpt': '2026年最新VPN翻墙机场跑路黑名单与避坑指南。整理神速云、大麦云、星河云、闪电云等近期跑路机场名单，拆解低价圈钱与换皮洗库套路。'},
    {'slug': 'subscription-guide', 'title': '网络订阅地址获取与客户端通用配置防跑路避坑常识', 'date': '2026-08-27', 'cat': 'warning', 'views': 3181, 'excerpt': '科普网络订阅地址获取流程，解析代理订阅泄露风险，并提供在机场遭遇攻击、跑路等风控事件下的高可用备用方案。'},
    {'slug': 'airport-guide-2026', 'title': '2026年机场排行榜：高性价比翻墙机场科普与横向评测推荐', 'date': '2026-07-24', 'cat': 'eval', 'views': 2540, 'excerpt': '2026年最新稳定高速且便宜高性价比的专线机场推荐合集，涵盖极连云、速界、边缘、光年梯等9大主流梯子深度横向评测。'},
    {'slug': 'iplc-guide', 'title': 'IPLC/IEPL专线科普：4K不卡顿、游戏加速与专线机场完全指南', 'date': '2026-07-23', 'cat': 'tech', 'views': 1890, 'excerpt': '深入科普什么是IPLC与IEPL物理专线，为什么专线机场能够做到晚高峰4K不卡顿与极低延迟游戏加速，并推荐性价比专线。'},
    {'slug': 'streaming-ai-guide', 'title': 'Netflix/ChatGPT/TikTok机场选择指南：流媒体与AI工具加速完全攻略', 'date': '2026-07-22', 'cat': 'tech', 'views': 2310, 'excerpt': '针对Netflix、Disney+流媒体解锁以及ChatGPT、Claude、TikTok等海外应用防风控封号的节点选择及机场配置教程。'},
    {'slug': 'clash-tutorial', 'title': 'Clash配置教程：2026年最全Clash节点导入与订阅地址使用完全指南', 'date': '2026-07-20', 'cat': 'guide', 'views': 2120, 'excerpt': '最详细的Clash客户端使用教程，包含Mihomo内核Clash Verge、Clash for Windows的节点获取、订阅导入与系统代理开启避坑指南。'},
    {'slug': 'shadowrocket-setup', 'title': 'Shadowrocket配置教程：iOS苹果小火箭订阅地址导入与SS/SSR专线配置完全指南', 'date': '2026-07-16', 'cat': 'guide', 'views': 1980, 'excerpt': 'iOS苹果系统下最主流的Shadowrocket（小火箭）客户端配置教程，详解美区苹果账号购买下载、订阅地址拉取及SS/SSR/V2Ray专线导入。'},
    {'slug': 'v2rayng-guide', 'title': 'V2RayNG配置教程：安卓手机一键导入订阅地址与VLESS/Vmess网络配置攻略', 'date': '2026-07-09', 'cat': 'guide', 'views': 1560, 'excerpt': 'Android安卓手机翻墙必备客户端V2RayNG详细配置教程，涵盖节点订阅获取、一键测试连接性、Reality与VLESS协议导入教程。'},
    {'slug': 'lantern-alternative', 'title': '蓝灯Lantern好用吗？2026年蓝灯替代方案与SS/SSR专线中转机场推荐', 'date': '2026-07-02', 'cat': 'eval', 'views': 940, 'excerpt': '深入剖析老牌翻墙VPN蓝灯Lantern在2026年无法连上的原因，提供主流Shadowsocks/V2Ray专线机场等更优高性价比替代方案。'},
    {'slug': 'reality-protocol', 'title': 'Reality协议科普：什么是Reality协议？安全性与主流客户端配置详解', 'date': '2026-06-25', 'cat': 'tech', 'views': 1120, 'excerpt': '深入探讨2026年最热门的Xray Reality协议，分析其免除证书指纹、模拟真实网页混淆的无感知安全性及主流客户端如何配置导入。'},
    {'slug': 'hysteria2-vs-tuic', 'title': 'Hysteria2与Tuic协议对比：晚高峰高丢包环境下的最佳UDP翻墙协议选择', 'date': '2026-06-18', 'cat': 'tech', 'views': 920, 'excerpt': '对比基于UDP的Hysteria2与Tuic协议，探讨它们在低带宽、晚高峰高丢包率恶劣网络环境下的极速提速性能表现与适用场景。'},
    {'slug': 'iplc-vs-iepl', 'title': 'IPLC专线机场与IEPL中转有何区别？主流专线机场网络传输架构大科普', 'date': '2026-06-11', 'cat': 'tech', 'views': 1340, 'excerpt': '深度科普IPLC（国际私用出租信道）与IEPL（国际以太网专线）的底层物理架构区别，帮助科学上网用户避开虚假中转宣传。'},
    {'slug': 'openwrt-router', 'title': 'OpenWrt科普教程：软路由固件插件安装、Clash/Sing-box节点配置完全指南', 'date': '2026-06-04', 'cat': 'guide', 'views': 1650, 'excerpt': '软路由科学上网一站式指南，介绍如何在OpenWrt系统安装PassWall、SSR-Plus或OpenClash插件，并导入专线中转节点订阅。'},
    {'slug': 'vps-vs-airport', 'title': '自建节点对比专线机场：2026年为什么我不建议新手折腾搭建翻墙？', 'date': '2026-05-28', 'cat': 'eval', 'views': 1040, 'excerpt': '从服务器购买成本、防封锁技术门槛、网络晚高峰QoS限速等多维度对比自建VPS节点与直接订阅专线机场的优缺点，揭开自建翻墙高昂成本。'},
    {'slug': 'one-multiplier', 'title': '什么是1倍率机场？如何看懂计费规则，避开机场流量折算陷阱？', 'date': '2026-05-21', 'cat': 'promo', 'views': 1420, 'excerpt': '详解机场计费面板中的流量倍率规则（如0.1倍率、1倍率、5倍率），教你如何计算真实流量消耗，避开不良商家的充值资费陷阱。'},
    {'slug': 'streaming-unlock', 'title': '什么是解锁流媒体节点？Netflix/Disney+ 住宅IP分流选择科普与机场推荐', 'date': '2026-05-14', 'cat': 'tech', 'views': 1180, 'excerpt': '科普流媒体平台IP封锁机制，详解如何利用机场的原生住宅IP进行分流配置，顺利看懂Netflix独家片源与Disney+。'},
    {'slug': 'clash-subscription', 'title': '网络订阅地址获取与客户端通用配置防跑路避坑常识', 'date': '2026-05-07', 'cat': 'promo', 'views': 1220, 'excerpt': '科普网络订阅地址获取流程，解析代理订阅泄露风险，并提供在机场遭遇攻击、跑路等风控事件下的高可用备用方案。'},
    {'slug': 'hy2-performance', 'title': 'Hysteria2协议在低带宽晚高峰下的速度实测与Reality/VLESS协议横向评测', 'date': '2026-04-30', 'cat': 'tech', 'views': 1080, 'excerpt': '在恶劣带宽环境下对Hysteria2协议进行吞吐量和延迟实测，对比VLESS-XTLS与Reality混淆的防封锁及晚高峰抗丢包性。'},
    {'slug': 'tuic-latency', 'title': 'Tuic协议适合玩外服游戏吗？Tuic低延迟原理分析与SS/SSR专线游戏节点选择', 'date': '2026-04-23', 'cat': 'tech', 'views': 1150, 'excerpt': '分析新一代Tuic协议在低延迟网络通信中的优势，结合UDP Full-Cone NAT技术评估其在Steam、Apex游戏联机中的实际加速表现。'},
    {'slug': 'router-firmware', 'title': '软路由科普深度科普：OpenWrt主流固件插件性能对比与Clash配置教程', 'date': '2026-04-16', 'cat': 'guide', 'views': 950, 'excerpt': '深度对比OpenWrt软路由系统下的OpenClash、HomeProxy与PassWall等常用插件的系统资源占用率与专线分流效率。'},
    {'slug': 'reality-vless-verge', 'title': 'VLESS与Reality协议在Clash Verge中的通用配置与速度优化教程', 'date': '2026-04-09', 'cat': 'guide', 'views': 1310, 'excerpt': '手把手教你在Clash Verge客户端中如何利用YAML配置扩展对VLESS和Reality协议进行参数调优与Anycast分流策略配置。'},
    {'slug': 'shadowrocket-h2', 'title': '小火箭Hysteria2节点怎么配置？iOS Shadowrocket基于UDP的高丢包提提速教程', 'date': '2026-04-02', 'cat': 'guide', 'views': 1480, 'excerpt': '介绍iOS苹果小火箭Shadowrocket配置Hysteria2协议的具体端口及UDP参数，解决晚高峰丢包网络卡顿的提速实操教程。'},
    {'slug': 'ssr-airport-guide', 'title': 'SSR机场推荐：2026年最稳定SSR/V2Ray节点机场评选与购买指南', 'date': '2026-03-05', 'cat': 'eval', 'views': 1650, 'excerpt': '2026年最值得订阅的SSR与V2Ray协议机场推荐合集，对比各家的节点覆盖地区、晚高峰稳定性与流量套餐性价比，帮助新手快速选出最适合自己的翻墙机场。'},
    {'slug': 'android-vpn-guide', 'title': '安卓翻墙教程：V2RayNG一键导入SSR/V2Ray/VLESS节点完全配置指南', 'date': '2026-02-28', 'cat': 'guide', 'views': 1420, 'excerpt': '面向Android安卓用户的翻墙入门配置教程，手把手教你下载安装V2RayNG，导入SSR/V2Ray/VLESS订阅节点并开启系统VPN，彻底解决安卓手机科学上网卡顿。'},
    {'slug': 'trojan-protocol', 'title': 'Trojan协议科普：原理解析、与V2Ray对比及主流客户端配置详解', 'date': '2026-02-24', 'cat': 'tech', 'views': 1190, 'excerpt': '深入剖析Trojan翻墙协议的TLS伪装原理，与V2Ray VMess/VLESS协议的安全防检测能力横向对比，并提供iOS、安卓、Windows主流客户端配置教程。'},
    {'slug': 'free-vpn-risks', 'title': '免费翻墙VPN有哪些隐患？2026年免费VPN与付费专线机场全面对比', 'date': '2026-02-17', 'cat': 'promo', 'views': 1380, 'excerpt': '揭露市面上免费翻墙VPN的七大隐患，包括数据隐私泄露、广告注入、带宽限速、跑路风险等，并从价格、速度、安全性等维度与付费专线机场进行全面横向对比。'},
    {'slug': 'glados-review', 'title': 'GLaDOS机场测评：面向开发者与程序员的稳定高速科学上网机场评测', 'date': '2026-02-10', 'cat': 'eval', 'views': 1290, 'excerpt': 'GLaDOS机场深度评测，涵盖节点覆盖、晚高峰延迟测试、Netflix解锁能力与套餐价格综合评分，探讨其是否适合程序员与开发者群体的日常科学上网需求。'},
    {'slug': 'openwrt-singbox', 'title': 'Sing-box在OpenWrt软路由系统下的配置与高吞吐专线分流教程', 'date': '2026-03-26', 'cat': 'guide', 'views': 1240, 'excerpt': '介绍在OpenWrt软路由下如何配置使用Sing-box核心，以及如何利用专线节点实现大带宽大吞吐的智能分流优化。'},
    {'slug': 'blue-lantern-vpn', 'title': '蓝灯VPN好用吗？为什么老牌翻墙VPN蓝灯连不上与最优机场方案对比', 'date': '2026-03-19', 'cat': 'eval', 'views': 980, 'excerpt': '深度分析老牌翻墙VPN蓝灯（Lantern）连不上的原因，并对比主流专线中转机场，为寻求高稳定梯子方案的用户提供指引。'},
    {'slug': 'reality-vless-comparison', 'title': 'Reality混淆协议与传统VLESS/Vmess加密协议安全性与防封锁横向对比', 'date': '2026-03-12', 'cat': 'tech', 'views': 1050, 'excerpt': '对比分析新一代Xray Reality混淆协议与传统VMess、VLESS协议的安全防检测能力及主流科学上网客户端配置选型。'},
    {'slug': 'shandian-warning', 'title': '闪电机场跑路避雷：Shandian VPN失联始末与高风险机场识别指南', 'date': '2026-07-28', 'cat': 'warning', 'views': 1860, 'excerpt': '闪电机场（Shandian VPN）跑路避雷警报，深度揭露其失联始末、用户损失及识别高风险机场的实用防骗技巧。'},
    {'slug': 'geeknet-warning', 'title': '极客网络避雷警告：Geek Net节点重度故障与用户退款纠纷全记录', 'date': '2026-07-26', 'cat': 'warning', 'views': 1520, 'excerpt': '极客网络（Geek Net）机场避雷警告：节点重度故障、大面积宕机与用户退款纠纷全记录，附识别问题机场的实用方法。'},
    {'slug': 'feitian-warning', 'title': '飞天梯停止运营避雷：Feitian从盛极一时到突然关停的全过程复盘', 'date': '2026-07-25', 'cat': 'warning', 'views': 1340, 'excerpt': '飞天梯（Feitian）从盛极一时到突然关停的全过程复盘，附科学上网防跑路实用指南。'}
]

# 合并所有文章元信息列表，排序供归档与侧边栏使用
merged_articles = []
for ap in airports:
    # 模拟机场测评的日期、描述等
    # 奶昔和花云需要有各自的元信息
    date_val = '2026-07-18' if ap['slug'] == 'jilianyun-review' else '2026-07-03'
    views_val = 2180 if ap['slug'] == 'jilianyun-review' else 1950
    merged_articles.append({
        'slug': ap['slug'],
        'title': ap['name'] + ' 机场评测：高稳定性与极速专线节点官网订阅推荐',
        'date': date_val,
        'cat': 'airport',
        'views': views_val,
        'excerpt': f"详细对 {ap['name']} 机场进行多节点速度实测、晚高峰延迟丢包连通监控及套餐资费比对..."
    })

for sa in science_articles:
    merged_articles.append({
        'slug': sa['slug'],
        'title': sa['title'],
        'date': sa['date'],
        'cat': sa['cat'],
        'views': sa['views'],
        'excerpt': sa['excerpt']
    })

# 按日期排序
merged_articles.sort(key=lambda x: x['date'], reverse=True)

# 热门推荐：选5篇
hot_articles = merged_articles[:5]

# 生成左侧边栏 (Left Sidebar) 的共用 HTML

def get_left_sidebar_html(depth=0, toc_links_html="", cta_card_html="", article_tags=None, body_content="", page_name=""):
    prefix = "" if depth == 0 else "../"
    
    def get_tag_link(tag, curr_depth):
        mapping = {
            '机场评测': 'index.html?category=eval',
            '科普专栏': 'vpn-guide.html',
            'Clash配置': 'articles/clash-tutorial.html',
            '小火箭': 'articles/shadowrocket-setup.html',
            'Reality协议': 'articles/reality-protocol.html',
            'Hysteria2': 'articles/hysteria2-vs-tuic.html',
            '便宜机场': 'articles/one-multiplier.html',
            'Netflix': 'articles/streaming-ai-guide.html',
            'ChatGPT': 'articles/streaming-ai-guide.html',
            '软路由': 'articles/openwrt-router.html',
            'SSR机场推荐': 'articles/ssr-airport-guide.html',
            'V2Ray节点': 'articles/ssr-airport-guide.html',
            'Shadowsocks': 'articles/clash-subscription.html',
            '免费翻墙VPN': 'articles/free-vpn-risks.html',
            'Trojan协议': 'articles/trojan-protocol.html',
            'iPhone翻墙': 'articles/shadowrocket-setup.html',
            '安卓VPN': 'articles/android-vpn-guide.html',
            'GLaDOS机场': 'articles/glados-review.html',
            '付费机场': 'articles/airport-guide-2026.html',
            '节点订阅': 'articles/clash-subscription.html',
            '流媒体解锁': 'articles/streaming-unlock.html',
            'Disney+': 'articles/streaming-unlock.html',
            'TikTok加速': 'articles/streaming-ai-guide.html',
            '国内电脑VPN': 'articles/lantern-alternative.html',
            '低延迟': 'articles/iplc-guide.html',
            '4K不卡顿': 'articles/iplc-guide.html',
            '游戏专线': 'articles/tuic-latency.html',
            '安全防护': 'articles/reality-protocol.html',
            '按量付费': 'articles/one-multiplier.html',
            '傻瓜一键翻墙': 'articles/clash-tutorial.html',
            '月付': 'articles/one-multiplier.html'
        }
        raw_link = mapping.get(tag, 'index.html')
        if curr_depth == 1:
            if raw_link.startswith('articles/'):
                return raw_link.replace('articles/', '')
            else:
                return f"../{raw_link}"
        else:
            return raw_link

    total_posts = len(science_articles) + len(airports)
    total_tags = 31
    daily_views = "99+"
    
    # 静态分类 HTML
    cat_items = [
        {'name': '全部文章', 'slug': 'all'},
        {'name': '机场评测', 'slug': 'eval'},
        {'name': '新手教程', 'slug': 'guide'},
        {'name': '技术进阶', 'slug': 'tech'},
        {'name': '优惠活动', 'slug': 'promo'}
    ]
    categories_html = '<div class="sidebar-category-list">\n'
    for c in cat_items:
        link_url = f"{prefix}index.html" if c['slug'] == 'all' else f"{prefix}index.html?category={c['slug']}"
        categories_html += f'  <a href="{link_url}" class="sidebar-cat-item">{c["name"]}</a>\n'
    categories_html += '</div>'
    
    # 标签云
    tags = ['机场评测', '科普专栏', '低延迟', '4K不卡顿', 'Clash配置', '小火箭', 'Reality协议', 'Hysteria2', '便宜机场', '月付', '按量付费', 'Netflix', 'ChatGPT', '软路由', '游戏专线', '安全防护', 'SSR机场推荐', 'V2Ray节点', 'Shadowsocks', '免费翻墙VPN', 'Trojan协议', 'iPhone翻墙', '安卓VPN', '傻瓜一键翻墙', 'GLaDOS机场', '付费机场', '节点订阅', '流媒体解锁', 'Disney+', 'TikTok加速', '国内电脑VPN']
    tags_html = "".join([f'<a href="{get_tag_link(t, depth)}" class="tag-pill" data-tag="{t}">{t}</a>' for t in tags])
    
    if article_tags:
        article_tags_html = "".join([f'<a href="{get_tag_link(t, depth)}" class="tag-pill" data-tag="{t}"># {t}</a>' for t in article_tags])
    else:
        article_tags_html = ""

    # 热门测速文章 Widget
    hot_items_html = ""
    for idx, ha in enumerate(hot_articles, 1):
        link_path = f"articles/{ha['slug']}.html" if depth == 0 else f"{ha['slug']}.html"
        hot_items_html += f"""
          <div class="mini-article-item">
            <span class="mini-article-index">{idx}</span>
            <div class="mini-article-content">
              <a href="{link_path}" class="mini-article-title">{ha['title']}</a>
              <span class="mini-article-date">📅 {ha['date']}</span>
            </div>
          </div>"""

    hot_widget_html = f"""
        <div class="sidebar-card">
          <h3 class="toc-title">热门测速文章</h3>
          <div style="display: flex; flex-direction: column; gap: 12px;">
            {hot_items_html}
          </div>
        </div>"""

    # 侧边栏图片 Banner Widget
    airports_guide_path = f"articles/airport-guide-2026.html" if depth == 0 else "airport-guide-2026.html"
    software_guide_path = f"articles/clash-tutorial.html" if depth == 0 else "clash-tutorial.html"
    img_prefix = "images/" if depth == 0 else "../images/"

    cta_widget_html = f"""
        <div class="sidebar-card sidebar-banner-widget" style="padding: 12px; display: flex; flex-direction: column; gap: 12px; background: transparent; border: none; box-shadow: none;">
          <a href="{airports_guide_path}" class="sidebar-banner-item" style="display: block; border-radius: var(--radius-md); overflow: hidden; transition: transform 0.25s ease, box-shadow 0.25s ease; border: 1px solid var(--border-color);">
            <img src="{img_prefix}sidebar_banner_airports.png" alt="翻墙机场推荐" style="width: 100%; height: auto; display: block; object-fit: cover;">
          </a>
          <a href="{software_guide_path}" class="sidebar-banner-item" style="display: block; border-radius: var(--radius-md); overflow: hidden; transition: transform 0.25s ease, box-shadow 0.25s ease; border: 1px solid var(--border-color);">
            <img src="{img_prefix}sidebar_banner_apps.png" alt="科学上网客户端教程" style="width: 100%; height: auto; display: block; object-fit: cover;">
          </a>
        </div>"""

    # 本文大纲 Widget
    toc_widget_html = ""
    if toc_links_html:
        toc_widget_html = f"""
        <div class="sidebar-card toc-card">
          <h3 class="toc-title">本文大纲</h3>
          <div class="toc-list">
            {toc_links_html}
          </div>
        </div>"""

    # 机场推荐 List (主页放 6 个，文章页精简放 2 个精选卡片，确保左右对齐)
    all_promos = [
        {'name': '极连云', 'desc': '全程 IPLC 物理专线 · 晚高峰零丢包保障', 'slug': 'jilianyun-review', 'logo': 'https://i.ibb.co/TxW2rqGj/jilianyunlogo.webp', 'style': 'linear-gradient(135deg, #a299ca 0%, #6366f1 100%)', 'btn_class': 'promo-btn-white'},
        {'name': '速界', 'desc': '中转专线 · 不限制设备数 · 一键连接', 'slug': 'sujie-review', 'logo': 'https://i.ibb.co/tpkZpVhs/sujielogo.webp', 'style': 'linear-gradient(135deg, #38bdf8 0%, #0284c7 100%)', 'btn_class': 'promo-btn-white'},
        {'name': '边缘节点', 'desc': '只读内存服务器 · 零日志绝对安全', 'slug': 'edge-review', 'logo': 'https://i.ibb.co/C5P4QcfT/bianyuanjiedianlogo.webp', 'style': 'linear-gradient(135deg, #7ccaae 0%, #059669 100%)', 'btn_class': 'promo-btn-white'},
        {'name': '光年梯', 'desc': '物理中继线路 · 高清流媒体智能解锁', 'slug': 'guangnianti-review', 'logo': 'https://i.ibb.co/mCYxy3yM/guanniantilogo.webp', 'style': 'linear-gradient(135deg, #ffb69b 0%, #ea580c 100%)', 'btn_class': 'promo-btn-white'},
        {'name': '快狸', 'desc': '设备数不限 · ¥15/月起高性价比备用', 'slug': 'kuaili-review', 'logo': 'https://i.ibb.co/1f4FvF92/kuaililogo.webp', 'style': 'linear-gradient(135deg, #ecec84 0%, #eab308 100%)', 'btn_class': 'promo-btn-black'},
        {'name': '瞬云', 'desc': 'Anycast 智能选路 · 千兆大带宽端口', 'slug': 'shunyun-review', 'logo': 'https://i.ibb.co/jkR2rZRw/shunyunlogo.webp', 'style': 'linear-gradient(135deg, #fb7185 0%, #e11d48 100%)', 'btn_class': 'promo-btn-white'}
    ]
    
    if depth == 1 and body_content:
        chars = len(body_content)
        if chars < 1200:
            count = 2
        elif chars < 1800:
            count = 3
        elif chars < 2500:
            count = 4
        elif chars < 3500:
            count = 5
        else:
            count = 6
        current_promos = all_promos[:count]
    else:
        current_promos = all_promos if depth == 0 else all_promos[:6]
    
    promo_cards_html = ""
    for p in current_promos:
        link_path = f"articles/{p['slug']}.html" if depth == 0 else f"{p['slug']}.html"
        promo_cards_html += f"""
            <a href="{link_path}" class="sidebar-promo-card">
              <div class="promo-card-left">
                <h4 class="promo-card-title">{p['name']} 机场</h4>
                <p class="promo-card-desc">{p['desc']}</p>
                <span class="promo-card-btn">立即评测</span>
              </div>
              <div class="promo-card-right">
                <img src="{p['logo']}" alt="{p['name']}" class="promo-card-logo">
              </div>
            </a>"""
            
    promo_widget_html = f"""
        <div class="sidebar-card promo-list-widget">
          <h3 class="toc-title">机场推荐</h3>
          <div class="sidebar-promo-container">
            {promo_cards_html}
          </div>
        </div>"""

    # 主页 vs 文章页 侧边栏卡片输出差异
    if depth == 0:
        if page_name == "about":
            sidebar_inner_html = f"""
        <div class="sidebar-card profile-card">
          <div class="profile-avatar" style="width: 86px; height: 86px; margin: 0 auto 14px; border-radius: 50%; overflow: hidden; border: 3px solid var(--accent-primary); box-shadow: 0 4px 16px rgba(15, 82, 186, 0.25); background: #ffffff; padding: 3px;">
            <img src="{prefix}images/profile_avatar.png" alt="vpn推荐" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%; display: block;">
          </div>
          <h3 class="profile-name">vpn推荐</h3>
          <p class="profile-motto">vpn推荐 专注于2026年最新、最稳的国际物理专线、BGP中继翻墙机场评测与科学上网客户端避坑科普。</p>
          <div class="profile-stats">
            <div class="stat-item">
              <span class="stat-value">{total_posts}</span>
              <span class="stat-label">文章数</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{total_tags}</span>
              <span class="stat-label">标签数</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{daily_views}</span>
              <span class="stat-label">日访问量</span>
            </div>
          </div>
          <div class="profile-buttons">
            <a href="{prefix}about.html" class="profile-btn profile-btn-primary">关于我们</a>
            <a href="{prefix}vpn-guide.html" class="profile-btn profile-btn-secondary">科普专栏</a>
          </div>
        </div>
        
        <div class="sidebar-card">
          <h3 class="toc-title">分类目录</h3>
          {categories_html}
        </div>

        {cta_widget_html}
        """
        else:
            # 主页: 完整大侧栏
            promo_section = "" if page_name == "archives" else promo_widget_html
            sidebar_inner_html = f"""
        <div class="sidebar-card profile-card">
          <div class="profile-avatar" style="width: 86px; height: 86px; margin: 0 auto 14px; border-radius: 50%; overflow: hidden; border: 3px solid var(--accent-primary); box-shadow: 0 4px 16px rgba(15, 82, 186, 0.25); background: #ffffff; padding: 3px;">
            <img src="{prefix}images/profile_avatar.png" alt="vpn推荐" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%; display: block;">
          </div>
          <h3 class="profile-name">vpn推荐</h3>
          <p class="profile-motto">vpn推荐 专注于2026年最新、最稳的国际物理专线、BGP中继翻墙机场评测与科学上网客户端避坑科普。</p>
          <div class="profile-stats">
            <div class="stat-item">
              <span class="stat-value">{total_posts}</span>
              <span class="stat-label">文章数</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{total_tags}</span>
              <span class="stat-label">标签数</span>
            </div>
            <div class="stat-item">
              <span class="stat-value">{daily_views}</span>
              <span class="stat-label">日访问量</span>
            </div>
          </div>
          <div class="profile-buttons">
            <a href="{prefix}about.html" class="profile-btn profile-btn-primary">关于我们</a>
            <a href="{prefix}vpn-guide.html" class="profile-btn profile-btn-secondary">科普专栏</a>
          </div>
        </div>
        
        <div class="sidebar-card">
          <h3 class="toc-title">分类目录</h3>
          {categories_html}
        </div>

        {cta_widget_html}
        
        <div class="sidebar-card">
          <h3 class="toc-title">热门标签</h3>
          <div class="tags-cloud">
            {tags_html}
          </div>
        </div>

        {hot_widget_html}
        {promo_section}
        """
    else:
        # 文章页: 精简轻量侧栏 (优先展示大纲, 避免拉长超标，左右对齐)
        tags_title = "本文标签" if article_tags else "热门标签"
        hot_section = hot_widget_html if page_name == "airport-guide-2026" else ""
        tags_content = article_tags_html if article_tags else tags_html
        
        sidebar_inner_html = f"""
        <div class="sidebar-card profile-card">
          <div class="profile-avatar" style="width: 76px; height: 76px; margin: 0 auto 10px; border-radius: 50%; overflow: hidden; border: 3px solid var(--accent-primary); box-shadow: 0 4px 12px rgba(15, 82, 186, 0.2); background: #ffffff; padding: 2px;">
            <img src="{prefix}images/profile_avatar.png" alt="vpn推荐" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%; display: block;">
          </div>
          <h3 class="profile-name" style="font-size: 1.1rem;">vpn推荐</h3>
          <p class="profile-motto" style="font-size: 0.76rem; margin-bottom: 12px;">vpn推荐 专注于2026年最新、最稳的国际物理专线、BGP中继翻墙机场评测与科学上网客户端避坑科普。</p>
        </div>
        
        {toc_widget_html}

        {cta_card_html}

        <div class="sidebar-card">
          <h3 class="toc-title">分类目录</h3>
          {categories_html}
        </div>

        <div class="sidebar-card">
          <h3 class="toc-title">{tags_title}</h3>
          <div class="tags-cloud">
            {tags_content}
          </div>
        </div>

        {promo_widget_html}
        {hot_section}
        """

    html = f"""
      <aside class="left-sidebar">
        {sidebar_inner_html}
      </aside>
    """
    return html

# 生成右侧边栏 (全站不要右边栏，统一双栏)
def get_right_sidebar_html(depth=0, toc_links_html=""):
    return ""


# 清理正文中的未闭合/多余标签及AI提炼的图标
def clean_body_content(body_content):
    # 彻底清除截取正文时混入的重复页脚、FAQ、版权声明、底部导航卡片与脚本地块
    body_content = re.sub(r'<footer\s+class="footer">.*?</footer>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<div\s+class="geo-faq-section".*?</div>\s*</div>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<div\s+class="geo-faq-section".*?</div>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<script\s+type="application/ld\+json">.*?</script>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<div\s+class="article-copyright-box".*?</div>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<div\s+class="article-prev-next-nav".*?</div>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<a\s+[^>]*class="[^"]*article-nav-card[^"]*"[^>]*>.*?</a>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<script\s+src="[^"]*main\.js"></script>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<div\s+class="ai-summary-card".*?</div>\s*</div>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<div\s+class="ai-summary-card".*?</div>', '', body_content, flags=re.DOTALL)
    body_content = re.sub(r'<p[^>]*>\s*<strong>本章速览（核心结论）：</strong>.*?</p>', '', body_content, flags=re.DOTALL)

    # 清理多余注释
    body_content = re.sub(r'<!--\s*GEO 优化: FAQ 常见问题板块\s*-->', '', body_content)
    body_content = re.sub(r'<!--\s*GEO 优化: AI 搜索摘要卡片\s*-->', '', body_content)
    body_content = re.sub(r'<!--\s*JSON-LD Schema \(SEO/GEO 自动抓取\)\s*-->', '', body_content)
    body_content = re.sub(r'<!--\s*版权与阅读须知卡片\s*-->', '', body_content)

    # 移除多余的闭合 article, main, body, html 标签
    body_content = body_content.replace("</article>", "").replace("</main>", "").replace("</body>", "").replace("</html>", "")
    
    # 移除末尾独立多余的闭合 </div>
    body_content = re.sub(r'</div>\s*$', '', body_content)
    
    return body_content.strip()


# 提取文章底部的相关标签并从正文中移除，以便将其渲染至右边栏
def extract_article_tags(body_content):
    # 查找 <div class="card-footer"
    footer_idx = body_content.find('<div class="card-footer"')
    if footer_idx == -1:
        # 也有可能是没有 card-footer，直接含有 card-tags
        footer_idx = body_content.find('<div class="card-tags"')
        
    if footer_idx == -1:
        return body_content, []
        
    footer_content = body_content[footer_idx:]
    cleaned_body = body_content[:footer_idx].strip()
    
    # 匹配其中的标签名称，例如：# 1倍率机场 或者 # tag_name
    tags_found = re.findall(r'#\s*([^<]+)', footer_content)
    tags_found = [t.strip() for t in tags_found if t.strip()]
    
    # 去重
    seen = set()
    unique_tags = []
    for t in tags_found:
        if t not in seen:
            seen.add(t)
            unique_tags.append(t)
            
    return cleaned_body, unique_tags


# 生成符合图123美学参考的高颜值文章 Cover 卡片 HTML
def build_article_card_cover_html(title, cat, slug, tags_list, depth=0):
    local_path = os.path.join(dest_dir, "images", "articles", f"{slug}.jpg")
    prefix = "" if depth == 0 else "../"
    if os.path.exists(local_path):
        img_url = f"{prefix}images/articles/{slug}.jpg"
    else:
        img_url = f"https://picsum.photos/seed/{slug}/140/90"
    return f"""
        <div class="article-card-cover-graphic" style="flex-shrink: 0; width: 140px; height: 90px; border-radius: 4px; overflow: hidden; display: block; background: var(--bg-tertiary); margin-left: 20px;">
          <img src="{img_url}" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.3s ease;" alt="{title}" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
    """


def get_article_link(slug, depth=0):
    return f"articles/{slug}.html" if depth == 0 else f"{slug}.html"

# 统一生成公共 Header (深度 depth=0 表示根目录，depth=1 表示 articles 文件夹内)
def get_header_html(depth=0):
    prefix = "" if depth == 0 else "../"
    
    # 机场推荐下拉单列表
    airport_dropdown = ""
    for ap in airports:
        link_val = get_article_link(ap['slug'], depth)
        airport_dropdown += f'<a href="{link_val}" class="dropdown-item">{ap["name"]} 测评</a>\n'
    html = f"""
  <script>
    (function() {{
      let savedTheme = null;
      try {{
        savedTheme = localStorage.getItem('theme');
      }} catch (e) {{}}
      const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const theme = savedTheme === 'dark' || (!savedTheme && systemPrefersDark) ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', theme);
    }})();
  </script>
  
  <header class="header">
    <div class="container header-container">
      <a href="{prefix}index.html" class="logo" onclick="if(window.resetFilters) {{ window.resetFilters(); }} else {{ return true; }}">
        <img class="logo-icon" src="{prefix}images/logo.png?v=2" alt="vpn推荐" />
        <span>vpn推荐</span>
      </a>
      
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle Menu">☰</button>
      
      <nav class="nav" id="nav-menu">
        <a href="{prefix}index.html" class="nav-link">主页</a>
        
        <!-- 机场推荐 (下拉式) -->
        <div class="nav-item">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">机场推荐 <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            {airport_dropdown}
          </div>
        </div>
        
        <!-- 科普文章 (下拉式) -->
        <div class="nav-item">
          <a href="{prefix}vpn-guide.html" class="nav-link dropdown-toggle">干货分享 <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="{get_article_link('airport-guide-2026', depth)}" class="dropdown-item">机场排行与评测</a>
            <a href="{get_article_link('one-multiplier', depth)}" class="dropdown-item">便宜月付推荐</a>
            <a href="{get_article_link('shandian-warning', depth)}" class="dropdown-item">⚠️ 避雷指南</a>
            <a href="{prefix}vpn-guide.html" class="dropdown-item">📚 全部干货科普 →</a>
          </div>
        </div>
        
        <!-- 更多 -->
        <div class="nav-item">
          <a href="#" class="nav-link dropdown-toggle" onclick="return false;">更多 <svg viewBox="0 0 24 24"><path d="M7 10l5 5 5-5z"/></svg></a>
          <div class="dropdown-menu">
            <a href="{prefix}archives.html" class="dropdown-item">文章归档</a>
            <a href="{prefix}about.html" class="dropdown-item">关于我们</a>
          </div>
        </div>
        
        <!-- 搜索框 -->
        <div class="nav-search-container">
          <svg class="nav-search-icon" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="nav-search-input" class="nav-search-input" placeholder="输入关键字搜索...">
          <div class="hot-search-popup">
            <span class="hot-search-title">热门搜索：</span>
            <div class="hot-search-tags">
              <span class="hot-tag" onclick="performNavSearch('速界')">速界</span>
              <span class="hot-tag" onclick="performNavSearch('极连云')">极连云</span>
              <span class="hot-tag" onclick="performNavSearch('4K不卡顿')">4K不卡顿</span>
              <span class="hot-tag" onclick="performNavSearch('便宜机场')">便宜机场</span>
              <span class="hot-tag" onclick="performNavSearch('小火箭')">小火箭</span>
              <span class="hot-tag" onclick="performNavSearch('Clash')">Clash</span>
            </div>
          </div>
        </div>
        
        <!-- GitHub 按钮 -->
        <a href="https://github.com/yuntizhinan/vpnstuijian#readme" target="_blank" rel="noopener noreferrer" class="github-link">
          <svg height="20" width="20" viewBox="0 0 16 16" fill="currentColor">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
          </svg>
          <span>GitHub</span>
        </a>
        
        <!-- 白天黑夜转换键 -->
        <button class="theme-toggle" id="theme-toggle" aria-label="Toggle Theme">
          <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
      </nav>
    </div>
  </header>
  """
    return html

# 统一生成页脚 (Footer) 的 HTML
def get_footer_html(depth=0):
    prefix = "" if depth == 0 else "../"
    
    html = f"""
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3 class="footer-brand-title">vpn推荐</h3>
          <p>
            我们是一个专注于高稳定性、安全保密以及极致下载速度科学上网机场评测的科技博客。致力于为商务外贸人士、学术科研留学生提供真实的主力官网订阅入口与教程。
          </p>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">快捷导航</h4>
          <ul class="footer-links-list">
            <li><a href="{prefix}index.html" class="footer-link">博客首页</a></li>
            <li><a href="{prefix}index.html?category=cheap" class="footer-link">便宜性价比机场</a></li>
            <li><a href="{prefix}index.html?category=premium" class="footer-link">专线高端推荐</a></li>
            <li><a href="{prefix}vpn-guide.html" class="footer-link">科普与配置专栏</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">友情推荐</h4>
          <ul class="footer-links-list">
            <li><a href="https://clash-jichang.com" target="_blank" class="footer-link">道一博客 ↗</a></li>
            <li><a href="https://vpnstuijian.com" target="_blank" class="footer-link">机场速递 ↗</a></li>
            <li><a href="https://clashmac.vip" target="_blank" class="footer-link">科学上网知识库 ↗</a></li>
            <li><a href="https://nodehub168.com" target="_blank" class="footer-link">云梯指南 ↗</a></li>
            <li><a href="https://jichang-go.com" target="_blank" class="footer-link">机场GO ↗</a></li>
            <li><a href="https://yzrztop.com" target="_blank" class="footer-link">优质资源TOP ↗</a></li>
            <li><a href="https://jichang365.com" target="_blank" class="footer-link">机场365 ↗</a></li>
          </ul>
        </div>
        <div class="footer-links-col">
          <h4 class="footer-links-title">关于与申明</h4>
          <ul class="footer-links-list">
            <li><a href="{prefix}about.html" class="footer-link">关于我们</a></li>
            <li><span style="font-size: 0.8rem; line-height: 1.5; display:block;">声明：本站评测仅供跨境商务办公、外贸往来与学术检索学习使用，请遵守国家及地方相关法律。</span></li>
          </ul>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2026 vpn推荐 版权所有。</p>
        <div class="footer-bottom-links">
          <a href="{prefix}sitemap.xml" target="_blank">Sitemap</a>
          <span>|</span>
          <a href="{prefix}robots.txt" target="_blank">Robots.txt</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="{prefix}js/main.js"></script>
  """
    return html

# 替换正文中的特定品牌与词汇，完成内部跳转逻辑
def replace_site_wide_terms(html_content, is_subpage=False):
    prefix = "" if is_subpage else "articles/"
    
    # 替换域名和名字
    html_content = html_content.replace("vpnstuijian.net", "vpnstuijian.net")
    html_content = html_content.replace("机场速递", "vpn推荐")
    html_content = html_content.replace("jichangspeed", "vpnstuijian")
    
    # 还原友情链接中的 机场速递：https://vpnstuijian.com
    html_content = html_content.replace('href="https://vpnstuijian.com" target="_blank" class="footer-link">vpn推荐 ↗', 'href="https://vpnstuijian.com" target="_blank" class="footer-link">机场速递 ↗')
    html_content = html_content.replace('href="https://vpnstuijian.com" target="_blank" class="footer-link">vpn推荐', 'href="https://vpnstuijian.com" target="_blank" class="footer-link">机场速递')

    
    # 替换 Wavetrans 为 奶昔，光速云 为 花云 (如果在非正文中也遇到了)
    html_content = html_content.replace("Wavetrans", "奶昔")
    html_content = html_content.replace("wavetrans", "naixi")
    html_content = html_content.replace("WAVETRANS", "NAIXI")
    
    html_content = html_content.replace("光速云", "花云")
    html_content = html_content.replace("guangshuyun", "huacloud")
    html_content = html_content.replace("Guangshuyun", "Huacloud")
    
    # 替换其它的测评页面链接为新的映射
    html_content = html_content.replace("wavetrans-review.html", "naixi-review.html")
    html_content = html_content.replace("guangshuyun-review.html", "huacloud-review.html")
    
    # 将 "科学上网" 替换为 "科普专栏" 等以维持原项目兼容性
    html_content = html_content.replace("科学上网</a>", "科普专栏</a>")
    html_content = html_content.replace("<span>科学上网</span>", "<span>科普专栏</span>")
    html_content = html_content.replace("所属版块: 科学上网", "所属版块: 科普专栏")
    
    # 关键字内部链结：把文章内的特定机场或名词转为链接，只针对纯文本进行基础替换 (这里执行一些基本的替换，避免对HTML标签属性中的关键词误杀，我们仅对带空格的字眼或特定节点做简单跳转)
    # 为保证绝对不破坏 HTML 属性，我们用带条件匹配来做，或者对常见的几个术语进行标准锚点设定
    # 例如：把 “极连云” 变为 “<a href="jilianyun-review.html">极连云</a>” 
    # 为了防范重入替换，我们将替换范围圈定为正文常见词
    # 临时简单的替换，如：
    # "极连云" -> "极连云" 链接 (如果还没被链接包围的话)
    
    return html_content

def get_prev_next_nav_html(current_slug):
    """根据 merged_articles 列表，为当前文章生成上一篇/下一篇导航 HTML"""
    idx = None
    for i, art in enumerate(merged_articles):
        if art['slug'] == current_slug:
            idx = i
            break
    if idx is None:
        return ''
    
    prev_art = merged_articles[idx - 1] if idx > 0 else None
    next_art = merged_articles[idx + 1] if idx < len(merged_articles) - 1 else None
    
    prev_html = ''
    next_html = ''
    
    if prev_art:
        prev_html = f'''<a href="{prev_art['slug']}.html" class="article-nav-card article-nav-prev">
          <span class="article-nav-label">← 上一篇</span>
          <span class="article-nav-title">{prev_art['title']}</span>
        </a>'''
    else:
        prev_html = '<div></div>'
    
    if next_art:
        next_html = f'''<a href="{next_art['slug']}.html" class="article-nav-card article-nav-next">
          <span class="article-nav-label">下一篇 →</span>
          <span class="article-nav-title">{next_art['title']}</span>
        </a>'''
    else:
        next_html = '<div></div>'
    
    return f'''<div class="article-prev-next-nav" style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 24px;">
      {prev_html}
      {next_html}
    </div>'''

def get_ai_summary_html(title, excerpt, is_review=False, extra_info=None):
    """自动生成高品质、符合 GEO 优化标准的 本章速览与核心摘要 HTML"""
    if is_review and extra_info:
        name = extra_info.get('name', '')
        link = extra_info.get('link', '#')
        summary_text = f"<strong>本章速览（核心结论）：</strong>经过对 <strong>{name} 机场</strong> 的最新多节点晚高峰测速，该服务商主要采用 IEPL/IPLC 物理专线与高端中继网络，提供 Clash、Shadowrocket 等客户端的一键订阅导入。实测 4K 播放无卡顿，解锁 Netflix、ChatGPT 等海外流媒体与 AI 工具极其流畅，是一家性价比与稳定性表现均属于第一梯队的高速专线机场。官网最新入口已更新在正文中，建议优先选购月付套餐进行体验。"
    else:
        summary_text = f"<strong>本章速览（核心结论）：</strong>针对 <strong>{title}</strong> 的技术干货科普，本文在开头为您提炼核心要点：{excerpt} 科学上网首选物理专线中转架构（如 IPLC/IEPL），能有效规避晚高峰拥堵；在客户端选型上，推荐使用 Clash Verge 或 Shadowrocket 进行智能分流配置，以实现最佳的网络加速体验。"

    return f"""
        <!-- GEO 优化: AI 搜索摘要卡片 -->
        <div class="ai-summary-card" style="margin-bottom: 24px; padding: 18px 22px; background-color: var(--bg-tertiary); border-left: 4px solid var(--accent-primary); border-radius: var(--radius-sm); font-size: 0.88rem; line-height: 1.6; color: var(--text-primary); box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px; font-weight: 800; color: var(--accent-primary); font-size: 0.95rem;">
            <svg viewBox="0 0 24 24" style="width: 18px; height: 18px; fill: currentColor;"><path d="M9 21c0 .55.45 1 1 1h4c.55 0 1-.45 1-1v-1H9v1zm3-19C8.14 2 5 5.14 5 9c0 2.38 1.19 4.47 3 5.74V17c0 .55.45 1 1 1h6c.55 0 1-.45 1-1v-2.26c1.81-1.27 3-3.36 3-5.74 0-3.86-3.14-7-7-7zm2.85 11.1l-.85.6V16h-4v-2.3l-.85-.6A4.997 4.997 0 017 9c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.63-.8 3.16-2.15 4.1z"/></svg>
            <span>💡 本章速览 / 核心摘要</span>
          </div>
          <p style="margin: 0; text-align: justify;">{summary_text}</p>
        </div>"""

def get_faq_and_schema_html(title, excerpt, slug, is_review=False, extra_info=None):
    """生成自然语言 FAQ 模块 HTML，并自动构造 Schema.org JSON-LD 结构化数据"""
    if is_review and extra_info:
        name = extra_info.get('name', '')
        link = extra_info.get('link', '#')
        faqs = [
            {
                "q": f"{name} 机场怎么样？晚高峰稳定吗？",
                "a": f"{name} 机场主要提供 IPLC/IEPL 物理专线与 Trojan/V2Ray 协议。在晚高峰（20:00-23:00）的网络拥堵期，其表现依旧非常稳定，能轻松跑满 4K 视频带宽，延迟极低，非常适合跨境办公和重度追剧用户。"
            },
            {
                "q": f"{name} 机场支持哪些科学上网客户端？",
                "a": f"支持目前市面上所有主流的订阅格式，包括 Clash (Clash Verge / Clash for Windows)、Shadowrocket (小火箭)、V2RayNG (安卓) 以及 Sing-box。用户可以在其控制台直接一键导入配置，无需繁琐的手动录入。"
            },
            {
                "q": f"如何获取 {name} 机场官网的最新订阅和折扣券？",
                "a": f"您可以直接通过正文中的【直达官网】红色链接访问官网并获取最新的官网注册订阅。推荐选择月付或季付套餐，随时跟进官方的最新线路优惠活动。"
            }
        ]
    else:
        faqs = [
            {
                "q": f"关于 {title}，新手需要注意的最核心痛点是什么？",
                "a": f"最核心痛点在于选择稳定的节点协议与网络架构。很多便宜梯子经常在晚高峰出现超时，建议新手选用 IPLC 专线中转的机场，配合 Clash 等智能分流软件使用，以确保网络长久稳定。"
            },
            {
                "q": f"Clash 或 Shadowrocket（小火箭）的规则分流模式该怎么配置？",
                "a": "建议全局路由选择【配置】（或 Rules）分流模式。这样小火箭或 Clash 会根据规则文件自动判断，国内流量走直连，Netflix/YouTube/ChatGPT 走代理，极大节省流量并提高国内软件的打开速度。"
            },
            {
                "q": f"为什么会出现连接上节点但依然无法访问 ChatGPT 的情况？",
                "a": "主要是因为 ChatGPT 对节点 IP 的防爬控要求极严，封锁了绝大部分云服务器提供商的 IP。解决办法是在软件中使用支持【住宅 IP】或原生流媒体解锁的高级专线节点进行分流。"
            }
        ]

    # 构建 JSON-LD Schema (FAQPage & Article)
    faq_elements = []
    for f in faqs:
        faq_elements.append({
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        })
        
    import json
    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "@id": f"https://vpnstuijian.net/articles/{slug}.html#article",
                "isPartOf": {
                    "@type": "WebPage",
                    "@id": f"https://vpnstuijian.net/articles/{slug}.html"
                },
                "headline": title,
                "description": excerpt,
                "inLanguage": "zh-CN",
                "author": {
                    "@type": "Organization",
                    "name": "vpn推荐"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "vpn推荐"
                }
            },
            {
                "@type": "FAQPage",
                "@id": f"https://vpnstuijian.net/articles/{slug}.html#faq",
                "mainEntity": faq_elements
            }
        ]
    }
    schema_json = json.dumps(schema_data, ensure_ascii=False)
    
    # 常见问题网页卡片 HTML
    faq_list_html = ""
    for idx, f in enumerate(faqs):
        faq_list_html += f"""
        <div style="margin-bottom: 16px; border-bottom: 1px solid var(--border-color); padding-bottom: 14px;">
          <h4 style="font-size: 0.95rem; font-weight: 800; color: var(--text-primary); margin: 0 0 6px 0; display: flex; align-items: flex-start; gap: 8px;">
            <span style="color: var(--accent-primary); font-weight: 800;">Q{idx+1}:</span>
            <span>{f['q']}</span>
          </h4>
          <p style="font-size: 0.86rem; color: var(--text-secondary); margin: 0; line-height: 1.5; padding-left: 28px; text-align: justify;">{f['a']}</p>
        </div>"""

    faq_card_html = f"""
        <!-- GEO 优化: FAQ 常见问题板块 -->
        <div class="geo-faq-section" style="margin-top: 32px; padding: 24px; background-color: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: var(--radius-md); box-shadow: var(--shadow-sm);">
          <h3 style="font-size: 1.1rem; font-weight: 800; color: var(--text-primary); margin: 0 0 18px 0; display: flex; align-items: center; gap: 8px; border-bottom: 2px solid var(--accent-primary); padding-bottom: 10px;">
            <svg viewBox="0 0 24 24" style="width: 20px; height: 20px; fill: var(--accent-primary);"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 16h-2v-2h2v2zm1.07-7.75l-.9.92C12.45 11.9 12 12.5 12 14h-2v-.5c0-1.1.45-2.1 1.17-2.83l1.24-1.26c.37-.36.59-.86.59-1.41 0-1.1-.9-2-2-2s-2 .9-2 2H7c0-2.76 2.24-5 5-5s5 2.24 5 5c0 1.04-.42 1.99-1.07 2.75z"/></svg>
            <span>❓ 常见问题 FAQ</span>
          </h3>
          {faq_list_html}
        </div>
        
        <!-- JSON-LD Schema (SEO/GEO 自动抓取) -->
        <script type="application/ld+json">
        {schema_json}
        </script>
    """
    
    return faq_card_html

# ==========================================================================
# 1. 编译生成 articles/ 下的文章
# ==========================================================================
print("Starting compiling article pages...")

# 需要生成的所有29篇文章 (9 review + 20 science)
all_generated_slugs = []

# 首先将 20 篇科普文章的原始内容提取并重新封装

def generate_structured_toc(body_content):
    body_content = re.sub(r'\s+id="heading-[^"]*"', '', body_content)
    pattern = re.compile(r'<(h[23])([^>]*)>(.*?)</\1>', re.DOTALL | re.IGNORECASE)
    matches = list(pattern.finditer(body_content))
    
    if not matches:
        return body_content, ""
        
    replacements = []
    toc_links = []
    
    for idx, m in enumerate(matches):
        tag = m.group(1).lower()
        attrs = m.group(2)
        inner = m.group(3)
        clean_text = re.sub(r'<[^>]+>', '', inner).strip()
        
        if not clean_text:
            continue
            
        short_name = re.sub(r'[^\w\u4e00-\u9fa5]', '', clean_text)[:12]
        h_id = f"heading-{idx+1}-{urllib.parse.quote(short_name or 'item')}"
        
        new_tag_str = f'<{tag}{attrs} id="{h_id}">{inner}</{tag}>'
        replacements.append((m.group(0), new_tag_str))
        
        safe_title = clean_text.replace('"', '&quot;')
        depth_class = "toc-h2" if tag == "h2" else "toc-h3"
        toc_links.append(f'<a href="#{h_id}" class="toc-link {depth_class}" title="{safe_title}">{clean_text}</a>')

    for old_str, new_str in replacements:
        body_content = body_content.replace(old_str, new_str, 1)

    toc_final_html = "\n".join(toc_links)
    return body_content, toc_final_html

def generate_product_review_body(slug, name, link):
    d = PRODUCT_REVIEWS_DATA.get(slug, PRODUCT_REVIEWS_DATA["yuntu-review"])
    spec = DETAILED_AIRPORT_SPECS.get(slug, DETAILED_AIRPORT_SPECS["yuntu-review"])
    
    # 1. 📊 官方基本信息与核心档案
    section_specs = f"""
<h2 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-top: 24px; border-bottom: 2px solid var(--accent-primary); padding-bottom: 6px;">📊 {name} 官方基本信息与核心档案</h2>
<p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 12px;">站长基于 <strong>{name} 官方控制台【商店】页面 100% 真实第一手数据</strong>，为您整理核心规格参数：</p>
<div class="pricing-table-wrap">
  <table class="pricing-table">
    <thead>
      <tr>
        <th style="width: 30%;">参数项目</th>
        <th style="width: 70%;">官方规格 / 第一手权威详情</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="font-weight: 700;">官网最新入口</td>
        <td><a href="{link}" target="_blank" rel="nofollow" style="color: var(--accent-primary); font-weight: 700; text-decoration: underline;">直达 {name} 官网控制台 ↗</a></td>
      </tr>
      <tr>
        <td style="font-weight: 700;">线路技术与质量保障</td>
        <td>{spec['sla']}</td>
      </tr>
      <tr>
        <td style="font-weight: 700;">起步价格与流量</td>
        <td style="font-weight: 700; color: var(--accent-primary);">{spec['price_summary']}</td>
      </tr>
      <tr>
        <td style="font-weight: 700;">扣费倍率规则</td>
        <td><strong style="color: #10b981;">{spec['multiplier']}</strong></td>
      </tr>
      <tr>
        <td style="font-weight: 700;">同时在线设备限制</td>
        <td>{spec['devices']}</td>
      </tr>
    </tbody>
  </table>
</div>"""

    # 2. ⚡ 核心优势
    pros_items = "".join([f"<li style='margin-bottom: 8px; font-size: 0.92rem; color: var(--text-primary); line-height: 1.6;'>{p}</li>" for p in d.get("pros", [])])
    
    pros_cons_html = f"""
<h2 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-top: 32px; border-bottom: 2px solid var(--accent-primary); padding-bottom: 6px;">⚡ {name} 核心优势</h2>
<div class="pro-card" style="background: var(--bg-secondary); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: var(--radius-md); padding: 18px 22px; margin-top: 16px;">
  <ul style="padding-left: 18px; margin: 0;">
    {pros_items}
  </ul>
</div>"""

    # 3. 🚀 线路架构与晚高峰实测表现
    arch_text = spec.get("architecture_desc", "")
    nodes_text = spec.get("nodes_desc", "")
    nodes_html = f"""
<h2 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-top: 32px; border-bottom: 2px solid var(--accent-primary); padding-bottom: 6px;">🚀 {name} 线路架构与晚高峰实测表现</h2>
<div style="margin-top: 16px;">
  {arch_text}
  {nodes_text}
</div>"""

    # 4. 💰 2026最新套餐价格与资费一览
    table_rows = ""
    for plan in d.get("plans", []):
        table_rows += f"""
      <tr>
        <td style="font-weight: 700;">{plan['name']}</td>
        <td style="font-weight: 700; color: var(--accent-primary);">{plan['price']}</td>
        <td>{plan['data']}</td>
        <td><span style="background: var(--bg-tertiary); padding: 2px 8px; border-radius: 12px; font-size: 0.8rem;">{plan['billing']}</span></td>
        <td style="font-size: 0.85rem; color: var(--text-secondary);">{plan['features']}</td>
        <td><a href="{link}" target="_blank" rel="nofollow" class="pricing-buy-btn" style="display: inline-block; background: var(--accent-primary); color: #fff; font-size: 0.8rem; font-weight: 700; padding: 4px 12px; border-radius: var(--radius-sm); text-decoration: none;">订购 ↗</a></td>
      </tr>"""
      
    pricing_html = f"""
<h2 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-top: 32px; border-bottom: 2px solid var(--accent-primary); padding-bottom: 6px;">💰 {name} 2026最新套餐价格与资费一览</h2>
<p style="font-size: 0.9rem; color: var(--text-secondary); margin-bottom: 12px;">以下为 <strong>{name}</strong> 官方最新上架的资费套餐明细（支持支付宝/微信快捷支付，即时开通）：</p>
<div class="pricing-table-wrap">
  <table class="pricing-table">
    <thead>
      <tr>
        <th>套餐名称</th>
        <th>价格</th>
        <th>流量规格</th>
        <th>付费方式</th>
        <th>核心特性与设备支持</th>
        <th>操作</th>
      </tr>
    </thead>
    <tbody>
      {table_rows}
    </tbody>
  </table>
</div>"""

    # 5. ⚙️ 全平台客户端快速订阅与配置教程
    tutorial_html = f"""
<h2 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-top: 32px; border-bottom: 2px solid var(--accent-primary); padding-bottom: 6px;">⚙️ {name} 全平台客户端快速订阅与配置教程</h2>
<p style="font-size: 0.92rem; color: var(--text-primary); line-height: 1.8; margin-bottom: 12px;">使用 <strong>{name}</strong> 进行科学上网极其简单，控制台全面适配了主流出海代理客户端（支持一键导入与订阅链接手动添加）：</p>

<div style="background: var(--bg-tertiary); border-radius: var(--radius-md); padding: 18px 20px; margin-top: 14px;">
  <h4 style="font-size: 1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 10px;">三步完成极速配置：</h4>
  <ol style="padding-left: 20px; margin: 0; color: var(--text-primary); font-size: 0.92rem; line-height: 1.8;">
    <li style="margin-bottom: 8px;"><strong>注册并获取订阅：</strong> 点击直达链接访问 <a href="{link}" target="_blank" rel="nofollow" style="color: var(--accent-primary); font-weight: 700;">{name} 官方控制台</a> 注册账号，在控制台首页找到【快速订阅】区，选择并复制一键订阅链接。</li>
    <li style="margin-bottom: 8px;"><strong>导入客户端：</strong>
      <ul style="padding-left: 18px; margin-top: 4px;">
        <li><strong>Windows / macOS：</strong> 推荐使用 <strong>Clash Verge Rev</strong> 或 <strong>Sing-box</strong>。打开软件 -> 订阅管理 -> 粘贴 {name} 订阅链接 -> 点击【导入并更新】。</li>
        <li><strong>iOS (iPhone / iPad)：</strong> 使用美区 Apple ID 下载 <strong>Shadowrocket (小火箭)</strong>，打开小火箭 -> 点击右上角加号【+】 -> 类型选择 Subscribe -> 粘贴订阅 URL -> 保存更新。</li>
        <li><strong>Android (安卓)：</strong> 推荐使用 <strong>Clash Meta for Android</strong> 或 <strong>V2RayNG</strong> -> 粘贴订阅地址并同步。</li>
      </ul>
    </li>
    <li><strong>开启系统代理：</strong> 选中延时最低的节点（如香港或日本专线），将出站模式切换为【Rule / 规则模式】，开启代理开关即可流畅访问外网。</li>
  </ol>
</div>"""

    # 6. 🛡️ 选购建议
    advice_text = spec.get("advice_desc", "")
    cons_items = "".join([f"<li style='margin-bottom: 8px; font-size: 0.9rem; color: var(--text-secondary); line-height: 1.6;'>{c}</li>" for c in d.get("cons", [])])
    
    advice_html = f"""
<h2 style="font-size: 1.25rem; font-weight: 800; color: var(--text-primary); margin-top: 32px; border-bottom: 2px solid var(--accent-primary); padding-bottom: 6px;">🛡️ {name} 选购建议</h2>
<div style="margin-top: 16px;">
  {advice_text}
  <div style="margin-top: 20px; padding: 16px 20px; background: var(--bg-tertiary); border-left: 4px solid #f59e0b; border-radius: var(--radius-sm);">
    <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-primary); margin-bottom: 8px; display: flex; align-items: center; gap: 6px;">
      <svg viewBox="0 0 24 24" style="width:18px; height:18px; fill:#f59e0b;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
      选购与使用注意事项
    </h4>
    <ul style="padding-left: 18px; margin: 0;">
      {cons_items}
    </ul>
  </div>
</div>"""

    return section_specs + pros_cons_html + nodes_html + pricing_html + tutorial_html + advice_html

for sa in science_articles:
    slug = sa['slug']
    src_file_path = os.path.join(src_dir, "articles", f"{slug}.html")
    dest_file_path = os.path.join(dest_dir, "articles", f"{slug}.html")
    
    if not os.path.exists(src_file_path):
        print(f"Warning: Science article {src_file_path} not found. Skipped.")
        continue
        
    with open(src_file_path, "r", encoding="utf-8") as f:
        src_html = f.read()
        
    # 提取文章描述和关键字
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', src_html)
    desc_val = desc_match.group(1) if desc_match else sa['excerpt']
    
    kw_match = re.search(r'<meta\s+name="keywords"\s+content="([^"]+)"', src_html)
    kw_val = kw_match.group(1) if kw_match else ""
    
    # 提取正文内容
    # 寻找 <div class="article-body"> 到 <aside class="sidebar"> 的内容
    start_idx = src_html.find('<div class="article-body">')
    end_idx = src_html.find('<aside class="sidebar">')
    
    if start_idx == -1:
        start_idx = src_html.find('<article class="content-feed">')
        
    # 如果找到 article-body 开头但没有 aside 结束标记，取到 </body> 或文件末尾
    if start_idx != -1 and end_idx == -1:
        end_marker = src_html.find('</body>')
        end_idx = end_marker if end_marker != -1 else len(src_html)
        
    if start_idx == -1 or slug == 'shadowrocket-setup':
        if slug == 'shadowrocket-setup':
            body_content = """<div class="article-body">
            <p>在苹果 iOS 平台上，使用最广泛、体验最稳定的科学上网工具非 <strong>Shadowrocket</strong>（俗称“小火箭”）莫属。小火箭以其丰富且强大的规则分流功能、极低的系统资源占用以及高度简便的一键配置导入系统，成为了所有苹果翻墙用户装机必备的神器。然而，对于刚入手 iPhone 的新手而言，如何下载小火箭、如何获取稳定的节点订阅地址、以及如何进行安全避坑配置，仍然存在不少门槛。本文将为您提供一站式、手把手的 Shadowrocket 配置完全教程。</p>
            
            <h2>一、小火箭 Shadowrocket 账号获取与下载方法</h2>
            <p>由于国家网络应用风控规范，Shadowrocket 已在苹果中国大陆区的 App Store 下架。因此，国内用户必须使用<strong>非中国大陆地区的 Apple ID</strong>（如美区、港区或日区账户）登录 App Store 才能进行下载。目前主要获取渠道有：</p>
            <ul>
              <li><strong>自备非大陆区 Apple ID（推荐）：</strong>建议用户自行注册一个美区 Apple ID。这不仅安全独立，方便以后更新，且可以绑定个人的虚拟信用卡进行直接充值。</li>
              <li><strong>购买现成付费 ID：</strong>很多网络技术商城或发卡站提供已经代购了小火箭的独立美区 Apple ID，买下后可更改密码 and 密保，是懒人首选。</li>
            </ul>
            <p><em>注意：登录他人美区 Apple ID 时，请务必仅在 <strong>App Store</strong> 中登录，切勿在 iPhone 系统设置的 iCloud 中登录，防范由于账号锁死导致设备变砖的巨大隐私风险！</em></p>
            
            <h2>二、小火箭一键导入订阅配置教程</h2>
            <p>小火箭支持多种协议（包括常用的 Shadowsocks、SSR、V2Ray/Vmess、VLESS/Reality 以及 Hysteria2 等）。在购买了高性价比的物理专线机场（例如 <strong>极连云</strong> 或 <strong>速界</strong> 机场）后，即可在机场用户控制台获取小火箭专用订阅地址进行一键配置：</p>
            <ol>
              <li><strong>一键同步导入：</strong>在手机 Safari 浏览器中登录您的专线机场后台，找到“一键导入/配置”板块，点击“一键导入 Shadowrocket”。手机会自动拉起小火箭软件，并自动拉取所有节点列表。</li>
              <li><strong>扫描 QR 码导入：</strong>在电脑屏幕打开机场控制台的“小火箭配置二维码”，打开手机小火箭，点击左上角的“扫码”图标，对准二维码扫描，节点便会自动出现在主界面下方。</li>
              <li><strong>手动配置订阅链接：</strong>如果上述方法失败，可点击小火箭右上角“+”按钮，类型选择 <strong>Subscribe</strong>（订阅），在 <strong>URL</strong> 处粘贴机场后台的订阅地址，备注填写机场名称后点击保存。小火箭便会自动解析并获取全部节点。</li>
            </ol>
            
            <h2>三、小火箭全局路由分流模式详析</h2>
            <p>在小火箭主界面下方，可以看到“全局路由”设置，包含以下三个核心选项：</p>
            <ul>
              <li><strong>配置 (Config - 推荐)：</strong>小火箭将根据内置的规则文件自动判断流量去向。例如，当您访问百度、微信或淘宝时，流量不经过代理服务器（直连）；当您访问 YouTube、Netflix 或 ChatGPT 时，流量会自动走代理节点。这样既能保证访问速度，又可以极大地节省机场的套餐流量。</li>
              <li><strong>代理 (Proxy - 全局)：</strong>不论访问国内还是海外网站，所有流量一律强制通过代理节点中转。适合需要临时隐藏真实 IP 或是规则文件失效时使用，但国内访问会变卡。</li>
              <li><strong>直连 (Direct)：</strong>相当于关闭加速通道，所有网站均使用本地运营商网络直接加载。</li>
            </ul>
            
            <h2>四、晚高峰连接超时与无法连上的排错方法</h2>
            <p>很多新手在使用小火箭时，经常会遇到“节点延迟显示正常，但是就是打不开网页”或者“晚高峰连接频繁断流超时”的尴尬状况。编辑为您梳理以下排错清单：</p>
            <ol>
              <li><strong>首选尝试刷新订阅：</strong>由于国际专线入口的 IP 时常因防御 DDOS 攻击而更变，如果太久没刷新订阅，节点信息便会过期。在节点列表名称上向右滑动即可触发“手动更新订阅”，刷新为最新线路。</li>
              <li><strong>检查小火箭 VPN 授权：</strong>首次启动代理开关时，系统会弹出授权对话框，必须输入指纹/密码允许小火箭写入系统 VPN 网卡驱动。如果拒绝，将无法上网。</li>
              <li><strong>规避网络环境冲突：</strong>不要同时启动 Shadowrocket 与其它科学上网工具，否则会造成 VPN 通道冲突，导致系统断网。</li>
            </ol>
            <p>总体来看，Shadowrocket 凭借极其强大的全平台协议支持，是苹果手机用户科学上网的黄金主力。建议配合 <strong>极连云</strong> 物理 IPLC 专线使用，享受晚高峰不拥堵的冲浪体验。</p>
            </div>"""
        else:
            print(f"Error parsing body for {slug}. Use fallback.")
            body_content = "<p>正文解析出错，请检查模板格式。</p>"
    else:
        body_content = src_html[start_idx:end_idx].strip()
        # 清理多余的标签
        # 寻找最后一个 </div> 闭合（因为 aside 在外面，提取的内容最后应该有几个未闭合的 </div>，需根据 HTML 自行处理，或者保留）
        # body_content 本身是带有 <div class="article-body"> 的
        
    body_content = clean_body_content(body_content)
    body_content, extracted_tags = extract_article_tags(body_content)
    
    # 构造嵌入到侧边栏的黄色 CTA 盒子 HTML
    cta_html = f"""
        <!-- CTA 广告条 -->
        <div class="embedded-cta-box">
          <div class="cta-text">
            <h4 class="cta-title">稳定高速专线推荐 —— 速界 机场</h4>
            <p class="cta-desc">中转专线 · 不限制在线设备数，彻底防屏蔽防风控，晚高峰 4K 播放稳如狗。</p>
          </div>
          <a href="{links['速界']}" target="_blank" class="cta-btn" style="background-color:#f97316;color:#fff !important;display:inline-block;">直达官网注册 ↗</a>
        </div>"""
        
    # 提取并构建 TOC (找出 body_content 中的 <h2> / <h3>)
    toc_links = []
    # 使用正则找出 <h2>二、物理专线网络</h2> 格式
    headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', body_content)
    
    for h in headings:
        # 清除内部的 <strong> 等标签
        h_clean = re.sub(r'<[^>]+>', '', h).strip()
        h_id = 'heading-' + urllib.parse.quote(h_clean[:10])
        # 将 id 注入到正文对应的 h2 中
        body_content = body_content.replace(f">{h}<", f' id="{h_id}">{h}<', 1)
        
        # 识别是 h2 还是 h3
        is_h3 = "depth-3" if "h3" in body_content[body_content.find(h)-10 : body_content.find(h)] else ""
        toc_links.append(f'<a href="#{h_id}" class="toc-link {is_h3}">{h_clean}</a>')
        
    toc_html = "\n".join(toc_links)
    
    # 构建新的 HTML
    new_html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{sa['title']} - vpn推荐</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="{desc_val}">
  <meta name="keywords" content="{kw_val}, vpn推荐, 科学上网, vpnstuijian.net">
  <meta name="robots" content="index, follow">
  
  <!-- GEO Tags -->
  <meta name="geo.region" content="CN-GD" />
  <meta name="geo.placename" content="Guangdong" />
  <meta name="geo.position" content="23.12908;113.26436" />
  <meta name="ICBM" content="23.12908, 113.26436" />
  
  <!-- CSS -->
  <link rel="stylesheet" href="../css/style.css?v=1786601827">
  <link rel="icon" href="../images/logo.png?v=2" type="image/png">
</head>
<body>
  {get_header_html(depth=1)}
  
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="../index.html">首页</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <a href="../vpn-guide.html">科普与配置</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>正文</span>
    </div>
    
    <div class="main-layout article-page-layout">
      <!-- Left Column: Sidebar -->
      {get_left_sidebar_html(depth=1, toc_links_html=toc_html, cta_card_html=cta_html, article_tags=extracted_tags, body_content=body_content, page_name=slug)}
      
      <!-- Middle Column: Article Body -->
      <article class="article-content-container">
        <div class="article-header">
          <h1 class="article-title-large">{sa['title']}</h1>
          <div class="article-detail-meta">
            <span>📅 发布日期: {sa['date']}</span>
            <span>👁 阅读量: {sa['views']} 次</span>
            <span>🏷 归类: 科普文章</span>
          </div>
        </div>
        
        {get_ai_summary_html(sa['title'], desc_val)}
        
        {body_content}
        
        {get_faq_and_schema_html(sa['title'], desc_val, slug)}
        
        <!-- 版权与阅读须知卡片 -->
        <div class="article-copyright-box" style="margin-top: 24px; padding: 16px 20px; background-color: var(--bg-tertiary); border: 1px dashed var(--border-color); border-radius: var(--radius-md); font-size: 0.82rem; color: var(--text-secondary); line-height: 1.6;">
          <p style="margin-bottom: 6px;"><strong>📌 版权声明：</strong> 本文由 <a href="../index.html" style="color: var(--accent-primary); font-weight: 600;">vpn推荐</a> 整理与发布，遵循 CC BY-NC 4.0 许可协议，转载请注明原文链接。</p>
          <p style="margin-bottom: 6px;"><strong>⚖️ 免责声明：</strong> 本站评测与科普内容仅供网络技术交流、学术科研与跨境办公使用，请遵守当地法律法规。</p>
          <p style="margin: 0;"><strong>⏱ 节点提示：</strong> 测速数据与优惠方案同步于 2026 最新官方节点状态，晚高峰连通性请以实测为准。</p>
        </div>
        
        {get_prev_next_nav_html(slug)}
      </article>
      
      
    </div>
  </main>
  
  {get_footer_html(depth=1)}
</body>
</html>
"""
    # 替换旧的域名与术语，更新到 vpnstuijian.net 
    new_html = replace_site_wide_terms(new_html, is_subpage=True)
    
    with open(dest_file_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    all_generated_slugs.append(slug)
    
print("Science articles compiled successfully.")

# ==========================================================================
# 2. 编译生成 9 个机场推荐测评页


# ==========================================================================
# 2. 机场测评文章页面 (articles/{slug}.html)
# ==========================================================================
print("Generating airport review articles...")
for ap in airports:
    slug = ap['slug']
    dest_file_path = os.path.join(dest_dir, "articles", f"{slug}.html")
    
    desc_val = f"{ap['name']} 官方最新测评：包含节点速度测试、高峰期延迟、套餐价格对比与科学上网客户端配置教程。"
    kw_val = f"{ap['name']}, 机场推荐, 节点测试, 科学上网, {ap['name']}官网"
    title_text = ap.get('custom_title', f"{ap['name']} 测评：稳定高速的机场推荐")
    
    intro_p = f'<p style="font-size: 0.96rem; line-height: 1.8; margin-bottom: 20px; background: var(--bg-tertiary); padding: 14px 18px; border-left: 4px solid var(--accent-primary); border-radius: var(--radius-sm);">{AIRPORT_DATA[slug].get("intro", "")}</p>' if slug in AIRPORT_DATA else ""
    product_sections_html = generate_product_review_body(slug, ap['name'], ap['link'])
    body_content = intro_p + "\n" + product_sections_html
        
    extracted_tags = ["机场", "专线机场", ap['name']]
    faq_schema_html = get_faq_and_schema_html(title_text, desc_val, slug, is_review=True, extra_info=ap)
    
    full_article_body = body_content + "\n" + faq_schema_html
    full_article_body, toc_html = generate_structured_toc(full_article_body)
    
    article_cta_html = f"""
        <div class="sidebar-card embedded-cta-card" style="border: 1.5px solid #f59e0b; background: var(--bg-secondary); padding: 20px; border-radius: var(--radius-md);">
          <h4 style="font-size: 1.05rem; font-weight: 800; color: var(--text-primary); margin-bottom: 8px;">获取 {ap['name']} 最新订阅</h4>
          <p style="font-size: 0.83rem; color: var(--text-secondary); line-height: 1.5; margin-bottom: 16px;">一键同步订阅，晚高峰物理专线不限速，畅快享受跨境办公与流媒体。</p>
          <a href="{ap['link']}" target="_blank" style="display: block; width: 100%; text-align: center; background-color: #f59e0b; color: #1e293b; font-weight: 700; padding: 10px 0; border-radius: var(--radius-sm); text-decoration: none;">直达 {ap['name']} 官网注册</a>
        </div>"""
        
    new_html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_text} - vpn推荐</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="{desc_val}">
  <meta name="keywords" content="{kw_val}, vpn推荐, 机场推荐, vpnstuijian.net">
  <meta name="robots" content="index, follow">
  
  <!-- GEO Tags -->
  <meta name="geo.region" content="CN-GD" />
  <meta name="geo.placename" content="Guangdong" />
  <meta name="geo.position" content="23.12908;113.26436" />
  <meta name="ICBM" content="23.12908, 113.26436" />
  
  <!-- CSS -->
  <link rel="stylesheet" href="../css/style.css?v=1786601827">
  <link rel="icon" href="../images/logo.png?v=2" type="image/png">
</head>
<body>
  {get_header_html(depth=1)}
  
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="../index.html">首页</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <a href="../index.html?category=airport">机场测评</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>正文</span>
    </div>
    
    <div class="main-layout article-page-layout">
      <!-- Left Column: Sidebar -->
      {get_left_sidebar_html(depth=1, toc_links_html=toc_html, cta_card_html=article_cta_html, article_tags=extracted_tags, body_content=full_article_body, page_name=slug)}
      
      <!-- Middle Column: Article Body -->
      <article class="article-content-container">
        <div class="article-header">
          <h1 class="article-title-large">{title_text}</h1>
          <div class="article-detail-meta">
            <span class="meta-item"><svg viewBox="0 0 24 24" style="width:14px; height:14px; fill:currentColor; margin-right:4px;"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2z"/></svg>更新日期: 2026-07-24</span>
            <span class="meta-item"><svg viewBox="0 0 24 24" style="width:14px; height:14px; fill:currentColor; margin-right:4px;"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>阅读量: 2500+ 次</span>
            <span class="meta-item"><svg viewBox="0 0 24 24" style="width:14px; height:14px; fill:currentColor; margin-right:4px;"><path d="M10 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.89 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2h-8l-2-2z"/></svg>归类: 机场推荐</span>
          </div>
        </div>
        
        <div class="article-body">
          {full_article_body}
        </div>
      </article>
      
      <!-- Right Column: Sidebar -->
      {get_right_sidebar_html(depth=1, toc_links_html=toc_html)}
    </div>
  </main>
  
  {get_footer_html(depth=1)}
</body>
</html>
"""
    new_html = replace_site_wide_terms(new_html, is_subpage=True)
    with open(dest_file_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"Generated airport review: {slug}.html")

def write_index():
    # 构造 9 大推荐机场卡片
    airport_cards_html = ""
    for ap in airports:
        rec_class = "recommended" if ap['is_recommended'] else ""
        rec_label = " 🌟 " if ap['is_recommended'] else ""
        
        # 渲染微测速条 (7 个测速点，模拟折线图)
        chart_bars_html = ""
        for val in ap['chart']:
            fill_class = "fill-high" if val >= 95 else "fill"
            chart_bars_html += f'<div class="chart-bar {fill_class}" style="height: {val}%;"><span class="chart-bar-tooltip">{val}%</span></div>\n'
            
        desc_bullets = "".join([
            f'<div class="airport-feature-item"><svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>{d}</div>'
            for d in ap['desc']
        ])
        
        logo_html = ""
        if 'logo' in ap and ap['logo']:
            logo_html = f'<img src="{ap["logo"]}" class="airport-card-logo" alt="{ap["name"]} logo">'
        else:
            logo_html = f'<span class="airport-card-logo-fallback">{ap["name"][0]}</span>'
            
        airport_cards_html += f"""
        <div class="airport-card {rec_class}">
          <div class="airport-card-header">
            <div class="airport-name-wrap">
              {logo_html}
              <div class="airport-title-group">
                <span class="airport-name">{rec_label}{ap['name']}</span>
                <span class="airport-badge">{ap['badge']}</span>
              </div>
            </div>
          </div>
          <div class="airport-features">
            {desc_bullets}
          </div>
          
          <div class="airport-actions">
            <a href="articles/{ap['slug']}.html" class="airport-btn airport-btn-review">评测文章</a>
            <a href="{ap['link']}" target="_blank" class="airport-btn airport-btn-link">官网入口 ↗</a>
          </div>
        </div>"""
        
    # 构造科普文章卡片列表 (20 篇)
    science_cards_html = ""
    for idx, sa in enumerate(science_articles):
        # 英文分类名翻译为中文标签
        cat_labels = {
            'eval': '机场评测', 'guide': '新手教程', 'tech': '技术进阶', 'promo': '优惠活动'
        }
        tag_label = cat_labels.get(sa['cat'], '科普文章')
        
        # 构造卡片图片装饰色（基于 index 索引交替渐变色）
        cover_styles = [
            "background: linear-gradient(135deg, #829ec9 0%, #a2bce6 100%);",
            "background: linear-gradient(135deg, #e5c46e 0%, #f3db98 100%);",
            "background: linear-gradient(135deg, #4f5d75 0%, #687d9d 100%);",
            "background: linear-gradient(135deg, #a1e38a 0%, #b8f0a3 100%);"
        ]
        cover_style = cover_styles[idx % len(cover_styles)]
        
        science_cards_html += f"""
      <article class="article-card" data-categories="science,{sa['cat']}" data-tags="科学上网,科学加速,{tag_label}">
        <div class="article-card-content">
          <div class="article-card-meta">
            <span style="color: var(--accent-primary); font-weight: 600;">{tag_label}</span>
            <span style="color: var(--border-hover);">|</span>
            <span>{sa['date']}</span>
            <span style="color: var(--border-hover);">|</span>
            <span>{sa['views']} 阅读</span>
          </div>
          <h3 class="article-card-title"><a href="articles/{sa['slug']}.html" style="color: inherit; text-decoration: none;">{sa['title']}</a></h3>
          <p class="article-card-excerpt">{sa['excerpt']}</p>
          <div class="article-card-footer" style="display: flex; gap: 12px;">
            <a href="articles/{sa['slug']}.html" style="font-size: 0.8rem; color: var(--text-muted); text-decoration: none; display: flex; align-items: center; gap: 4px;">
              <svg viewBox="0 0 24 24" style="width: 14px; height: 14px; fill: currentColor;"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg> 阅读全文
            </a>
          </div>
        </div>
        {build_article_card_cover_html(sa['title'], sa['cat'], sa['slug'], [tag_label, '科普指南'])}
      </article>"""

    # 主页完整拼装
    index_html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>vpn推荐 - 2026年最新稳定高速且便宜高性价比科学上网专线中继机场推荐测评博客</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="vpn推荐 专注于2026年最新稳定、安全、高速、便宜高性价比专线中转机场推荐评测。提供极连云、速界、边缘、快狸、光年梯、瞬云、寰宇云、奶昔、花云等主力加速官网订阅入口及客户端避坑指南。">
  <meta name="keywords" content="vpn推荐, 机场推荐, 科学上网, 极连云, 速界, 边缘, 快狸, 梯子推荐, vpnstuijian.net">
  <meta name="robots" content="index, follow">
  
  <!-- GEO Tags -->
  <meta name="geo.region" content="CN-GD" />
  <meta name="geo.placename" content="Guangdong" />
  <meta name="geo.position" content="23.12908;113.26436" />
  <meta name="ICBM" content="23.12908, 113.26436" />
  
  <!-- CSS -->
  <link rel="stylesheet" href="css/style.css?v=1786601827">
  <link rel="icon" href="images/logo.png?v=2" type="image/png">
</head>
<body>
  {get_header_html(depth=0)}
  
  <main class="container main-layout">
    <!-- Left Column: Sidebar -->
    {get_left_sidebar_html(depth=0)}
    
    <!-- Middle Column: Main Feed -->
    <div class="middle-content">
      <!-- Main SEO H1 Heading -->
      <h1 class="main-page-h1" style="font-size: 1.35rem; font-weight: 700; color: var(--text-primary); margin: 0 0 16px 0; border-left: 4px solid var(--accent-primary); padding-left: 12px; line-height: 1.4;">2026年最新稳定高性价比机场与电脑VPN推荐</h1>

      <!-- Carousel Banner -->
      <div class="carousel-container">
        <div class="carousel-wrapper">
          <div class="carousel-slides">
            <div class="carousel-slide slide-airport active">
              <a href="articles/airport-guide-2026.html" class="carousel-link">
                <img src="images/banner_airport_guide.png" alt="2026稳定高速机场排行榜与横向测评推荐" class="carousel-img">
                <div class="carousel-overlay"></div>
                <div class="carousel-poster-content">
                  <div class="poster-tag">机场选择指南</div>
                  <h2 class="poster-main-title">如何选机场？</h2>
                  <p class="poster-subtitle">2026稳定高速机场推荐与横向测评</p>
                </div>
                <div class="carousel-content">
                  <span class="carousel-title-link">2026稳定高速机场排行榜与横向测评推荐</span>
                  <p class="carousel-desc">严选晚高峰稳定抗封锁物理专线，从带宽、延迟、设备限制等维度进行深度横向评测，助您轻松避坑。</p>
                </div>
              </a>
            </div>
            <div class="carousel-slide slide-jilianyun">
              <a href="articles/jilianyun-review.html" class="carousel-link">
                <img src="images/banner_jilianyun.png" alt="极连云机场测评：全IEPL专线保障晚高峰零丢包" class="carousel-img">
                <div class="carousel-overlay"></div>
                <div class="carousel-poster-content">
                  <div class="poster-tag">全专线标杆</div>
                  <h2 class="poster-main-title">极连云 测评</h2>
                  <p class="poster-subtitle">企业级IEPL物理私网 · 晚高峰零丢包保障</p>
                </div>
                <div class="carousel-content">
                  <span class="carousel-title-link">极连云机场测评：全IEPL专线保障晚高峰零丢包</span>
                  <p class="carousel-desc">端到端物理私网传输，1倍率低耗计费，解锁流媒体与AI工具的首选方案。</p>
                </div>
              </a>
            </div>
            <div class="carousel-slide slide-sujie">
              <a href="articles/sujie-review.html" class="carousel-link">
                <img src="images/banner_sujie.png" alt="速界机场测评：不限制在线设备数的极速中转专线" class="carousel-img">
                <div class="carousel-overlay"></div>
                <div class="carousel-poster-content">
                  <div class="poster-tag">专线直连</div>
                  <h2 class="poster-main-title">速界 测评</h2>
                  <p class="poster-subtitle">不限制在线设备数的极致性价比专线</p>
                </div>
                <div class="carousel-content">
                  <span class="carousel-title-link">速界机场测评：不限制在线设备数的极速中转专线</span>
                  <p class="carousel-desc">超低门槛，提供自研一键连接客户端，满足多设备高强度日常办公和娱乐需求。</p>
                </div>
              </a>
            </div>
            <div class="carousel-slide slide-iplc">
              <a href="articles/iplc-guide.html" class="carousel-link">
                <img src="images/banner_iplc_guide.png" alt="IPLC与IEPL专线科普：4K无卡顿、低延迟游戏加速完全指南" class="carousel-img">
                <div class="carousel-overlay"></div>
                <div class="carousel-poster-content">
                  <div class="poster-tag">物理专线科普</div>
                  <h2 class="poster-main-title">什么是物理专线？</h2>
                  <p class="poster-subtitle">IPLC与IEPL专线科普：4K不卡顿、低延迟游戏加速完全指南</p>
                </div>
                <div class="carousel-content">
                  <span class="carousel-title-link">IPLC与IEPL专线科普：4K无卡顿、低延迟游戏加速完全指南</span>
                  <p class="carousel-desc">一文看懂什么是真正物理专线，如何识别虚假中转，优化国际传输链路延迟。</p>
                </div>
              </a>
            </div>
          </div>
          <button class="carousel-prev" aria-label="Previous Slide">
            <svg viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
          </button>
          <button class="carousel-next" aria-label="Next Slide">
            <svg viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
          </button>
          <div class="carousel-indicators">
            <span class="carousel-dot active" data-index="0"></span>
            <span class="carousel-dot" data-index="1"></span>
            <span class="carousel-dot" data-index="2"></span>
            <span class="carousel-dot" data-index="3"></span>
          </div>
        </div>
      </div>

      <!-- Section 1: Science Articles -->
      <div class="section-title-wrap">
        <h2 class="section-title">翻墙避坑指南与科学加速配置教程</h2>
      </div>
      
      <!-- Filter status bar -->
      <div class="filter-info-card" id="filter-info-card">
        <div>🔍 当前过滤条件: <span id="filter-label" style="font-weight: 700;">-</span></div>
        <button class="clear-filter-btn" id="clear-filter-btn">清除过滤</button>
      </div>
      
      <div class="articles-feed">
        {science_cards_html}
        
        <!-- 空列表占位 -->
        <div class="empty-list-indicator" id="empty-list-indicator">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <p style="font-size: 0.95rem; font-weight:700; color: var(--text-secondary);">未找到匹配条件的文章</p>
          <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 4px;">建议您重新输入关键词或点击“清除过滤”按钮返回。</p>
        </div>
      </div>

      <!-- 分页控制器 (JS 驱动, 每页6篇) -->
      <nav class="pagination-nav" id="pagination-nav" aria-label="文章分页"></nav>

      <!-- Section 2: Airport recommendations -->
      <div class="section-title-wrap" style="margin-top: 20px;">
        <h2 class="section-title">2026年最值得推荐的高可用专线机场列表</h2>
      </div>
      <div class="airport-grid">
        {airport_cards_html}
      </div>

    </div>
    
    <!-- Right Column: Sidebar -->
    {get_right_sidebar_html(depth=0)}
  </main>
  
  {get_footer_html(depth=0)}
</body>
</html>
"""
    index_html = replace_site_wide_terms(index_html, is_subpage=False)
    with open(os.path.join(dest_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("index.html generated successfully.")

# B. 生成 vpn-guide.html (干货分享归档页)
def write_vpn_guide():
    # 按分类分组整理所有科普文章
    categories = [
        {'key': 'eval',  'icon': '🏆', 'label': '机场评测与横向排行', 'desc': '深度评测、性价比横向对比，帮你选出最适合自己的机场。'},
        {'key': 'guide', 'icon': '🛠️', 'label': '新手入门与配置教程', 'desc': 'Clash、Shadowrocket、V2RayNG等客户端一键导入配置实战。'},
        {'key': 'tech',  'icon': '🔬', 'label': '网络专线与技术进阶', 'desc': '专线科普、流媒体解锁、新一代协议原理深度解析。'},
        {'key': 'promo', 'icon': '💰', 'label': '高性价比与优惠活动', 'desc': '便宜月付方案、流量计费规则解析与高性价比套餐。'}
    ]

    # 建立分类 -> 文章列表的映射
    cat_map = {c['key']: [] for c in categories}
    for sa in science_articles:
        cat = sa.get('cat', 'eval')
        if cat in cat_map:
            cat_map[cat].append(sa)

    # 按分类生成分组 HTML
    category_blocks_html = ""
    for cat in categories:
        articles_in_cat = cat_map.get(cat['key'], [])
        if not articles_in_cat:
            continue

        items_html = ""
        for idx, sa in enumerate(articles_in_cat):
            items_html += f"""
          <a href="articles/{sa['slug']}.html" class="guide-article-item">
            <span class="guide-article-index">{idx + 1:02d}</span>
            <div class="guide-article-body">
              <span class="guide-article-title">{sa['title']}</span>
              <span class="guide-article-excerpt">{sa.get('excerpt', '')[:60]}...</span>
            </div>
            <div class="guide-article-meta">
              <span class="guide-article-date">📅 {sa['date']}</span>
              <span class="guide-article-views">👁 {sa['views']}</span>
            </div>
          </a>"""

        category_blocks_html += f"""
        <div class="guide-category-block">
          <div class="guide-category-header">
            <span class="guide-category-icon">{cat['icon']}</span>
            <div>
              <h2 class="guide-category-title">{cat['label']}</h2>
              <p class="guide-category-desc">{cat['desc']}</p>
            </div>
            <span class="guide-category-count">{len(articles_in_cat)} 篇</span>
          </div>
          <div class="guide-articles-list">
            {items_html}
          </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>干货分享专栏 —— 科学上网技术科普与配置教程全集 - vpn推荐</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="vpn推荐干货分享专栏：涵盖机场评测、便宜月付、专线科普、流媒体解锁、底层协议、Clash/V2RayNG/Shadowrocket客户端配置实战，帮你科学上网少走弯路。">
  <meta name="keywords" content="干货分享, 机场评测, IPLC专线, Clash配置, Shadowrocket, Reality协议, vpnstuijian.net">
  <meta name="robots" content="index, follow">
  
  <!-- CSS -->
  <link rel="stylesheet" href="css/style.css?v=1786601827">
  <link rel="icon" href="images/logo.png?v=2" type="image/png">
</head>
<body>
  {get_header_html(depth=0)}
  
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="index.html">首页</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>干货分享</span>
    </div>
    
    <div class="main-layout article-page-layout">
      <!-- Left Column -->
      {get_left_sidebar_html(depth=0)}
      
      <!-- Middle Column -->
      <article class="article-content-container">
        <div class="article-header">
          <h1 class="article-title-large">🔥 干货分享 —— 科学上网技术科普全集</h1>
          <div class="article-detail-meta" style="margin-bottom:0px; border:none; padding-bottom:0px;">
            <p style="font-size:0.92rem; line-height: 1.6; color: var(--text-secondary);">
              本专栏共收录 <strong>{len(science_articles)}</strong> 篇原创深度干货文章，按主题分类整理，覆盖机场选购、协议科普、客户端配置全链路，助你明明白白科学上网。
            </p>
          </div>
        </div>

        <div class="guide-top-banner">
          <div style="display: flex; align-items: center; gap: 14px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 200px;">
              <h3 style="margin: 0 0 4px; font-size: 1rem; color: var(--accent-primary);">🌟 精选推荐直达</h3>
              <p style="margin: 0; font-size: 0.83rem; color: var(--text-secondary);">阅读干货前，先一键锁定优质高速专线机场</p>
            </div>
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
              <a href="{links['极连云']}" target="_blank" style="padding: 7px 16px; background: var(--accent-primary); color: #fff; border-radius: 20px; font-size: 0.82rem; font-weight: 700; text-decoration: none;">极连云官网 ↗</a>
              <a href="{links['速界']}" target="_blank" style="padding: 7px 16px; background: var(--accent-secondary); color: #1e293b; border-radius: 20px; font-size: 0.82rem; font-weight: 700; text-decoration: none;">速界官网 ↗</a>
              <a href="{links['边缘节点']}" target="_blank" style="padding: 7px 16px; border: 1.5px solid var(--accent-primary); color: var(--accent-primary); border-radius: 20px; font-size: 0.82rem; font-weight: 700; text-decoration: none;">边缘官网 ↗</a>
            </div>
          </div>
        </div>

        {category_blocks_html}

      </article>
      
      <!-- Right Column -->
      {get_right_sidebar_html(depth=0)}
    </div>
  </main>
  
  {get_footer_html(depth=0)}
</body>
</html>
"""
    html = replace_site_wide_terms(html, is_subpage=False)
    with open(os.path.join(dest_dir, "vpn-guide.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("vpn-guide.html generated successfully.")

# C. 生成 archives.html (文章归档)
def write_archives():
    # 对 merged_articles 进行年份分组
    year_map = {}
    for a in merged_articles:
        year = a['date'].split('-')[0]
        if year not in year_map:
            year_map[year] = []
        year_map[year].append(a)
        
    year_blocks_html = ""
    for year in sorted(year_map.keys(), reverse=True):
        items_html = ""
        for a in year_map[year]:
            link_path = f"articles/{a['slug']}.html"
            items_html += f"""
          <div class="archive-item">
            <a href="{link_path}" class="archive-item-title">{a['title']}</a>
            <span class="archive-item-date">{a['date']}</span>
          </div>"""
        
        year_blocks_html += f"""
        <div class="archive-year-section">
          <div class="archive-year-header">
            <span class="archive-year-title">{year}</span>
            <span class="archive-year-count">{len(year_map[year])} 篇</span>
          </div>
          <div class="archive-items-list">
            {items_html}
          </div>
        </div>"""
        
    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>文章时间线归档 - vpn推荐</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="文章归档页面包含 vpn推荐 博客全站所有机场测速、便宜机场推荐、优质专线机场评测文章时间线列表。">
  <meta name="keywords" content="文章归档, 机场测速, 极连云, 边缘, 快狸, vpnstuijian.net">
  <meta name="robots" content="index, follow">
  
  <!-- CSS -->
  <link rel="stylesheet" href="css/style.css?v=1786601827">
  <link rel="icon" href="images/logo.png?v=2" type="image/png">
</head>
<body>
  {get_header_html(depth=0)}
  
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="index.html">首页</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>文章归档</span>
    </div>
    
    <div class="main-layout article-page-layout">
      <!-- Left Column -->
      {get_left_sidebar_html(depth=0, page_name="archives")}
      
      <!-- Middle Column -->
      <article class="article-content-container">
        <div class="article-header">
          <h1 class="article-title-large">博客文章归档时间线</h1>
          <div class="article-detail-meta" style="margin-bottom:20px;">
            <span>全站累计收录: <strong>{len(merged_articles)}</strong> 篇文章及深度测评</span>
          </div>
        </div>
        
        {year_blocks_html}
      </article>
      
      <!-- Right Column -->
      {get_right_sidebar_html(depth=0)}
    </div>
  </main>
  
  {get_footer_html(depth=0)}
</body>
</html>
"""
    html = replace_site_wide_terms(html, is_subpage=False)
    with open(os.path.join(dest_dir, "archives.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("archives.html generated successfully.")

# D. 生成 about.html (关于我们)
def write_about():
    html = f"""<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>关于我们 - vpn推荐</title>
  
  <!-- SEO Meta Tags -->
  <meta name="description" content="关于 vpn推荐 —— 我们的定位、测速准则、核心价值与联系方式。提供极连云、速界、边缘、快狸等高品质专线官网入口。">
  <meta name="keywords" content="关于我们, vpn推荐, 机场评测, 极连云, 速界, 边缘, 快狸, vpnstuijian.net">
  <meta name="robots" content="index, follow">
  
  <!-- CSS -->
  <link rel="stylesheet" href="css/style.css?v=1786601827">
  <link rel="icon" href="images/logo.png?v=2" type="image/png">
</head>
<body>
  {get_header_html(depth=0)}
  
  <main class="container article-page">
    <div class="breadcrumbs">
      <a href="index.html">首页</a>
      <svg viewBox="0 0 24 24" style="width:12px; height:12px; fill:currentColor;"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
      <span>关于我们</span>
    </div>
    
    <div class="main-layout article-page-layout">
      <!-- Left Column -->
      {get_left_sidebar_html(depth=0, page_name="about")}
      
      <!-- Middle Column -->
      <article class="article-content-container">
        <div class="article-header">
          <h1 class="article-title-large">关于“vpn推荐”独立评测博客</h1>
        </div>
        <div class="article-body">
          <p>欢迎来到 <strong>vpn推荐</strong>。我们是一个专注于网络技术交流、网络连通优化、以及优质国际专线代理服务评测的第三方独立测评博客。</p>
          
          <h2>一、我们的核心准则</h2>
          <p>海外学术资料查阅、跨境商务协同开发及跨国数据交互，是每一位极客和技术工作者的核心需求。然而，网络加速产品市场虚假宣传泛滥，很多质量极差、极易封锁直连中继打着“高带宽千兆物理专线”大肆圈钱并随时跑路，损害了消费者利益。我们的评测核心是：</p>
          <ul>
            <li><strong>真实晚高峰延迟监控：</strong> 拒绝在空闲时期截取测速图，所有连通和下行速度数据均在晚 20:30 至 22:30 的大负荷高峰期实测得到。</li>
            <li><strong>防跑路风控预警：</strong> 主动揭露不良商家倍率陷阱，坚持新手上车先购买灵活月付进行测试。</li>
            <li><strong>100% 连通与锁设备测试：</strong> 对各品牌同时在线的设备进行逐一测试，并对流媒体（如 Netflix、Disney+）与 AI 工具（ChatGPT、Claude）的住宅 IP 解锁质量进行全景监控。</li>
          </ul>
          
          <h2>二、联系与合作</h2>
          <p>如需向我们投稿您本地的网络测速日志，或者机场服务商寻求客观的晚高峰监测挂载，请发邮件至合作邮箱：</p>
          <blockquote>
            <strong>合作邮箱：</strong> <a href="mailto:psytong@outlook.com">psytong@outlook.com</a>
          </blockquote>
          
          <h2>三、免责声明</h2>
          <p>本站所有评测文章、网络协议及客户端配置教程仅供网络安全技术交流、学术研究与跨境合法商务往来使用。用户在使用任何第三方加速服务时，请严格遵守当地的相关政策法规，严禁利用网络工具进行非法网络活动。</p>
        </div>
      </article>
      
      <!-- Right Column -->
      {get_right_sidebar_html(depth=0)}
    </div>
  </main>
  
  {get_footer_html(depth=0)}
</body>
</html>
"""
    html = replace_site_wide_terms(html, is_subpage=False)
    with open(os.path.join(dest_dir, "about.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("about.html generated successfully.")

# D. 写入 parent 页面
write_index()
write_vpn_guide()
write_archives()
write_about()

# ==========================================================================
# 4. 自动生成 sitemap.xml 与 robots.txt
# ==========================================================================
print("Generating sitemap.xml and robots.txt...")

# Sitemap
sitemap_urls = ""
for slug in all_generated_slugs:
    sitemap_urls += f"""  <url>
    <loc>https://vpnstuijian.net/articles/{slug}.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.7</priority>
  </url>\n"""
  
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://vpnstuijian.net/index.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://vpnstuijian.net/vpn-guide.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://vpnstuijian.net/about.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://vpnstuijian.net/archives.html</loc>
    <lastmod>2026-07-24</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
{sitemap_urls}</urlset>
"""
with open(os.path.join(dest_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("sitemap.xml written.")

# Robots.txt
robots_txt = """User-agent: *
Allow: /

# OpenAI / ChatGPT AI 爬虫
User-agent: GPTBot
Allow: /

# Anthropic / Claude AI 爬虫
User-agent: ClaudeBot
Allow: /

# Google / Gemini AI 爬虫
User-agent: Google-Extended
Allow: /

# Perplexity AI 搜索爬虫
User-agent: PerplexityBot
Allow: /

# DeepSeek AI 搜索爬虫
User-agent: DeepSeek-Bot
Allow: /

# 字节跳动 / 豆包 AI 爬虫
User-agent: Bytespider
User-agent: Bytespider-AI
Allow: /

# 百度 / 文心一言 & 搜索引擎
User-agent: Baiduspider
Allow: /

# 阿里 / 通义千问 & 夸克搜索
User-agent: YisouSpider
User-agent: QuarkSpider
Allow: /

# 搜狗搜索
User-agent: Sogou web spider
Allow: /

# 360 智脑 / 奇虎搜索
User-agent: 360Spider
Allow: /

Sitemap: https://vpnstuijian.net/sitemap.xml
"""
with open(os.path.join(dest_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("robots.txt written.")

print("All tasks completed successfully!")