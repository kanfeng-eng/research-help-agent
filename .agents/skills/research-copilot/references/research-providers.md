# 已接入的科研能力

## ARS-Codex

本包包含真实的 `../academic-research-suite/`，由 `docs/upstream-lock.json` 锁定仓库与提交。优先读取该包 `SKILL.md` 的路由规则，并按当前任务只加载一个所需 workflow。其资源都保存在包内，移动整个 `dl_agent` 后仍可定位。

| 工作 | 相对 ARS skill 根目录的入口 |
| --- | --- |
| 文献检索、研究问题、跨论文综合 | `ars/deep-research/WORKFLOW.md` |
| 实验设计、执行或结果复核 | `ars/experiment-agent/WORKFLOW.md` |
| 假设、方法与候选构想的反向审查 | `ars/deep-research/WORKFLOW.md` 与 `ars/deep-research/agents/devils_advocate_agent.md` |
| 用户明确要求稿件审阅或模拟同行评审 | `ars/academic-paper-reviewer/WORKFLOW.md` |
| 用户明确进入写作、修订与引用检查 | `ars/academic-paper/WORKFLOW.md` |
| 用户明确要求完整研究至论文流程 | `ars/academic-pipeline/WORKFLOW.md` |
| 用户明确要求已有文献记录筛选 | `ars/sr-screener/WORKFLOW.md` |

调用意味着读取对应方法和必要资源，用当前 Codex 工具实际完成工作。纯论文讨论可以使用本地讨论规则，所需背景核查调用 ARS deep-research。子 agent 使用它时由主 agent 提供入口绝对路径。

## 按当前请求适配

用户文档选择了长期探索、可回退、最小实验和可选写作。本地主流程遵循这些选择，ARS 作为当前阶段的专业方法来源。

- 方向、阶段、资源投入与正式决策按照用户当前请求及已确认记忆。
- 上游模板中的默认篇数、固定检查表和复现容差按实际任务采用，只有对当前结论有影响时才成为检验条件。
- 日常假设审查加载 deep-research 的反向论证方法，按本地创新审查合同返回机制、反例、竞争解释和最小检验。正式稿件审阅由用户明确要求后进入 academic-paper-reviewer，遵循该 workflow 的角色卡片、入口确认及用户明确授权的跳过规则。实际流程和研究员已有授权保持一致。
- 上游特定模型、API、MCP、Claude 命令或外部服务示例需检查本环境。使用已有 Codex、搜索、shell 与文件工具完成其实际目的，缺能力时报告真实缺口。
- 上游实验模块默认只运行用户提供的命令，本包同时支持用户授权的实现、调试和预算内重试，按本地实验协议记录变化。
- 正式科研记忆由本地项目 `memory/` 维护。ARS 需要的阶段产物可保存在对应论文、IDEA 或实验子目录，避免生成两套冲突的研究状态。

## 刚才检索到的其他方案

ResearchPilot 的中文分阶段组织、Orchestra 的实验/反思双循环和 K-Dense 的竞争解释思路可供进一步比较。本包当前安装并调用 ARS-Codex，下面三个项目列作设计参考，未声明为已加载的技能依赖。

- [ResearchPilot-Skills](https://github.com/LMDHQ-0420/ResearchPilot-Skills)
- [Orchestra AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs)
- [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
