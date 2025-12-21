# 个人主页网站

一个简洁、现代化的个人主页，采用纯 HTML + CSS + JavaScript 构建，专注于性能优化和用户体验。

## 🌐 在线预览

**主站:** https://950831.xyz/
**博客:** https://yangzhenai.top/

## ✨ 主要特性

### 🎨 设计特色
- 📱 **完全响应式设计** - 完美适配桌面端、平板和移动设备
- 🌓 **深色/浅色主题切换** - 支持系统主题自动检测和手动切换
- ✨ **流畅动画效果** - 页面加载淡入动画和滚动触发动画
- 🎯 **现代化 UI** - 采用卡片式设计，清晰的视觉层次

### ⚡ 性能优化
- 🖼️ **WebP 图片格式** - 相比 PNG/JPG 减少 90% 文件大小
- 📦 **图片懒加载** - 按需加载图片，提升首屏加载速度
- 🚀 **Cloudflare CDN** - 全球 CDN 加速，HTTPS 安全连接
- 💾 **浏览器缓存优化** - 静态资源缓存策略

### 🔍 SEO 优化
- 📊 **Google Analytics 集成** - 网站访问数据统计
- 🗺️ **结构化数据** - Schema.org JSON-LD 标记
- 📝 **完整的 Meta 标签** - Open Graph、Twitter Card 支持
- 🤖 **Sitemap 和 robots.txt** - 搜索引擎友好

### ♿ 无障碍性
- 🎯 **语义化 HTML** - 使用正确的 HTML5 标签
- ⌨️ **键盘导航支持** - 全站可通过键盘操作
- 📱 **移动端优化** - 触控友好的交互设计

## 🛠️ 技术栈

- **前端框架:** 无（原生 JavaScript，零依赖）
- **样式技术:** CSS3（Flexbox、Grid、CSS 变量）
- **图标库:** Font Awesome 6.0
- **部署平台:** Cloudflare Pages
- **CDN 服务:** Cloudflare
- **版本控制:** Git + GitHub

## 🚀 快速开始

### 本地运行

**方法 1: 直接打开**
```bash
# 直接用浏览器打开 index.html 文件
```

**方法 2: 使用 Python HTTP 服务器**
```bash
python -m http.server 8000
# 访问 http://localhost:8000
```

**方法 3: 使用 Node.js**
```bash
npx serve
# 或
npx http-server
```

### 部署到 Cloudflare Pages

1. Fork 本仓库到你的 GitHub 账号
2. 登录 [Cloudflare Pages](https://pages.cloudflare.com/)
3. 连接你的 GitHub 仓库
4. 选择本项目并部署
5. 添加自定义域名（可选）

推送到 GitHub 后会自动触发部署！

## 📁 项目结构

```
PersonalProfile/
├── index.html                 # 主页面（包含所有内容）
├── style.css                  # 样式文件
├── images/                    # 图片资源目录
│   ├── avatar.webp           # 头像（WebP 格式）
│   ├── avatar.png            # 头像（PNG 备份）
│   ├── *-icon.webp           # 各种图标（WebP 格式）
│   └── *-icon.png            # 图标（PNG 备份）
├── sitemap.xml               # 站点地图
├── robots.txt                # 搜索引擎爬虫配置
├── README.md                 # 项目说明文档
├── CHANGELOG.md              # 版本更新日志
└── convert_to_webp.py        # 图片格式转换工具
```

## 🎯 功能模块

### 1. 个人信息展示
- 头像、姓名、简介
- 主题切换按钮

### 2. 关于我
- 技能卡片展示
- 多列响应式布局

### 3. 社交媒体
- 微信公众号（二维码弹窗）
- 哔哩哔哩
- 小宇宙播客

### 4. 最新发布
- 博客文章列表
- 链接到外部博客

### 5. 作品展示
- 视频作品
- 图片作品
- 文章作品

### 6. 联系方式
- Gmail 邮箱
- 个人微信（复制功能）

## 🔧 自定义配置

### 修改个人信息

编辑 `index.html` 文件中的以下部分：

```html
<!-- 个人信息 -->
<h1 class="name">你的名字</h1>
<p class="subtitle">你的职位 · 你的标签</p>

<!-- Meta 标签 -->
<meta name="description" content="你的网站描述">
<meta name="author" content="你的名字">
```

### 修改主题颜色

编辑 `style.css` 文件中的 CSS 变量：

```css
:root {
    --primary-color: #your-color;
    --background-color: #your-color;
    /* ... */
}
```

### 添加 Google Analytics

替换 `index.html` 中的 GA 代码：

```javascript
gtag('config', 'YOUR-GA-ID');
```

## 📊 性能指标

- **Lighthouse 评分:** 90+ (性能、无障碍性、最佳实践、SEO)
- **首屏加载时间:** < 1s
- **页面大小:** < 500KB（包含所有资源）
- **图片优化:** 90% 压缩率（WebP）

## 🌍 浏览器支持

- ✅ Chrome (最新版本)
- ✅ Firefox (最新版本)
- ✅ Safari (最新版本)
- ✅ Edge (最新版本)
- ✅ 移动端浏览器

## 📝 更新日志

查看 [CHANGELOG.md](./CHANGELOG.md) 了解详细的版本更新历史。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

© 2025 - All rights reserved

---

**Built with ❤️ using Pure HTML, CSS & JavaScript**
