#!/usr/bin/env python3
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

SECTION_RE = re.compile(r"^섹션\s*\d+$")

def find_solved_problem_names() -> set[str]:
    """
    solved 기준:
      - 경로가 '섹션 N/<문제폴더>/' 형태
      - 그 문제폴더 내부에 .py 파일이 하나라도 있으면 solved
    반환:
      - README 체크리스트에 쓰인 문제 폴더명 (예: '1. 이분검색') set
    """
    solved = set()

    for section_dir in ROOT.iterdir():
        if not section_dir.is_dir():
            continue
        if not SECTION_RE.match(section_dir.name):
            continue

        for problem_dir in section_dir.iterdir():
            if not problem_dir.is_dir():
                continue
            # 문제 폴더 내부에 .py 있으면 solved
            has_py = any(p.suffix == ".py" for p in problem_dir.glob("*.py"))
            if has_py:
                solved.add(problem_dir.name)

    return solved

def update_readme(readme_text: str, solved_names: set[str]) -> str:
    """
    README 라인의 패턴:
      - [ ] <문제폴더명>
      - [x] <문제폴더명>
    문제폴더명이 solved_names에 있으면 [x]로 바꿈.
    """
    out_lines = []
    line_re = re.compile(r"^(\s*-\s*\[)( |x|X)(\]\s+)(.+?)\s*$")

    for line in readme_text.splitlines():
        m = line_re.match(line)
        if not m:
            out_lines.append(line)
            continue

        prefix, checked, mid, title = m.groups()
        title = title.strip()

        if title in solved_names:
            out_lines.append(f"{prefix}x{mid}{title}")
        else:
            out_lines.append(f"{prefix} {mid}{title}")

    return "\n".join(out_lines) + ("\n" if readme_text.endswith("\n") else "")

def main():
    if not README.exists():
        raise SystemExit("README.md not found at repo root")

    solved = find_solved_problem_names()
    original = README.read_text(encoding="utf-8")
    updated = update_readme(original, solved)

    if updated != original:
        README.write_text(updated, encoding="utf-8")
        print("README updated")
    else:
        print("README already up to date")

if __name__ == "__main__":
    main()