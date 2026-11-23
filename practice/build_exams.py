#!/usr/bin/env python3
"""Generate the three Markdown mock exams from the question bank.

    python build_exams.py
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
LETTERS = "ABCD"


def main():
    bank = {d: json.loads((HERE / "bank" / f"domain{d}.json").read_text()) for d in "123"}
    for n in (1, 2, 3):
        qs = []
        for d in "123":
            qs += [q for i, q in enumerate(bank[d]) if i % 3 == n - 1]
        lines = [
            f"# NCA-AIIO Mock Exam {n}",
            "",
            f"**{len(qs)} questions · 60 minutes · weighted 38% / 40% / 22% like the real exam.**",
            "",
            "Rules: set a 60-minute timer. Write your answers on paper. Do not open the answer key until you finish.",
            "Interactive version: `python practice/quiz.py --exam " + str(n) + "`",
            "",
        ]
        for i, q in enumerate(qs, 1):
            lines.append(f"### Q{i}. {q['q']}")
            lines.append("")
            for j, o in enumerate(q["options"]):
                lines.append(f"- {LETTERS[j]}. {o}")
            lines.append("")
        lines += ["---", "", "## Answer key", "", "<details><summary>Show answers (only after you finish)</summary>", "",
                  "| Q | Answer | Topic | Why |", "|---|---|---|---|"]
        for i, q in enumerate(qs, 1):
            why = q["explain"].replace("|", "/")
            lines.append(f"| {i} | **{LETTERS[q['answer']]}** | {q['topic']} | {why} |")
        lines += ["", "</details>", "",
                  "**Score guide:** 40+/50 (80%) = ready. 35–39 = review weak topics. Below 35 = repeat the study plan week for weak domains."]
        (HERE / f"mock-exam-{n}.md").write_text("\n".join(lines) + "\n")
        print(f"mock-exam-{n}.md: {len(qs)} questions")


if __name__ == "__main__":
    main()
