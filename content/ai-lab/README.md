# AI Lab 目录

> **注意：此目录目前为架构占位，暂无真实内容。**

## 说明

AI Lab 部分是信息架构图中规划的内容区域，用于存放：
- AI Agent 实验
- Prompt 工程
- 自动化流程
- AI 产品原型
- AI 辅助开发经验
- 其他 AI 相关实验和探索

## 当前状态

**PLACEHOLDER / FUTURE CONTENT**

目前网站上显示的 3 个实验（AI 会议纪要 Agent、AI 旅行规划 Agent、更多实验）仅为架构示例，不是真实内容。

## 未来规划

当有真实的 AI 实验时，可在此目录下建立：

```
ai-lab/
├── meeting-summary-agent/
│   ├── overview.md
│   ├── prompt.md
│   └── demo/
├── travel-planning-agent/
│   ├── overview.md
│   ├── prompt.md
│   └── demo/
└── other-experiments/
    └── README.md
```

## 接入方式

真实内容创建后，需要：
1. 在此目录创建对应的 Markdown 文档
2. 更新 `index.html` 中的 `ARTICLES.lab.items` 配置
3. 修改 `renderArticle()` 函数以加载真实内容（或链接到外部项目）

等待填充真实内容。
