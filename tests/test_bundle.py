import importlib.util
import re
import tempfile
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents/skills/research-copilot'
spec = importlib.util.spec_from_file_location('init_memory', SKILL / 'scripts/init_memory.py')
initializer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(initializer)


class BundleChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (ROOT / 'tmp/checks').mkdir(parents=True, exist_ok=True)

    def test_native_roles_parse(self):
        names = set()
        for path in (ROOT / '.codex/agents').glob('*.toml'):
            role = tomllib.loads(path.read_text(encoding='utf-8'))
            self.assertEqual(set(role), {'name', 'description', 'developer_instructions'})
            self.assertEqual(role['name'], path.stem)
            self.assertTrue(role['developer_instructions'].strip())
            names.add(role['name'])
        self.assertEqual(names, {'literature_analyst', 'innovation_reviewer', 'experiment_engineer', 'result_analyst'})

    def test_local_markdown_references_resolve(self):
        for path in SKILL.rglob('*.md'):
            for reference in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' not in reference:
                    self.assertTrue((path.parent / reference.split('#')[0]).is_file(), (path, reference))

    def test_upstream_workflows_exist(self):
        provider = ROOT / '.agents/skills/academic-research-suite'
        self.assertTrue((provider / 'SKILL.md').is_file())
        for name in ['deep-research', 'experiment-agent', 'academic-paper', 'academic-paper-reviewer', 'academic-pipeline', 'sr-screener']:
            self.assertTrue((provider / 'ars' / name / 'WORKFLOW.md').is_file(), name)
        self.assertTrue((provider / 'ars/deep-research/agents/devils_advocate_agent.md').is_file())

    def test_initialization_is_idempotent(self):
        with tempfile.TemporaryDirectory() as folder:
            first = initializer.initialize(folder)
            self.assertEqual(len(first['created']), 3)
            memory = Path(folder) / 'memory'
            target = memory / '00_Current_State.md'
            target.write_text('用户手写进度\n', encoding='utf-8')
            second = initializer.initialize(folder)
            self.assertEqual(second['created'], [])
            self.assertEqual(len(second['preserved']), 3)
            self.assertEqual(target.read_text(encoding='utf-8'), '用户手写进度\n')
            self.assertEqual(len(list(memory.iterdir())), 3)

    def test_existing_memory_is_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            memory = Path(folder) / 'memory'
            memory.mkdir()
            target = memory / '06_Decision_Log.md'
            target.write_text('失败记录必须保留', encoding='utf-8')
            initializer.initialize(folder)
            self.assertEqual(target.read_text(encoding='utf-8'), '失败记录必须保留')

    def test_relative_or_skill_roots_are_rejected(self):
        with self.assertRaises(ValueError):
            initializer.initialize('.')
        with self.assertRaises(ValueError):
            initializer.initialize(SKILL)
        with self.assertRaises(FileNotFoundError):
            initializer.initialize(ROOT / 'missing-research-project')

    def test_configuration_bundle_roots_are_rejected(self):
        for folder in (ROOT, ROOT / 'tmp/checks'):
            with self.subTest(folder=folder):
                with self.assertRaises(ValueError):
                    initializer.initialize(folder)

    def test_project_memories_are_independent(self):
        with tempfile.TemporaryDirectory() as folder:
            first = Path(folder) / 'project-a'
            second = Path(folder) / 'project-b'
            first.mkdir()
            second.mkdir()
            initializer.initialize(first)
            initializer.initialize(second)
            first_state = first / 'memory/00_Current_State.md'
            second_state = second / 'memory/00_Current_State.md'
            first_state.write_text('Project A direction', encoding='utf-8')
            initializer.initialize(second)
            self.assertEqual(first_state.read_text(encoding='utf-8'), 'Project A direction')
            self.assertNotIn('Project A direction', second_state.read_text(encoding='utf-8'))


if __name__ == '__main__':
    (ROOT / 'tmp/checks').mkdir(parents=True, exist_ok=True)
    unittest.main()
