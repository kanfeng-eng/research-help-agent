# 环境与实现记录

核对日期为 2026-11-13。

## 初始状态

当前科研目录为 `C:/Users/kanfe/Desktop/科研/无人机的小目标检测`，包含论文与研究规划，目录自身未初始化 Git。`dl_agent` 初始不存在，父目录未发现已有项目级 `AGENTS.md`、skills、agents 或 `memory/`。用户级编码指南和现有论文阅读技能保持原位置。

## 当前 Codex

- PATH 中 npm CLI 为 `0.144.6`。
- 桌面程序自带 CLI 为 `0.167.0-alpha.4.1`，使用该版本核对项目级发现。
- 当前会话提供原生 spawn、send、wait、close 子 agent 工具。
- 官方当前格式为项目 `.codex/agents/*.toml`，必要字段为 name、description、developer_instructions。
- 本地项目 skills 放在 `.agents/skills/`。本包创建 research-copilot，并安装固定提交的完整 academic-research-suite。

本包没有修改用户级 config.toml 或全局 agent 目录，没有写入主机全局记忆。原生角色使用继承模型与权限，项目本身无需新增 config.toml。

## 安装与可迁移性

系统 skill-installer 的 ZIP 全仓解压遇到 Windows 临时路径长度限制，随后改为下载固定提交归档，只提取指定 skill 子树，校验目标路径并使用 Windows 扩展长度文件路径写入。上游文件保持原样，归档 SHA-256 和提交保存在 upstream-lock.json。

包内 ARS 约 37 MiB，保留完整资源和许可。它是可直接读取的文件依赖，项目记忆与外部论文路径由实际科研会话明确指定。

## 验证边界

结构、格式、引用路径与初始化保护由本地测试验证。原生角色发现、工作流 A—J 情景检查及执行记录以 tmp/checks 的实际结果为准。真实论文新颖性和 GPU 实验留待相应科研任务检验。

当前对话加载的角色和技能目录可能在新会话中更新。以 `dl_agent` 打开项目后重新开始会话，可以让项目级配置参与正常发现；以其他目录启动时，需要明确提供本包入口路径。

## 原生角色调用测试

桌面自带 CLI 的只读 smoke test 实际发起了新会话。会话报告其 spawn 接口缺少自定义角色选择参数，因此没有按 result_analyst 类型生成子 agent，结果记为受限。当前主会话提供的 spawn 工具同样只接受任务、上下文和模型等字段。

实现采用明确的角色指令传递作为后备方式，原生 TOML 保留给支持自定义类型加载的客户端。TOML 解析通过、原生子 agent 实际运行、以及自定义类型直接加载，三个状态分别记录。
