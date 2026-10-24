# XXTPilot 官网

XXTPilot（学习通 AI 助手）的中文官网与使用文档，使用 MkDocs Material 构建。

- 官网：<https://xxtpilot.github.io/>
- 脚本源码：<https://github.com/zhu-hailin/chaoxing-ai-assistant>

## 本地预览

需要 Python 3.10 或更新版本。在本仓库运行：

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

打开终端中显示的本地地址。页面正文位于 `docs/`，导航与主题配置位于 `mkdocs.yml`，自定义样式位于 `docs/assets/stylesheets/extra.css`。

## 构建与发布

```sh
python -m mkdocs build --strict
python scripts/check_site.py
```

构建产物位于 `site/`。推送 `main` 后，GitHub Actions 自动构建并部署到 GitHub Pages；Pull Request 只构建检查。仓库 Settings → Pages 的发布来源使用 **GitHub Actions**。

## 内容维护

- 修改页面：直接编辑对应 Markdown 文件；新增页面后更新 `mkdocs.yml` 的 `nav`。
- 替换截图：更新 `docs/assets/images/` 中的截图并同步说明文字。`entry-original.png` 保留原始文件，页面展示的 `entry-page.svg` 仅裁掉外围背景，保留整个白色页面。
- 更新功能：先核对脚本源码，再修改使用指南；本地新增功能列入“近期进展”，公开版本日期以原项目 Releases 为准。
- 安装链接：始终指向原项目完整的 `学习通AI助手.user.js`，不在官网仓库分发源码片段。

官网不收集 API Key，不使用统计、广告或在线客服。截图由用户提供；产品源码与官网分别维护。
