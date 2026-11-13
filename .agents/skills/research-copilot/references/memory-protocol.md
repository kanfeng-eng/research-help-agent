# 项目科研记忆

## 根目录与首次初始化

科研记忆位于用户当前指定的科研项目 `<project>/memory/`。配置包、技能目录与实际科研项目分别定位，项目可与配置包放在不同位置。无法确定根目录时只询问这一个必要信息。

确认项目后执行以下命令，脚本位置相对本 skill。

```powershell
python scripts/init_memory.py --project-root "<科研项目绝对路径>"
```

脚本只补充 `memory/README.md`、`00_Current_State.md`、`08_Research_Handoff.md`，已有文件保留。研究方向、论文与实验记录在实际产生内容时创建。使用绝对路径参数，避免把记忆初始化到技能安装目录。首次使用可直接按模板维护文件，Python 暂不可用时说明采用的方式。

## 按进展创建

| 路径 | 维护内容 |
| --- | --- |
| `01_Research_Direction.md` | 方向、范围、资源、历史调整 |
| `02_Researcher_Ideas.md` | 用户实际提出的猜想与判断，和 AI 推断分别标记 |
| `03_Literature_Index.md` | 论文 ID、版本、阅读范围和记录链接 |
| `papers/Paper_<ID>.md` | 单篇讨论及来源 |
| `04_Cross_Paper_Analysis.md` | 有来源的跨论文比较 |
| `05_Research_Gaps.md` | 观察、假设、潜在空白与状态 |
| `ideas/IDEA_<ID>.md` | 候选构想、反例及成熟度历史 |
| `experiments/<ID>/Experiment_Plan.md` | 预先记录的实验协议及预算 |
| `experiments/<ID>/Experiment_Log.md` | 执行配置、日志路径、失败和重试 |
| `experiments/<ID>/Result_Analysis.md` | 公平性、结果、解释和限制 |
| `06_Decision_Log.md` | 研究员决策、依据、日期及后续动作 |
| `07_Open_Questions.md` | 待核查和待回答事项 |

## 每次读写

启动先读索引、当前状态及交接，再有选择地读取相关记录。结束按本次实际增量更新对应文件，重要进展同步状态和交接。代码、数据、权重、大日志使用原项目目录，记忆记录路径、版本和摘要。

主 agent 统一写正式记忆。子 agent 默认返回可审查结果，修改实验代码时使用单独授权的写入范围。对正式记忆的改动先重新读取当前文件，检查是否有用户修改或同时更新。原结论被修正时追加日期、原因、证据与取代关系，保留负面结果、排除的 IDEA 和决定过程。

模板位于 `../templates/`。索引使用稳定 ID 和相对项目路径，源材料移动时更新对应定位。缺文件、过期运行记录或未知事实进入待核查项，避免补造历史。

这里的项目 `memory/` 与 Codex 主机全局记忆为独立系统。初始化或维护项目记忆时，写入范围限定在明确的科研项目。
