# Resume 目录

> 此目录用于存放简历 PDF 文件。

## 当前状态

**未上传简历 PDF**

网站上的 Resume 区域目前显示占位按钮："Resume PDF - COMING SOON · ADD FILE"

## 如何添加简历

### 步骤 1: 准备简历 PDF
- 文件名建议：`Carla_Resume.pdf` 或 `WangYan_Resume.pdf`
- 确保 PDF 可以在浏览器中预览

### 步骤 2: 放置文件
- 将 PDF 文件放到此目录（`resume/`）

### 步骤 3: 更新配置
- 打开 `index.html`
- 定位到第 435 行左右：`const SITE = { resumePdf: null };`
- 修改为：`const SITE = { resumePdf: "resume/Carla_Resume.pdf" };`
- 保存文件

### 步骤 4: 验证
- 刷新浏览器
- 滚动到 Resume 区域
- 应该看到两个按钮：
  - **Preview PDF ↗** （在浏览器中打开）
  - **Download ↓** （下载 PDF）

## 多语言简历（可选）

如果有中英文两个版本的简历，可以这样组织：

```
resume/
├── Carla_Resume_CN.pdf    # 中文简历
├── Carla_Resume_EN.pdf    # 英文简历
└── README.md              # 本文档
```

然后在配置中选择主要展示的版本，或者修改 `initResume()` 函数以支持两个下载按钮。

---

等待上传简历 PDF 文件。
