# CONTENT MAP — 内容地图与接入指南

> 本文档说明整个 Portfolio 网站的内容来源、文件路径、页面对应关系，以及如何将真实资料接入网站。

---

## 📋 目录

- [一、内容分类](#一内容分类)
- [二、文件结构总览](#二文件结构总览)
- [三、真实内容映射](#三真实内容映射)
- [四、占位内容说明](#四占位内容说明)
- [五、接入流程](#五接入流程)
- [六、配置文件位置](#六配置文件位置)

---

## 一、内容分类

### ✅ REAL CONTENT（真实内容）

以下是需要填充真实资料的部分：

#### 1. 个人信息
- 姓名、定位、简介
- 教育背景
- 实习/工作经历
- 技能清单
- 联系方式

**文件位置**: `content/profile/`

#### 2. 三个真实项目

##### LoveMemo
- 项目概览、用户研究、用户流程、开发协作、产品复盘
- PRD 文档、原型设计
- Demo / GitHub / Figma 链接

**文件位置**: `content/projects/lovememo/`

##### Personal OS
- 项目概览、用户研究、用户流程、开发协作、产品复盘
- PRD 文档、原型设计、模块设计
- Demo / GitHub / Figma 链接

**文件位置**: `content/projects/personal-os/`

##### Vybcall Video
- 项目概览、业务背景、用户流程、内容策略、数据埋点、开发协作、产品复盘
- PRD 文档、H5 原型
- Demo / GitHub / Figma 链接

**文件位置**: `content/projects/vybcall/`

#### 3. 简历 PDF
**文件位置**: `resume/`

---

### ⏳ PLACEHOLDER / FUTURE CONTENT（占位内容）

以下是架构图中的规划内容，目前仅为示例，**不是真实内容**：

#### Research（产品研究）
- 小红书评论区优化分析
- 微信朋友圈体验分析
- 豆包 AI 产品分析

**文件位置**: `content/research/`  
**当前状态**: 架构占位，无真实内容

#### AI Lab（AI 实验）
- AI 会议纪要 Agent
- AI 旅行规划 Agent
- 更多实验

**文件位置**: `content/ai-lab/`  
**当前状态**: 架构占位，无真实内容

#### Thinking（产品思考）
- 为什么 AI 产品越来越像记忆产品？
- 产品经理为什么要懂一点技术？
- 为什么 MVP 不是"简陋版本"？

**文件位置**: `content/thinking/`  
**当前状态**: 架构占位，无真实内容

---

## 二、文件结构总览

```
咕咕的个人作品集/
│
├── index.html                          # 网站主文件（单文件架构）
├── Carla_Portfolio_V3.3.html           # V3.3 备份（不要修改）
├── 架构图.jpg                          # 信息架构参考
├── 项目结构说明.md                     # 技术文档
├── CONTENT_MAP.md                      # 本文档
│
├── content/                            # 📁 内容目录（Markdown 文档）
│   ├── profile/                        # 个人信息
│   │   ├── personal-info.md            # 基本信息
│   │   ├── education.md                # 教育背景
│   │   ├── experience.md               # 工作经历
│   │   ├── skills.md                   # 技能清单
│   │   └── contact.md                  # 联系方式
│   │
│   ├── projects/                       # 项目文档
│   │   ├── lovememo/
│   │   │   ├── overview.md             # 项目概览
│   │   │   ├── user-research.md        # 用户研究
│   │   │   ├── user-flow.md            # 用户流程
│   │   │   ├── development.md          # 开发协作
│   │   │   ├── review.md               # 产品复盘
│   │   │   ├── prd/                    # PRD 文档目录
│   │   │   │   └── README.md
│   │   │   └── prototype/              # 原型设计目录
│   │   │       └── README.md
│   │   │
│   │   ├── personal-os/
│   │   │   ├── overview.md
│   │   │   ├── user-research.md
│   │   │   ├── user-flow.md
│   │   │   ├── development.md
│   │   │   ├── review.md
│   │   │   ├── prd/
│   │   │   │   └── README.md
│   │   │   └── prototype/
│   │   │       └── README.md
│   │   │
│   │   └── vybcall/
│   │       ├── overview.md
│   │       ├── business-background.md  # 业务背景
│   │       ├── user-flow.md
│   │       ├── content-strategy.md     # 内容策略
│   │       ├── tracking.md             # 数据埋点
│   │       ├── development.md
│   │       ├── review.md
│   │       ├── prd/
│   │       │   └── README.md
│   │       └── prototype/
│   │           └── README.md
│   │
│   ├── research/                       # ⏳ 占位
│   │   └── README.md
│   ├── ai-lab/                         # ⏳ 占位
│   │   └── README.md
│   └── thinking/                       # ⏳ 占位
│       └── README.md
│
├── assets/                             # 📁 静态资源目录（图片/视频/PDF）
│   ├── README.md
│   ├── home/                           # Home 页面素材
│   ├── projects/
│   │   ├── lovememo/                   # LoveMemo 项目素材
│   │   ├── personal-os/                # Personal OS 项目素材
│   │   └── vybcall/                    # Vybcall 项目素材
│   └── about/                          # About 页面素材
│
├── links/                              # 📁 链接配置
│   └── project-links.md                # 项目外部链接集中管理
│
└── resume/                             # 📁 简历目录
    └── README.md
```

---

## 三、真实内容映射

### 网站页面 ↔ 内容文件对应关系

| 网站页面/区域 | 内容来源 | 文件路径 | 当前状态 |
|--------------|---------|---------|---------|
| **Home - Hero** | 个人信息 | `content/profile/personal-info.md` | ⏳ 等待填充 |
| **Home - Projects 列表** | 项目概览 | `content/projects/*/overview.md` | ⏳ 等待填充 |
| **Projects - LoveMemo 详情页** | 项目完整文档 | `content/projects/lovememo/` | ⏳ 等待填充 |
| **Projects - Personal OS 详情页** | 项目完整文档 | `content/projects/personal-os/` | ⏳ 等待填充 |
| **Projects - Vybcall 详情页** | 项目完整文档 | `content/projects/vybcall/` | ⏳ 等待填充 |
| **About** | 个人信息、教育、经历、技能 | `content/profile/` | ⏳ 等待填充 |
| **Resume** | 简历 PDF | `resume/Carla_Resume.pdf` | ⏳ 等待上传 |
| **Research 详情页** | 研究文章 | `content/research/` | ⚠️ 占位 |
| **AI Lab 详情页** | AI 实验 | `content/ai-lab/` | ⚠️ 占位 |
| **Thinking 详情页** | 思考文章 | `content/thinking/` | ⚠️ 占位 |

---

## 四、占位内容说明

### ⚠️ 重要提示

目前网站上显示的以下内容**不是真实内容**，仅为架构示例：

1. **Research 区域**
   - "小红书评论区优化分析"
   - "微信朋友圈体验分析"
   - "豆包 AI 产品分析"
   
   👉 这些是架构图中的占位文章标题，用于演示信息架构，不是你的真实研究成果。

2. **AI Lab 区域**
   - "AI 会议纪要 Agent"
   - "AI 旅行规划 Agent"
   - "更多实验"
   
   👉 这些是架构图中的占位实验标题，用于演示信息架构，不是你的真实 AI 实验。

3. **Thinking 区域**
   - "为什么 AI 产品越来越像记忆产品？"
   - "产品经理为什么要懂一点技术？"
   - "为什么 MVP 不是'简陋版本'？"
   
   👉 这些是架构图中的占位文章标题，用于演示信息架构，不是你的真实思考文章。

### 如何处理占位内容

- **不要编造内容**填充这些占位部分
- 当有真实的研究/实验/文章时，按照"五、接入流程"更新
- 在填充真实内容之前，这些区域会显示"Documentation in progress"

---

## 五、接入流程

### 步骤 1: 准备内容文件

#### A. 个人信息
1. 编辑 `content/profile/` 下的 5 个 Markdown 文件
2. 填写真实的个人信息、教育背景、工作经历、技能、联系方式

#### B. 项目文档
1. 为每个项目（LoveMemo / Personal OS / Vybcall）编辑对应的 Markdown 文档
2. 上传项目相关图片到 `assets/projects/项目名/`
3. 如有 PRD PDF 或原型文件，放到对应的 `prd/` 或 `prototype/` 目录

#### C. 项目链接
1. 编辑 `links/project-links.md`
2. 填写真实的 Demo / GitHub / Figma / 文档链接

#### D. 简历 PDF
1. 将简历 PDF 文件放到 `resume/` 目录
2. 文件名建议：`Carla_Resume.pdf`

---

### 步骤 2: 更新网站配置

打开 `index.html`，定位到 **JavaScript 数据配置区**（约第 375-435 行）

#### A. 更新项目数据（DATA 对象）

根据 `content/projects/*/overview.md` 的内容，更新 `DATA` 对象：

```javascript
const DATA = {
  lovememo: {
    title: "LoveMemo",
    kicker: "RELATIONSHIP · PERSONAL PRODUCT",
    tagline: "从 overview.md 复制一句话介绍",
    problem: "从 overview.md 复制项目背景",
    work: [
      "从 overview.md 复制工作内容1",
      "从 overview.md 复制工作内容2",
      // ...
    ],
    sections: [
      "项目背景",
      "用户分析",
      // ... 根据实际文档调整
    ]
  },
  // personal / vybcall 同理
};
```

#### B. 更新项目封面图（IMGS 对象）

如果要替换项目封面图：
1. 将新图片转为 base64（工具：https://www.base64-image.de/）
2. 替换 `IMGS` 对象中的对应值

#### C. 更新项目资源链接（RESOURCES 对象）

根据 `links/project-links.md` 的内容，更新 `RESOURCES` 对象：

```javascript
const RESOURCES = {
  lovememo: [
    {type:'demo', label:'Live Demo ↗', sub:'OPEN LIVE PROJECT', url:'https://your-real-demo-url.com'},
    {type:'github', label:'GitHub ↗', sub:'SOURCE / REPO', url:'https://github.com/your-real-repo'},
    {type:'figma', label:'Figma 原型', sub:'DESIGN FILE', url:'https://figma.com/your-real-link'}, // 如果有
    {type:'prd', label:'PRD 文档', sub:'VIEW DOCUMENT', url:'content/projects/lovememo/prd/PRD_v1.0.pdf'}, // 如果有
    // ...
  ],
  // personal / vybcall 同理
};
```

**注意**: 
- 如果某个资源还没有，保持 `url: null`，会显示"Coming soon"
- 如果有真实链接，填入完整 URL

#### D. 更新简历配置（SITE 对象）

```javascript
const SITE = { 
  resumePdf: "resume/Carla_Resume.pdf"  // 👈 修改这里
};
```

---

### 步骤 3: 验证

1. 保存 `index.html`
2. 刷新浏览器
3. 逐一检查：
   - Home 页面信息是否正确
   - 点击项目卡片，进入详情页，检查内容是否显示
   - 点击资源链接，检查是否能正确打开
   - Resume 区域是否显示预览/下载按钮

---

## 六、配置文件位置

### 核心配置位置（index.html）

| 配置对象 | 行数（约） | 作用 |
|---------|----------|------|
| `DATA` | 375 | 项目文本内容 |
| `IMGS` | 376 | 项目封面图（base64） |
| `LINKS` | 377-385 | 旧版链接配置（保留兼容） |
| `RESOURCES` | 394-417 | 项目资源链接（重要⭐） |
| `ARTICLES` | 418-433 | Research/Lab/Thinking 文章配置 |
| `SITE` | 435 | 全局配置（Resume PDF 路径） |

### 辅助配置文件

| 文件 | 作用 |
|-----|------|
| `links/project-links.md` | 项目链接集中管理（方便查看） |
| `assets/README.md` | 静态资源目录说明 |
| `resume/README.md` | 简历上传指南 |
| `content/*/README.md` | 各内容目录说明 |

---

## 七、常见问题

### Q1: 我应该先填充哪些内容？

**建议顺序**：
1. 个人信息（`content/profile/`）
2. 三个项目的概览（`content/projects/*/overview.md`）
3. 项目链接（`links/project-links.md` + 更新 `index.html` 中的 `RESOURCES`）
4. 简历 PDF（`resume/` + 更新 `SITE.resumePdf`）
5. 项目详细文档（PRD / 用户研究 / 复盘等）
6. 项目图片素材（`assets/projects/`）

### Q2: 如何更新项目封面图？

**方法 A（推荐）：保持 base64 方式**
1. 新图片转为 base64
2. 替换 `IMGS` 对象中的值
3. 优点：单文件分发，打开即用

**方法 B：使用外部图片文件**
1. 图片放到 `assets/projects/项目名/`
2. 修改 `index.html` 中引用图片的代码（需要技术修改）
3. 优点：文件更小，图片易替换

### Q3: Research / AI Lab / Thinking 的占位内容需要删除吗？

**不需要删除**。

- 占位内容展示了信息架构，告诉访客"这里未来会有这些内容"
- 详情页会显示"Documentation in progress"，诚实表明正在整理中
- 当有真实内容时，按照接入流程更新即可

### Q4: 项目 PRD 文档是放 PDF 还是 Markdown？

**都可以**：
- **Markdown**：放在 `content/projects/*/prd/` 下，便于在线阅读和修改
- **PDF**：放在 `content/projects/*/prd/` 下，配置资源链接即可下载
- 建议两者都提供（Markdown 在线查看 + PDF 下载）

### Q5: 如何添加新的项目？

参考《项目结构说明.md》的"E. 后续新增项目的操作方法"部分。

---

## 八、下一步行动

### 现在可以做的：

1. ✅ **文件结构已搭建完成**（本次任务）
2. ⏳ **填充个人信息**（`content/profile/`）
3. ⏳ **填充项目文档**（`content/projects/`）
4. ⏳ **更新项目链接**（`links/project-links.md` + `index.html RESOURCES`）
5. ⏳ **上传简历 PDF**（`resume/` + `index.html SITE.resumePdf`）
6. ⏳ **上传项目图片**（`assets/projects/`）

### 接入支持：

当你准备好真实内容后，可以：
- 按照本文档的"五、接入流程"自行接入
- 或者提供内容文件，让 AI 辅助更新配置

---

**最后更新**: 2026-09-08  
**版本**: V3.4 内容结构搭建版
