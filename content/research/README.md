# Research 目录

> **注意：此目录目前为架构占位，暂无真实内容。**

## 说明

Research 部分是信息架构图中规划的内容区域，用于存放：
- 产品体验分析
- 用户研究笔记
- 行业观察
- 竞品分析
- 其他产品研究相关内容

## 当前状态

**PLACEHOLDER / FUTURE CONTENT**

目前网站上显示的 3 篇研究文章（小红书评论区、微信朋友圈、豆包 AI）仅为架构示例，不是真实内容。

## 未来规划

当有真实的研究内容时，可在此目录下建立：

```
research/
├── xiaohongshu-comments/
│   └── analysis.md
├── wechat-moments/
│   └── analysis.md
└── doubao-ai/
    └── analysis.md
```

## 接入方式

真实内容创建后，需要：
1. 在此目录创建对应的 Markdown 文档
2. 更新 `index.html` 中的 `ARTICLES.research.items` 配置
3. 修改 `renderArticle()` 函数以加载真实内容（或链接到外部文章）

等待填充真实内容。
