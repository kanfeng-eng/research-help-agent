# 已接入的科研能力

## ARS-Codex

本包包含真实的 `../academic-research-suite/`，由 `docs/upstream-lock.json` 锁定仓库与提交。优先读取该包 `SKILL.md` 的路由规则，并按当前任务只加载一个所需 workflow。其资源都保存在包内，移动整个 `dl_agent` 后仍可定位。

| 工作 | 相对 ARS skill 根目录的入口 |
| --- | --- |
| 文献检索、研究问题、跨论文综合 | `ars/deep-research/WORKFLOW.md` |
| 方向明确后的自动谱系追踪 | `ars/deep-research/WORKFLOW.md` 的检索、核查与综合方法，配合本地 [自动研究编排](research-orchestration.md) |
| 证据达到条件后的核心分析 | `ars/deep-research/WORKFLOW.md` 及 `ars/deep-research/agents/devils_advocate_agent.md`，最小实验设计使用 `ars/experiment-agent/WORKFLOW.md` 的 plan 方法 |
| 实验设计、执行或结果复核 | `ars/experiment-agent/WORKFLOW.md` |
| 假设、方法与候选构想的反向审查 | `ars/deep-research/WORKFLOW.md` 与 `ars/deep-research/agents/devils_advocate_agent.md` |
| 用户明确要求稿件审阅或模拟同行评审 | `ars/academic-paper-reviewer/WORKFLOW.md` |
| 用户明确进入写作、修订与引用检查 | `ars/academic-paper/WORKFLOW.md` |
| 用户明确要求完整研究至论文流程 | `ars/academic-pipeline/WORKFLOW.md` |
| 用户明确要求已有文献记录筛选 | `ars/sr-screener/WORKFLOW.md` |

调用意味着读取对应方法和必要资源，用当前 Codex 工具实际完成工作。论文创新讨论先用本地讨论规则开展具体分析，所需背景与近邻核查调用 ARS deep-research 的检索、综合和反向论证方法。上游 socratic 或教学模式仅在用户明确要求时进入。子 agent 使用它时由主 agent 提供入口绝对路径。

## 按当前请求适配

### 阶段产物路径映射

以下路径统一相对已明确的科研项目根目录。主 agent 在调用或委派前将路径展开成该项目内的绝对路径，沿用已有 ID、目录和用户内容。子 agent 默认返回分析，由主 agent 写正式记忆；明确授权的代码和实验产物写入范围另行给出。

| ARS 工作 | 正式研究记录位置 |
| --- | --- |
| deep-research 的论文分析、来源与阅读范围 | `memory/papers/Paper_<ID>.md`、`memory/03_Literature_Index.md`，需要来源台账时放 `memory/papers/<ID>/` |
| 自动谱系追踪及增量更新 | `memory/Research_Lineage.md`，关系附来源，状态与未完成动作同步当前状态和交接 |
| run the core logic 的综合与判断 | `memory/04_Cross_Paper_Analysis.md`，链接相关问题、IDEA 和最小实验计划；当前状态记录触发原因与已处理输入 |
| 研究问题、跨论文综合与近邻检索 | `memory/04_Cross_Paper_Analysis.md`、`memory/05_Research_Gaps.md`、`memory/07_Open_Questions.md` |
| 假设反向审查与成熟 IDEA | 初步观察和假设进入 `memory/05_Research_Gaps.md`；成熟构想进入 `memory/ideas/IDEA_<ID>.md`，研究员观点进入 `memory/02_Researcher_Ideas.md` |
| experiment-agent 的 plan、run、validate | `memory/experiments/<ID>/Experiment_Plan.md`、`Experiment_Log.md`、`Result_Analysis.md`；必要的阶段元信息放同一实验子目录 |
| 写作准备与主张依据 | `memory/Writing_Readiness.md`，记录逐项证据、缺口和可写范围 |
| 稿件评审、回复与文献筛选的过程记录 | 按需放 `memory/reviews/<ID>/`、`memory/literature-screening/<ID>/`，并链接对应论文、决策和来源 |
| 完整 pipeline 的阶段状态、Material Passport、交接与决策 | 状态汇总到 `memory/00_Current_State.md`，交接进入 `memory/08_Research_Handoff.md`，决策进入 `memory/06_Decision_Log.md`；阶段元信息嵌入相应记录或放其同级子目录 |

论文 PDF、全文提取、大型筛选表、代码、原始日志、权重、正式稿件和交付的 HTML 笔记使用用户指定或项目已有的资料/代码/产物目录，记忆保存路径、版本及摘要。目录和文件按真实产物创建。

上游 workflow 示例中的状态目录、阶段文件名或相对工作目录，都需先映射到此表。已有 ARS 记录先读取和关联，合并时保留来源与历史。一次调用开始与结束均核对实际落点，正式研究记录统一进入项目 `memory/`。

### 本地流程与上游方法

用户文档选择了长期探索、可回退、最小实验和可选写作。本地主流程遵循这些选择，ARS 作为当前阶段的专业方法来源。

- 方向、阶段、资源投入与正式决策按照用户当前请求及已确认记忆。
- 上游模板中的默认篇数、固定检查表和复现容差按实际任务采用，只有对当前结论有影响时才成为检验条件。
- 日常假设审查加载 deep-research 的反向论证方法，按本地创新审查合同返回机制、反例、竞争解释和最小检验。正式稿件审阅由用户明确要求后进入 academic-paper-reviewer，遵循该 workflow 的角色卡片、入口确认及用户明确授权的跳过规则。实际流程和研究员已有授权保持一致。
- 上游特定模型、API、MCP、Claude 命令或外部服务示例需检查本环境。使用已有 Codex、搜索、shell 与文件工具完成其实际目的，缺能力时报告真实缺口。
- 上游实验模块默认只运行用户提供的命令，本包同时支持用户授权的实现、调试和预算内重试，按本地实验协议记录变化。
- 正式科研记忆按上面的路径表维护，阶段状态复用项目当前状态和交接。上游写作入口先执行本地写作前核查，随后按实际可写范围调用。

## 刚才检索到的其他方案

ResearchPilot 的中文分阶段组织、Orchestra 的实验/反思双循环和 K-Dense 的竞争解释思路可供进一步比较。本包当前安装并调用 ARS-Codex，下面三个项目列作设计参考，未声明为已加载的技能依赖。

- [ResearchPilot-Skills](https://github.com/LMDHQ-0420/ResearchPilot-Skills)
- [Orchestra AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
