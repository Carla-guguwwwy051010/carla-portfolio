# Thinking 目录

> **注意：此目录目前为架构占位，暂无真实内容。**

## 说明

Thinking 部分是信息架构图中规划的内容区域，用于存放：
- 产品思考文章
- 对产品、技术、人的观察和思考
- 方法论总结
- 成长复盘
- 其他深度思考内容

## 当前状态

**PLACEHOLDER / FUTURE CONTENT**

目前网站上显示的 3 篇文章（AI 产品与记忆、产品经理为什么要懂技术、MVP 不是简陋版本）仅为架构示例，不是真实内容。

## 未来规划

当有真实的思考文章时，可在此目录下建立：

```
thinking/
├── ai-memory-products/
│   └── article.md
├── pm-tech-skills/
│   └── article.md
└── mvp-thinking/
    └── article.md
```

## 接入方式

真实内容创建后，需要：
1. 在此目录创建对应的 Markdown 文档
2. 更新 `index.html` 中的 `ARTICLES.thinking.items` 配置
3. 修改 `renderArticle()` 函数以加载真实内容（或链接到外部博客文章）

等待填充真实内容。
