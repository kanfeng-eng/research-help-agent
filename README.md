# DL Research Copilot

在当前 Codex 中使用的项目级科研协作包。研究员与主 agent 讨论，主 agent 按需要调用四个专业角色，并通过包内 ARS-Codex 完成文献、研究规划、实验分析与可选写作。

## 开始使用

可从 GitHub 获取完整配置包。

```powershell
git clone https://github.com/kanfeng-eng/research-help-agent.git
cd research-help-agent
```

跨项目使用时，将 `.agents/skills/` 内的 `research-copilot` 和 `academic-research-suite` 两个完整 skill 文件夹安装到用户级 `~/.agents/skills/`。专业职责按主 skill 的协作规范执行，原生 TOML 角色可按实际项目配置使用。

1. 在 Codex 中打开要开展研究的项目。
2. 输入 `$research-copilot` 调用科研助手。名称末尾为 `copilot`。下面示例中的 `<科研项目绝对路径>` 填当前项目位置，当前项目已明确时可直接引用。
3. 主 agent 加载该项目的 `memory/`，沿用已有方向和进展，缺少关键内容时只问当前最重要的问题。切换项目后加载新项目自己的记录。

```text
$research-copilot
科研项目根目录是 <科研项目绝对路径>。
我已经有研究方向，请读取已有资料和 memory，先讨论我当前的问题。
```

`dl_agent` 保存共享配置和技能资源，各项目分别保存科研记忆，例如 `项目A/memory/`、`项目B/memory/`。初始化脚本会拒绝把配置包及其子目录作为科研根目录。用户级技能安装目录同样受路径保护。

默认围绕你的 Research Direction 讨论论文，重点是创新机会、现有方法怎样改进，以及研究中遇到的瓶颈。AI 先恢复方向目标、资源约束、当前方案与瓶颈证据，再自主核对论文，串起“方向目标 → 瓶颈及竞争解释 → 论文机制 → 对现有方法的迁移或改进 → 最小验证”。论文中的结论与迁移到项目的假设分别记录，具体方法随证据调整。

