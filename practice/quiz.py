#!/usr/bin/env python3
"""NCA-AIIO practice quiz runner (Python 3.8+, no extra packages).

Examples:
    python quiz.py --exam 1               # mock exam 1: 50 questions, 60-minute timer
    python quiz.py --random 50            # 50 random questions, weighted like the real exam
    python quiz.py --domain 2             # all Domain 2 questions
    python quiz.py --topic 3.3            # one blueprint topic
    python quiz.py --review               # retry the questions you missed last time
"""
import argparse
import json
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
BANK = HERE / "bank"
MISSED = HERE / ".missed.json"
WEIGHTS = {"1": 19, "2": 20, "3": 11}  # 38% / 40% / 22% of 50
NOTES = {
    "1": "01-essential-ai-knowledge", "2": "02-ai-infrastructure", "3": "03-ai-operations",
}


def load():
    qs = []
    for d in ("1", "2", "3"):
        for q in json.loads((BANK / f"domain{d}.json").read_text()):
            q["domain"] = d
            qs.append(q)
    return qs


def exam_set(qs, n):
    out = []
    for d in ("1", "2", "3"):
        dq = [q for q in qs if q["domain"] == d]
        out += [q for i, q in enumerate(dq) if i % 3 == n - 1]
    return out


def weighted_random(qs, total):
    out = []
    for d, w in WEIGHTS.items():
        dq = [q for q in qs if q["domain"] == d]
        out += random.sample(dq, min(len(dq), round(w * total / 50)))
    return out


def ask(q, num, total):
    order = list(range(len(q["options"])))
    random.shuffle(order)
    letters = "ABCD"
    print(f"\n[{num}/{total}] ({q['topic']}) {q['q']}")
    for i, oi in enumerate(order):
        print(f"   {letters[i]}. {q['options'][oi]}")
    while True:
        a = input("Answer (A-D, s=skip, q=quit): ").strip().upper()
        if a in ("Q", "S") or (len(a) == 1 and a in letters[: len(order)]):
            break
    if a == "Q":
        return None
    correct_letter = letters[order.index(q["answer"])]
    ok = a != "S" and order[letters.index(a)] == q["answer"]
    print("   ✅ Correct." if ok else f"   ❌ Correct answer: {correct_letter}. {q['options'][q['answer']]}")
    print(f"   ↳ {q['explain']}")
    return ok


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group()
    g.add_argument("--exam", type=int, choices=[1, 2, 3])
    g.add_argument("--random", type=int)
    g.add_argument("--domain", choices=["1", "2", "3"])
    g.add_argument("--topic")
    g.add_argument("--review", action="store_true")
    p.add_argument("--minutes", type=int, default=60)
    p.add_argument("--seed", type=int)
    a = p.parse_args()
    if a.seed is not None:
        random.seed(a.seed)

    qs = load()
    if a.exam:
        sel = exam_set(qs, a.exam)
    elif a.random:
        sel = weighted_random(qs, a.random)
    elif a.domain:
        sel = [q for q in qs if q["domain"] == a.domain]
    elif a.topic:
        sel = [q for q in qs if q["topic"] == a.topic]
    elif a.review:
        ids = set(json.loads(MISSED.read_text())) if MISSED.exists() else set()
        sel = [q for q in qs if q["id"] in ids]
        if not sel:
            print("No missed questions saved yet.")
            return
    else:
        sel = weighted_random(qs, 50)
    random.shuffle(sel)

    timed = bool(a.exam or a.random)
    start = time.time()
    print(f"{len(sel)} questions." + (f" Time limit: {a.minutes} min (~72 s per question)." if timed else ""))
    score = defaultdict(lambda: [0, 0])
    missed = []
    for i, q in enumerate(sel, 1):
        if timed and time.time() - start > a.minutes * 60:
            print("\n⏰ Time is up.")
            break
        r = ask(q, i, len(sel))
        if r is None:
            break
        score[q["domain"]][1] += 1
        score[q["topic"]][1] += 1
        if r:
            score[q["domain"]][0] += 1
            score[q["topic"]][0] += 1
        else:
            missed.append(q)

    answered = sum(score[d][1] for d in "123")
    right = sum(score[d][0] for d in "123")
    if not answered:
        return
    mins = (time.time() - start) / 60
    print("\n" + "=" * 60)
    print(f"SCORE: {right}/{answered} = {right/answered:.0%}   time: {mins:.1f} min")
    for d in "123":
        if score[d][1]:
            print(f"  Domain {d}: {score[d][0]}/{score[d][1]} = {score[d][0]/score[d][1]:.0%}")
    print("Target: 80%+ on every mock exam before you book the real exam.")
    weak = sorted({q["topic"] for q in missed})
    if weak:
        print("\nReview these topics:")
        for t in weak:
            d = t.split(".")[0]
            print(f"  {t}: see {NOTES[d]}/{t}-*.md")
    MISSED.write_text(json.dumps([q["id"] for q in missed]))
    print(f"\nMissed questions saved. Run: python {Path(sys.argv[0]).name} --review")


if __name__ == "__main__":
    main()
