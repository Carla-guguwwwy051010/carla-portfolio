# 项目链接配置 / Project Links

> 此文档用于集中管理所有项目的外部链接（Demo / GitHub / Figma / 文档等）。

## 说明

这是项目链接的集中配置文件。修改此文件后，需要同步更新 `index.html` 中的 `RESOURCES` 配置对象。

---

## LoveMemo

### 已有链接 ✅
- **Live Demo**: https://our-lovememo-rcuv.vercel.app/
- **GitHub**: https://github.com/carla-guguwwwy051010

### 待添加链接 ⏳
- **Figma 原型**: 
- **PRD 文档**: https://my.feishu.cn/wiki/BmLPwLjfziACD0kP0FkcnZ58nMg?from=from_copylink
- **用户流程图**: 
- **信息架构图**: 
- **产品截图**: 
- **其他文档**: 

---

## Personal OS

### 已有链接 ✅
- **GitHub**: https://github.com/carla-guguwwwy051010

### 待添加链接 ⏳
- **Live Demo**: https://personal-os-green-nine.vercel.app/
- **Figma 原型**: 
- **PRD 文档**: https://my.feishu.cn/wiki/NfdLwDJNViedKBkox0OcFKWCn13?from=from_copylink
- **模块设计文档**: 
- **Dashboard 截图**: 
- **其他文档**: 

---

## Vybcall Video

### 已有链接 ✅
- **H5 Demo**: https://kuyin.iflysec.com/grocery/vybcall/index.html?b=1#/
- **GitHub**: https://github.com/carla-guguwwwy051010

### 待添加链接 ⏳
- **墨刀原型**: https://modao.cc/proto/AM6VODUtjwjoydsDThOG/sharing?view_mode=read_only&screen=rbpVSXFU1kby2mQiU 
- **PRD 文档**: https://my.feishu.cn/docx/PbRqdqTjpoA7a2xNOmscWngrn6c?from=from_copylink

---

## 如何更新网站上的链接

当你添加了新的链接后，需要：

1. **更新此文档**（记录链接）

2. **更新 `index.html` 中的 `RESOURCES` 配置**（约第 394-417 行）

   例如，为 LoveMemo 添加 Figma 链接：
   ```javascript
   const RESOURCES = {
     lovememo: [
       {type:'demo', label:'Live Demo ↗', sub:'OPEN LIVE PROJECT', url:'https://...'},
       {type:'github', label:'GitHub ↗', sub:'SOURCE / REPO', url:'https://...'},
       {type:'figma', label:'Figma 原型', sub:'DESIGN FILE', url:'https://figma.com/...'}, // 👈 修改这里
       // ...
     ]
   };
   ```

3. **保存并刷新浏览器**，查看项目详情页的资源链接

---

## 其他链接

### Resume PDF
- **当前状态**: 未上传
- **路径配置**: `SITE.resumePdf` (index.html 第 435 行)
- **添加方法**: 
  1. 将简历 PDF 放到 `resume/` 目录
  2. 修改 `SITE.resumePdf = "resume/Carla_Resume.pdf"`

### Research / AI Lab / Thinking 文章
- **当前状态**: 占位内容，暂无真实文章
- **未来**: 可以链接到外部博客文章（如知乎、Medium 等）

---

等待填充真实链接。
