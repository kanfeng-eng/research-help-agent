"""Initialize minimal project research records while preserving existing files."""
import argparse
import json
from pathlib import Path


def initialize(project_root):
    requested = Path(project_root).expanduser()
    if not requested.is_absolute():
        raise ValueError('Project root must be an absolute path')
    root = requested.resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Project root must be an existing directory')
    protected = [
        Path.home() / '.codex' / 'memories',
        Path.home() / '.codex' / 'skills',
        Path.home() / '.agents' / 'skills',
        Path(__file__).resolve().parents[2],
    ]
    if any(root.is_relative_to(path.resolve()) for path in protected):
        raise ValueError('Choose the actual research project, outside skill and host memory directories')
    memory = root / 'memory'
    if not memory.resolve().is_relative_to(root):
        raise ValueError('The memory directory resolves outside the research project')
    memory.mkdir(exist_ok=True)
    files = {
        'README.md': '# 项目科研记忆\n\n先读取 00_Current_State.md 和 08_Research_Handoff.md，再按任务读取相关资料。\n\n正式记录由主 agent 审核维护，重要修改保留日期、来源和历史，失败结果继续保留。论文、IDEA 和实验记录按实际进度创建。\n',
        '00_Current_State.md': '# 当前研究状态\n\n科研项目根目录为本 memory 目录的父目录。\n\n本文件由初始化程序补建。研究方向、当前问题、约束与真实进展以现有资料和后续核对为准，请读取其余研究记录确认实际状态。\n',
        '08_Research_Handoff.md': '# 科研交接\n\n本文件由初始化程序补建。下次会话先读取当前状态及已有论文、决策和实验记录，再继续已经授权的工作。\n\n本次初始化只补充文件，研究结论和运行状态需从实际资料核对。\n',
    }
    result = {'project_root': str(root), 'created': [], 'preserved': []}
    for name, content in files.items():
        try:
            with (memory / name).open('x', encoding='utf-8', newline='\n') as handle:
                handle.write(content)
            result['created'].append(name)
        except FileExistsError:
            result['preserved'].append(name)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(initialize(args.project_root), ensure_ascii=False, indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f'{error}\n')


if __name__ == '__main__':
    main()
