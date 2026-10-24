---
title: 学习通AI助手
hide:
  - navigation
  - toc
---

# <img src="assets/images/logo.png" alt="" width="24" height="24" /> 学习通AI助手

在学习通网页中提供题目分析、答案预填和课程学习辅助，通过 Tampermonkey 使用。

[安装脚本](install.md) · [使用指南](guide/index.md) · [GitHub](https://github.com/zhu-hailin/chaoxing-ai-assistant)

## 主要功能

- **题目与答案**：提取测验、作业的文字和图片，调用模型分析，核对后预填答案。
- **课程学习**：处理视频、资料和章节测验，跳过已学内容，查看未完成任务。
- **课程队列**：勾选课程，按列表顺序逐门处理；从具体课程开始时只处理本课程。
- **章节目录**：查看完成状态，搜索章节，定位未完成任务。
- **模型配置**：使用自己的 API Key，支持预设服务商和 OpenAI 兼容接口。
- **其他工具**：学习休息、视频间隔、倍速、课程菜单管理和窗口调整。

## 开始使用

1. 安装 Tampermonkey，再安装完整用户脚本。
2. 打开学习通，在助手的“模型设置”中填写 API Key 并选择模型。
3. 打开题目或课程页面，选择需要的功能。

脚本免费，模型调用由服务商计费。已有不同答案会保留；章节测验自动提交需要本次明确授权。

## 程序截图

| 待刷列表 | 题目与答案 |
| --- | --- |
| [![待刷列表](assets/images/study-queue.png)](assets/images/study-queue.png) | [![题目与答案](assets/images/questions.png)](assets/images/questions.png) |

[查看全部截图](features.md#程序预览)
