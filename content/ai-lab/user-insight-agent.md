# AI User Insight Agent

*把杂乱的用户反馈，整理成可追溯、带原文证据的洞察。*

> **线上 Demo**：[my-agent-demo-233.netlify.app](https://my-agent-demo-233.netlify.app)（浏览器内虚拟数据工作台，非真实模型分析）
>
> **GitHub**：[Carla-guguwwwy051010/-agent-](https://github.com/Carla-guguwwwy051010/-agent-)
>
> **状态**：V0.4 仍是首轮鲁棒性测试，不是最终完成版。

## 01. 产品定位与用户场景

这是一个面向产品经理与用户运营的用户反馈洞察 Agent（内部代号 Folio）。它解决的是一个很具体的问题：用户反馈往往散在表格、工单、评论和聊天记录里，量一大就只能靠人肉翻看，结论也很难说清"这句话是从哪条反馈得出来的"。

产品的核心主张不是"帮你收集更多反馈"，而是：

> 把原始反馈整理成可以统计、可以排序、并且每一条结论都能点回原文的洞察。

典型场景：把一批用户反馈（CSV、TSV、Excel、TXT，或逐行粘贴）上传进来，系统完成清洗、去重、分类和主题归并，给出 Top Issues、趋势、版本对比，以及一个可以就着数据集提问的 Agent。任何一个数字、主题或回答里的反馈 ID，都能点回数据库里的原始反馈。

## 02. 核心流程

整条链路是围绕"可追溯"设计的：

> Raw Feedback → Classification → Theme Normalization → Tool Calling → Evidence-backed Insight

- **Raw Feedback**：字段映射、清理空白、按文本去重，保留源文件、原始行号、稳定反馈 ID，以及无法解析的日期原值。单次导入上限 10,000 行 / 20 MB。
- **Classification**：对每条反馈判断 Intent / Sentiment / Severity，并落到受控枚举，模型自由主题完整保留。
- **Theme Normalization**：把模型的自由主题（Raw Theme）归并到受控的标准问题（Issue Theme），再挂到产品大模块（Module）。这一层是 Top Issues 能用起来的关键。
- **Tool Calling**：Agent 通过一组数据工具查询当前数据集，回答基于工具返回的事实。
- **Evidence-backed Insight**：结论回挂原始反馈 ID，可点开原文核对。

## 03. Workflow + Agent 混合架构

系统不是纯粹的"把一切丢给模型"，而是 Workflow 与 Agent 的混合：

- **确定性 Workflow** 负责导入、去重、字段映射、主题归并校验、统计口径——这些必须稳定、可复现的环节用规则和固定映射来做。
- **Agent + Tool Calling** 负责开放式提问。Agent 只能调用受限的数据工具，且查询都限定在当前数据集：

| 工具 | 作用 |
| --- | --- |
| `get_top_issues` | 返回按标准主题聚合的 Top Issues |
| `get_cluster_detail` | 返回单个主题的成员与明细 |
| `get_issue_trend` | 按有效日期返回趋势 |
| `compare_versions` | 版本间反馈量对比 |
| `search_feedback` | 原文关键词检索 |
| `get_evidence` | 按反馈 ID 取原文与元数据 |

缺少有效日期时不给趋势，少于两个有效版本时不给版本比较，根因和业务影响只作为待验证假设。

## 04. DeepSeek 本地真实接入，线上 Demo 为 Mock

这一点在项目里是明确区分、并在页面上标注的：

- **本地**保留 FastAPI 数据集 Agent 和 DeepSeek 的真实分析流程。DeepSeek 密钥只在服务端读取，余额不足或密钥无效时回退模拟模式；服务端每 60 秒检查一次账号可用状态。
- **线上 Demo** 是浏览器内的虚拟数据工作台。它复用同一套上传入口、字段确认、概览、Top Issues、证据抽屉和 Agent 对话布局，但跑的是内置的 16 条虚构反馈，不读取所选文件内容，也不调用模型。演示 Agent 的回答明确标注为**模拟回答**，不代表真实模型分析。

技术栈：前端 React 19 + TypeScript + Vite；完整分析后端 Python 3.11+ + FastAPI + SQLite；DeepSeek 请求走 httpx；线上模拟聊天用浏览器 localStorage。

## 05. Evaluation Framework、Failure Analysis、Regression、E2E

项目带一套本地评估框架，跑在本地 `backend/app.py` 上，除模型推理只访问 `api.deepseek.com` 外，不接触任何线上数据库。评估集全部是虚构、人工标注的数据。它测的维度包括：

- **分类一致性**：Intent / Sentiment / Severity / Enum Compliance / Module 固定映射。
- **Agent**：Tool Selection、Tool Parameter、Task Success。
- **Theme Normalization**：主题归并准确率、Purity、Over-splitting、Over-merging。
- **Failure Analysis**：每个失败 case 记录 Input / Expected / Actual / Failure Type / Possible Cause / Next Fix，作为待验证假设而不是直接改 gold。
- **Regression Test**：V0.1 的 10 条固定 fixtures 作为回归集，每次改动前后重跑。
- **End-to-End**：从原始反馈 / 分类 → 本地主题归并 → SQLite → 工具 → Final Answer 全链路跑通。

## 06. V0.1 → V0.4 的真实迭代

| 版本 | 重点 | 关键结果 |
| --- | --- | --- |
| V0.1 | 分类 + Agent baseline（10 条） | Module 10/10；Intent 6/10；Sentiment 9/10；Severity 8/10；Agent Tool Selection / Param / Task Success 均 10/10 |
| V0.2 | 扩到 50 条真实导入 + DeepSeek | Intent / Sentiment / Severity 各 47/50（94%）；Enum 50/50；V0.1 回归 10/10。但 50 条被分成 49 个自由主题，Top Issue 只有 2 条，暴露归并过细 |
| V0.3 | Theme Normalization | 49 → 13 个标准主题；Top 5 覆盖率 12% → 56%（+44pp）；归并专用集 36/36；Purity 100%；Over-splitting 0/12、Over-merging 0/12；E2E 5/5 |
| V0.4 | 首轮鲁棒性压力测试 | 90 条有效 + 5 重复 + 5 噪声，含多语言、错别字、混合语种等更难输入 |

### V0.3 的主题归并

V0.2 到 V0.3 是这个项目最关键的一次迭代。50 条反馈原本被模型拆成 49 个 Raw Theme，几乎一条一个主题，Top Issues 根本排不出来。加入 Theme Normalization 后：

- 用于 Top Issues 的主题从 49 归并到 13（-73.5%）；
- Top 5 覆盖率从 12%（6/50）升到 56%（28/50）；
- 归并专用集 Purity 100%，Over-splitting 0/12、Over-merging 0/12；
- Raw Theme 完整保留，归并只发生在 Issue Theme 这一层。

### V0.4 的定位

V0.4 是**首轮鲁棒性测试，不是最终完成版**。它故意喂进更难的输入（多语言、错别字、混合语种、噪声和重复），并且分类分数这一轮用的是未改动的本地 MockProvider，不是 DeepSeek。结果如实记录了退化：

| 指标 | V0.4 结果 |
| --- | --- |
| Intent（离线 Mock） | 43/90（47.8%） |
| Sentiment（离线 Mock） | 60/90（66.7%） |
| Severity（离线 Mock） | 57/90（63.3%） |
| Enum Compliance | 90/90（100%） |
| Theme Merge Accuracy | 72/90（80%） |
| Purity | 83/102（81.4%） |
| Unknown Theme Handling | 10/10（100%） |
| Top Issues Stability | 4/5 |
| End-to-End Task Success | 5/5 |

这一轮观察到 9 个 gold 主题被拆散、5 个预测主题出现混合，正是下一步要收敛的方向。指标退化是被预期的：更难的输入 + Mock 分类，本来就是用来找边界的。

## 07. 当前限制

- V1 为单机 SQLite，只有共享访问口令，无个人账户、租户隔离和并发任务队列。
- 模型分析可能需要人工复核；DeepSeek 部分批次失败会回退模拟分类并报告错误，尚无失败条目单独重跑界面。
- 当前支持主题级人工整理（改名、合并、移出列表），尚无逐条反馈人工修正界面或完整趋势图。
- 提及频次只表示提及量，不代表业务优先级。
- 评估样本为小规模合成数据，不代表生产准确率。

下一步计划用未参与规则设计的 100–200 条盲测集验证泛化，增加多标签策略处理一条反馈里的多个问题，并对"模块·其他问题"建立人工审核队列。
