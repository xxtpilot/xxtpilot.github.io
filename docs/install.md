---
title: 安装教程
description: 在 Chrome 或 Edge 安装 Tampermonkey 和 学习通AI助手，并完成首次模型配置。
---

# 安装教程

推荐在电脑端 Chrome 或 Edge 使用。官网可在手机阅读，脚本的页面适配与运行方式以电脑网页端为主。

## 1. 安装 Tampermonkey

打开 [Tampermonkey 官方网站](https://www.tampermonkey.net/)，选择你的浏览器，按页面入口进入对应扩展商店安装。安装后确认扩展处于启用状态。

!!! tip "找不到扩展图标？"
    打开浏览器工具栏的扩展菜单，找到 Tampermonkey；可将它固定到工具栏，方便查看脚本状态。

## 2. 允许用户脚本运行

进入 Tampermonkey 的浏览器扩展管理页，按当前浏览器提供的选项开启“允许运行用户脚本”。如果浏览器要求启用开发者模式，请按照 Tampermonkey 的提示设置。

Chrome 可在地址栏输入 `chrome://extensions/`；Edge 可输入 `edge://extensions/`。完成后刷新学习通页面。

更详细的逐步图片可参阅原项目的[图文安装教程](https://github.com/zhu-hailin/chaoxing-ai-assistant/blob/main/docs/%E5%AD%A6%E4%B9%A0%E9%80%9A%E8%84%9A%E6%9C%AC%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B.md)。

## 3. 安装完整脚本

[安装／更新 学习通AI助手](https://github.com/zhu-hailin/chaoxing-ai-assistant/raw/HEAD/%E5%AD%A6%E4%B9%A0%E9%80%9AAI%E5%8A%A9%E6%89%8B.user.js)

点击后，在 Tampermonkey 安装页核对脚本名称“学习通 AI 助手”，确认安装。随后打开或刷新学习通课程页面。

如果没有出现安装页，可从[原项目仓库](https://github.com/zhu-hailin/chaoxing-ai-assistant)打开完整 `学习通AI助手.user.js`，将全部内容复制到 Tampermonkey 的新建脚本编辑器并保存。

## 4. 配置自己的模型

打开“学习通AI助手”，进入 **设置 → 模型设置**：

1. 选择服务商，填写并保存自己的 API Key。
2. 获取模型列表，选择本次使用的模型；自定义服务填写 OpenAI 兼容接口地址与模型 ID。
3. 按需检测连接或图片能力。图片题和视频画面识别需要相应的图片能力。

脚本免费。API Key 由你自行准备，模型调用费用与额度由服务商决定。

[查看完整模型配置说明](guide/models.md)

## 5. 选择使用方式

| 所在页面 | 可以开始的操作 |
| --- | --- |
| 章节测验或作业 | 提取题目、AI 分析、核对与预填 |
| 具体课程首页或学习页 | 处理本课程的章节任务 |
| 个人空间课程列表 | 勾选课程，创建按顺序运行的课程队列 |

界面名称可能随脚本更新调整。官网按已发布的 v1.31 介绍，安装内容以原项目当前公开脚本为准。

## 更新脚本

再次点击本页安装按钮，或从 [GitHub Releases](https://github.com/zhu-hailin/chaoxing-ai-assistant/releases)下载完整脚本更新。更新后刷新已打开的课程页面。

当前仍有任务运行时，先停止并查看待办报告，再更新脚本。

## 入口仍未出现？

确认 Tampermonkey 和脚本均已启用、用户脚本运行权限已开启，并刷新整个页面。若问题仍在，请查看[常见问题](faq.md#安装后没有显示入口)。
