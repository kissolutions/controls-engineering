#!/usr/bin/env python3
"""Build an offline, single-file Modbus 001 training demo from a frozen engine and lesson stubs.

Standard library only. Execute from any working directory:
    python training/tools/build_modbus_001.py

The v0.2 baseline is read-only. This build is an incremental extraction: the
academic lessons and scenario data are externalized; older playbook/quiz
demonstration logic still lives in the legacy shell until a later milestone.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path

TRAINING = Path(__file__).resolve().parents[1]
COURSE = TRAINING / "courses" / "modbus-001"
BASELINE = TRAINING / "engine" / "baselines" / "v0.2" / "index.html"
OUTPUT = TRAINING / "engine" / "prototypes" / "v0.3" / "modbus-001.html"
WIDGET_JS = TRAINING / "engine" / "src" / "academic-widgets.js"
WIDGET_CSS = TRAINING / "engine" / "src" / "academic.css"


def replace_once(source: str, original: str, replacement: str, label: str) -> str:
    count = source.count(original)
    if count != 1:
        raise ValueError(f"Expected one {label} anchor; found {count}")
    return source.replace(original, replacement, 1)


def replace_between(source: str, start: str, end: str, replacement: str, label: str) -> str:
    if source.count(start) != 1 or source.count(end) != 1:
        raise ValueError(f"Expected unique {label} anchors")
    i = source.index(start) + len(start)
    j = source.index(end, i)
    return source[:i] + replacement + source[j:]


def build() -> tuple[Path, str]:
    manifest = json.loads((COURSE / "course.json").read_text(encoding="utf-8"))
    lessons = manifest["sections"][0]["items"]
    ids = [lesson["id"] for lesson in lessons]
    if len(ids) != len(set(ids)) or "overview" not in ids:
        raise ValueError("Duplicate lesson ID or missing overview")

    html_stubs = []
    navigation = []
    for item in lessons:
        stub = (COURSE / item["file"]).read_text(encoding="utf-8").strip()
        anchor = f'id="learn-{item["id"]}"'
        if stub.count(anchor) != 1 or not stub.startswith("<article "):
            raise ValueError(f"Lesson stub requires one stable article anchor: {item['id']}")
        if '<script' in stub.lower():
            raise ValueError("Lesson stubs must remain declarative HTML, not executable JS")
        html_stubs.append(stub)
        label = "Course overview" if item["id"] == "overview" else f'{item["number"]} · {item["title"]}'
        navigation.append(
            f'<button class="subitem" data-learning="{html.escape(item["id"])}">'
            f'{html.escape(label)}</button>'
        )
    data = {"scenarios": []}
    for definition in manifest["interactive_scenarios"]:
        if "file" not in definition:
            continue
        scene = json.loads((COURSE / definition["file"]).read_text(encoding="utf-8"))
        if scene["id"] != definition["id"]:
            raise ValueError("Scenario ID and manifest do not match")
        stage_ids = [stage["id"] for stage in scene["stages"]]
        if len(stage_ids) != len(set(stage_ids)):
            raise ValueError("Duplicate scenario stage ID")
        for stage in scene["stages"]:
            nodes = {node["id"] for node in stage["nodes"]}
            for edge in stage["links"]:
                if edge["from"] not in nodes or edge["to"] not in nodes:
                    raise ValueError("Scenario edge references missing node")
        data["scenarios"].append(scene)

    output = BASELINE.read_text(encoding="utf-8")
    output = replace_between(
        output,
        '<div class="subnav" data-subnav="intro" hidden>',
        '</div><button class="navitem active" data-chapter="playbook"',
        "".join(navigation),
        "academic navigation",
    )
    output = replace_between(
        output,
        '<div id="academicLessons">',
        '</div><div class="footerbar"><button class="btn" id="learnPrev"',
        "".join(html_stubs),
        "academic lessons",
    )
    output = replace_once(
        output,
        "const learningIds=['overview','principles','physical','registers','gateway'];",
        "const learningIds=" + json.dumps(ids, ensure_ascii=False, separators=(",", ":")) + ";",
        "academic lesson order",
    )
    output = replace_once(output, "PROTOTYPE 0.2", "COURSE BUILD 0.3", "version label")
    output = replace_once(
        output,
        "Sidebar chapters · linked steps · diagram stages · simulated faults · calculators · saved progress",
        "Modbus 001 · independent lessons · editable scenarios · preserved v0.2 playbook demo",
        "sidebar note",
    )
    output = replace_once(
        output,
        "localStorage.getItem('kis-course-progress')",
        "localStorage.getItem('kis-modbus-001-v03-playbook-progress')",
        "progress read key",
    )
    output = replace_once(
        output,
        "localStorage.setItem('kis-course-progress',",
        "localStorage.setItem('kis-modbus-001-v03-playbook-progress',",
        "progress write key",
    )
    # Open on academic overview; the v0.2 demonstration opened on playbook step 4.
    start = "switchChapter('playbook');document.querySelector('[data-subnav=\"playbook\"]').hidden=false;document.querySelector('[data-chapter=\"playbook\"]').setAttribute('aria-expanded','true');document.querySelector('[data-chapter=\"playbook\"] .chev').textContent='▾'"
    new_start = "showLearning('overview');document.querySelector('[data-subnav=\"intro\"]').hidden=false;document.querySelector('[data-chapter=\"intro\"]').setAttribute('aria-expanded','true');document.querySelector('[data-chapter=\"intro\"] .chev').textContent='▾'"
    output = replace_once(output, start, new_start, "academic launch state")
    output = replace_once(output, "</style>", WIDGET_CSS.read_text(encoding="utf-8") + "</style>", "academic CSS")
    scenario_text = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    injection = (
        '\n<script type="application/json" id="kisScenarioData">' + scenario_text + "</script>"
        '\n<script>' + WIDGET_JS.read_text(encoding="utf-8") + "</script>"
    )
    output = replace_once(output, "</body>", injection + "\n</body>", "academic interaction scripts")
    if output.count('class="card learning-block"') != len(lessons):
        raise ValueError("Lesson output count differs from manifest")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(output, encoding="utf-8")
    return OUTPUT, hashlib.sha256(output.encode("utf-8")).hexdigest()


if __name__ == "__main__":
    path, digest = build()
    print(f"Built {path.relative_to(TRAINING)}")
    print(f"SHA-256 {digest}")