讨论先给当前最有价值的研究判断、理由和可区分原因的验证。已遇到卡点时结合实际实验检查原因，目标与当前假设分别维护。暂未找到有依据的线索时，梳理论文的研究逻辑和对方向的实际启示。阅读顺序、教学问题和逐段带读在明确要求时启用。具体规则见 [方向导向的论文讨论](.agents/skills/research-copilot/references/research-workflow.md#方向导向的论文讨论)。

方向明确后会自动 trace the lineage，追踪研究谱系、方法分支和关键转折。阅读与讨论形成可比较机制、关键矛盾或新的诊断证据时，会自动 run the core logic，完成跨论文综合、机制推理、反例审查与最小实验设计。触发依据是相对已有分析的实质变化，已有文献库可以直接使用。

每轮会检查触发条件并在当前任务范围内推进。谱系进入 `memory/Research_Lineage.md`，核心分析进入 `memory/04_Cross_Paper_Analysis.md`，状态和已处理材料进入当前状态及交接。相同输入复用已有结果，方向或证据变化时定向更新。具体规则见 [自动研究编排](.agents/skills/research-copilot/references/research-orchestration.md)。

明确科研项目后，首次使用会自动初始化或加载其 `memory/`，有价值的讨论增量会持续保存。暂无线索的论文梳理也可以记录。你明确要求临时讨论、不保存或只读时，按对应范围执行。

也可以在当前对话中提供本包 `SKILL.md` 的绝对路径让 Codex 读取。项目级自动发现以实际打开的工作目录为准。

本次生成的是配置包，实际科研记忆将在进入明确的科研项目后初始化。可用以下命令单独验证初始化，命令从 `dl_agent` 运行。

```powershell
python .\.agents\skills\research-copilot\scripts\init_memory.py --project-root "<科研项目绝对路径>"
```

重复运行保留已有文件。科研项目的论文、数据、代码和模型继续使用各自正常位置，记忆只记录版本、路径和摘要。

ARS 的论文、假设、实验及阶段记录统一映射到这个项目的 `memory/`，具体位置见 [路径映射](.agents/skills/research-copilot/references/research-providers.md)。进入写作时先核对问题、近邻工作、方法、真实结果、公平对照、主张依据、机制、可复现性和创新措辞，准备记录保存在 `memory/Writing_Readiness.md`。

## 日常表达

```text
结合我的 direction、当前方法和瓶颈，讨论这篇论文能带来什么改进和研究机会。
这次实验卡在这里……结合论文和实际日志，帮我区分原因并确定最小诊断。
这篇论文的机制能迁移到我的方案哪个环节，条件与代价是什么？
这是我的想法……请核查机制、近邻工作和反例。
对比这些论文，看看是否存在同一个根因。
这是我的初步想法，帮我找反例与最接近的工作。
先设计最小实验，给出控制变量、预算和失败标准。
分析这些真实日志，先检查工程问题，再判断假设。
继续上次研究，先读取 memory。
```

科研探索可以反复回到论文、问题、假设和实验。用户决定正式方向、资源投入和是否进入写作，单篇论文可只形成准确的理解记录。

## 科研能力与专业角色

**已安装并接入的科研能力为 ARS-Codex**，统一入口是 `$academic-research-suite`。本地 `$research-copilot` 负责用户指定的长期讨论、创新成熟度、最小实验和项目记忆，按任务读取 ARS 的专业 workflow。当前选择以 ARS-Codex 为主，ResearchPilot、Orchestra 和 K-Dense 保留为有链接的设计参考。

| 专业角色 | 主要任务 |
| --- | --- |
| `literature_analyst` | 文献核查、方法比较与近邻工作 |
| `innovation_reviewer` | 证据、机制、反例、新颖性与反证实验 |
| `experiment_engineer` | 已授权实现、调试、运行与日志 |
| `result_analyst` | 独立检查公平性、实际结果与结论范围 |

例如可以说“让 innovation_reviewer 独立审查这个假设，主 agent 汇总依据”。委派时主 agent 提供项目根、证据、授权范围与完成条件，只调用有实际用途的角色。自定义角色暂不可用时，主 agent 按相同角色规范执行并报告真实方式。

本机测试中原生子 agent 可用，当前 spawn 接口没有按自定义类型选择角色的字段。默认后备方式是主 agent 读取 TOML 中的角色指令，显式传给原生子 agent；原生子 agent 也不可用时，主 agent 自己执行角色流程。TOML 类型直接加载仍需支持该选择方式的客户端验证。

角色继承主会话的模型和权限，只读角色的约束由指令表达。本包使用当前 Codex 登录态和原生工具，无需填写额外 API Key；交付物是文件配置和技能资源，没有独立 Agent 服务或后台守护进程。

## 目录

```text
dl_agent/
  AGENTS.md
  .codex/agents/                  四个原生 TOML 角色
  .agents/skills/
    research-copilot/             本地科研主流程、参考、模板和初始化脚本
    academic-research-suite/      完整 ARS-Codex skill 与本地依赖
  docs/                          环境、构建来源及上游版本/许可
  tests/                         本地结构、路径和记忆保护检查
  tmp/checks/                    验收输出与隔离测试材料
```

移动时复制整个目录。ARS 资源使用包内位置，原始 Downloads 提示词只作为构建来源，不参与运行。项目中可用的 `paper-reading-notes` 可继续按明确的精读笔记请求使用，主科研流程也支持直接读取 PDF 和讨论。

## 检查

```powershell
python -m unittest discover -s .\tests -v
```

实际环境、验证方式和限制见 [环境记录](docs/environment.md)、[验收报告](docs/acceptance.md) 与 `tmp/checks/`。结构测试、角色发现测试、工作流情景检查和真实科学实验分别按实际执行记录。新研究的模型训练及研究结论由之后的授权实验产生。

Git 仓库保存配置、技能资源、模板、测试和验收摘要。`tmp/` 为本机检查产物，测试会按需创建目录。各项目的 `memory/` 由实际科研会话维护。

## 来源与引用

- 用户提供的《Codex 科研 Skill 完整构建提示词》用于确定本地协作要求。文件摘要与 SHA-256 记录在 [构建来源](docs/build-source.json)。
- [ARS-Codex](https://github.com/Imbad0202/academic-research-skills-codex) 提供实际科研 workflow，作者 Cheng-I Wu。固定提交与分发文件记录在 [上游锁定记录](docs/upstream-lock.json)。上游许可为 CC BY-NC 4.0，保留完整 [许可证](docs/ARS-LICENSE.txt)、包内 NOTICE 和署名，使用与再分发遵循其许可。
- [ResearchPilot-Skills](https://github.com/LMDHQ-0420/ResearchPilot-Skills) 提供中文研究阶段组织参考，其资源后置估算规则由本地预算内最小实验要求取代。
- [Orchestra AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) 提供实验与反思双循环的参考。
- [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) 提供假设、竞争解释和证据边界的参考。
- [OpenAI 官方 subagents 文档](https://learn.chatgpt.com/docs/agent-configuration/subagents) 用于核对原生角色文件位置与必要字段。
- [OpenAI 官方 skills 文档](https://learn.chatgpt.com/docs/build-skills) 用于核对项目级技能发现与 `SKILL.md` 格式。
