# Python Quiz

A simple terminal quiz built to practice Python foundations as I work toward learning data analysis and machine learning.

## Features

- Three multiple-choice questions about Python.
- Accepts uppercase and lowercase answers and removes surrounding spaces.
- Asks again when an answer is not A, B, or C.
- Shows feedback after each answer and a final score.

## How to run

You need Python 3. No extra packages are required.

1. Download this repository using **Code > Download ZIP** and extract it.
2. Open a terminal in the extracted folder containing `quiz_game.py`.
3. Run:

```bash
python quiz_game.py
```

On Windows, if `python` is unavailable, try `py quiz_game.py`.

Enter A, B, or C for each question.

## Concepts practiced

- Variables and strings
- String methods: `strip()` and `upper()`
- Conditions and membership checks
- Functions, parameters, arguments, and return values
- Lists and dictionaries
- `for` and `while` loops
- Score tracking with `+=`
- String formatting and `len()`

## Adding a question

Add another dictionary to the `questions` list using the same keys: `question`, `a`, `b`, `c`, and `correct_answer`. Use A, B, or C for the correct answer. The final score total updates automatically.
