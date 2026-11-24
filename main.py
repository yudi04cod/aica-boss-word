#!/usr/bin/env python3
"""Write one word describing a boss to /output/entry.txt.

Competition: u-swift-badger-44-one-word-for-the-boss-6b48c735
"One Word for the Boss" — exactly one word, up to 30 characters,
no phrase, no caption, no explanation. A judge model compares words
pairwise on funniness, truth and freshness.

The program scores a shortlist of candidate words against the judge's
own five criteria — a real boss word, funny on its own, rings true,
fresh, travels across industries — and writes the winner.
Deterministic: the same word, byte for byte, on every run.
Standard library only, no network.
"""

import os

# (word, funny, true, fresh, travels) — each criterion scored 0-5.
# The judge weighs them in this order, so the score tuple is compared
# lexicographically: a word must first be a word people actually use
# about their boss, then be funny, then true, then fresh, then travel.
CANDIDATES = [
    # The boss who passes every task down the chain and keeps only the
    # credit: the one habit every office, kitchen and warehouse shares.
    ("Delegator", 4, 5, 4, 5),
    # The boss who is never there when you need a decision.
    ("Unreachable", 3, 4, 3, 4),
    # The boss who only exists in CC, watching without answering.
    ("Cc", 3, 3, 4, 2),
    # The boss who speaks only in corporate jargon.
    ("Synergy", 4, 3, 4, 3),
    # The boss who reads your message and never replies.
    ("Ghoster", 3, 4, 3, 4),
    # The first word anyone reaches for — true, but no surprise left.
    ("Micromanager", 2, 5, 1, 4),
    # The boss who is always in a meeting about meetings.
    ("Meeting", 3, 4, 2, 3),
]


def pick_word(candidates):
    """Return the candidate with the best lexicographic criteria score.

    Ties go to the earlier candidate, so the shortlist order is the
    final tie-break: the freshest true word is listed first.
    """
    best_word, best_score = None, None
    for word, funny, true, fresh, travels in candidates:
        score = (funny, true, fresh, travels)
        if best_score is None or score > best_score:
            best_word, best_score = word, score
    return best_word


def validate(word):
    """Check the gate: one word, 1-30 characters, not only whitespace."""
    if not word or not word.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(word) > 30:
        raise ValueError("entry must be at most 30 characters, got %d" % len(word))
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no spaces")
    if not word.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    return word


def main():
    word = validate(pick_word(CANDIDATES))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
