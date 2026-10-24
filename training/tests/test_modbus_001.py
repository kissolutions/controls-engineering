"""Modbus 001 prototype build contract and arithmetic smoke tests."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

TRAINING = Path(__file__).resolve().parents[1]
COURSE = TRAINING / "courses" / "modbus-001"
DEMO = TRAINING / "engine" / "prototypes" / "v0.3" / "modbus-001.html"
BASELINE = TRAINING / "engine" / "baselines" / "v0.2" / "index.html"


class ScriptCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.content_type = ""
        self.chunks = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        if tag == "script":
            self.active = True
            self.content_type = dict(attrs).get("type", "")
            self.chunks = []

    def handle_data(self, data):
        if self.active:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.active:
            self.scripts.append((self.content_type, "".join(self.chunks)))
            self.active = False


class TrainingBuildTests(unittest.TestCase):
    def test_all_six_academic_articles_and_nav_entries_present(self):
        manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
        ids = [x["id"] for x in manifest["sections"][0]["items"]]
        self.assertEqual(len(ids), 6)
        built = DEMO.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r'class="card learning-block"', built)), len(ids))
        for slug in ids:
            self.assertIn(f'id="learn-{slug}"', built)
            self.assertIn(f'data-learning="{slug}"', built)

    def test_source_authority_is_explicit(self):
        manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
        for key, source in manifest["source_catalog"].items():
            self.assertIn(source["repo"], ("kissolutions/controls-engineering", "kissolutions/knowledgebase_wikijs"), key)
            self.assertTrue(source["url"].startswith("https://github.com/kissolutions/"))
            self.assertNotIn("/blob/draft/", source["url"])
        self.assertTrue(BASELINE.exists())
        self.assertIn("PROTOTYPE 0.2", BASELINE.read_text(encoding="utf-8"))
        self.assertIn("COURSE BUILD 0.3", DEMO.read_text(encoding="utf-8"))

    def test_normal_and_degraded_polling_example(self):
        tx = (13 + 2 * 10) * 11 / 19200 + 0.020 + 0.005
        normal = 30 * tx
        degraded_three = 27 * tx + 3 * (2 + 1) * 0.5
        self.assertAlmostEqual(normal, 1.3171875, places=3)
        self.assertAlmostEqual(normal / 5 * 100, 26.3, places=1)
        self.assertAlmostEqual(degraded_three, 5.68546875, places=3)

    @unittest.skipUnless(shutil.which("node"), "Node.js unavailable")
    def test_inline_javascript_syntax(self):
        parser = ScriptCollector()
        parser.feed(DEMO.read_text(encoding="utf-8"))
        js = [content for kind, content in parser.scripts if kind in ("", "text/javascript")]
        self.assertGreaterEqual(len(js), 2)
        for i, code in enumerate(js):
            with self.subTest(script=i):
                with tempfile.TemporaryDirectory() as directory:
                    path = Path(directory) / "script.js"
                    path.write_text(code, encoding="utf-8")
                    completed = subprocess.run(
                        ["node", "--check", str(path)], capture_output=True, text=True, check=False
                    )
                    self.assertEqual(completed.returncode, 0, completed.stderr)


if __name__ == "__main__":
    unittest.main()

