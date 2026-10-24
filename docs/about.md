---
title: 关于项目
description: 学习通AI助手 的项目来源、费用、数据处理、开源许可与问题反馈。
---

# 关于项目

学习通AI助手通过 Tampermonkey 在学习通网页内提供题目图文分析、原生答案预填及课程学习辅助。

[项目源码](https://github.com/zhu-hailin/chaoxing-ai-assistant)
[官网仓库](https://github.com/xxtpilot/xxtpilot.github.io)

## 免费与开源

脚本采用 **MIT 协议**免费提供。API Key 需自行准备，模型调用费用由所选服务商收取。

脚本字体解密基于 wyn665817 的“超星字体解密”，保留原作者署名和 MIT 许可。原项目中的第三方资源遵循各自许可与归属说明。

官网使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)，导航与文档布局参考 [Meta-Docs](https://github.com/MetaCubeX/Meta-Docs)。产品截图由用户提供。

## 数据如何处理

- 官网是静态文档，不提供账户系统，不收集 API Key，不接入统计、广告或在线客服。
- 脚本将 API Key 与学习开关保存在 Tampermonkey 存储中。
- 使用模型功能时，相关题目、材料及图片会按你的配置发送到所选服务商接口。
- 结果暂存、运行记录等以脚本提供的设置和操作为准。

官网保留主题选择等必要的浏览器本地偏好。通过外部链接访问 GitHub、Tampermonkey 或模型服务商后，适用相应网站的政策。

## 使用边界

本项目为第三方学习辅助工具，与超星、学习通及模型服务商无隶属关系。请遵守学校、课程和平台的使用要求。

AI 输出请自行核对。人脸识别、验证码与未适配内容交由人工处理；学习任务完成以平台标记为准。原项目提供了更详细的[使用风险说明](https://github.com/zhu-hailin/chaoxing-ai-assistant/blob/main/docs/%E8%84%9A%E6%9C%AC%E4%BD%BF%E7%94%A8%E9%A3%8E%E9%99%A9%E5%88%86%E6%9E%90%E6%8A%A5%E5%91%8A.md)。

## 反馈问题

功能、适配和脚本问题请提交到[原项目 Issues](https://github.com/zhu-hailin/chaoxing-ai-assistant/issues)。建议附上：

1. 脚本版本和使用的浏览器。
2. 页面类型、操作步骤与实际提示。
3. 遮挡账号、课程链接敏感参数及 API Key 后的截图。

官网文案或链接问题，可在[官网仓库](https://github.com/xxtpilot/xxtpilot.github.io)提交 Issue 或 Pull Request。

## 持续更新

官网正文使用 Markdown 维护，随源码功能变化补充说明与截图。脚本发行版和官网部署分别管理，更新信息见[更新日志](changelog.md)。
