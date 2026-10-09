def ask_question(question, a, b, c, correct_answer):
    print(question, a, b, c, sep="\n")

    answer = input("What's your answer? ").strip().upper()

    while answer not in ("A", "B", "C"):
        print("Please enter A, B, or C.")
        answer = input("What's your answer? ").strip().upper()

    if answer == correct_answer:
        print("Correct answer!\n")
        return 1
    else:
        print(f"Wrong answer. The answer is {correct_answer}.\n")
        return 0


questions = [
    {
        "question": "Which Python data type stores True or False?",
        "a": "A. str",
        "b": "B. bool",
        "c": "C. int",
        "correct_answer": "B"
    },
    {
        "question": "Which Python data type stores text?",
        "a": "A. str",
        "b": "B. bool",
        "c": "C. int",
        "correct_answer": "A"
    },
    {
        "question": "Which Python data type is immutable?",
        "a": "A. list",
        "b": "B. dict",
        "c": "C. tuple",
        "correct_answer": "C"
    }
]

print("Welcome to the Python Quiz!\n")
score = 0

for item in questions:
    score += ask_question(
        item["question"],
        item["a"],
        item["b"],
        item["c"],
        item["correct_answer"]
    )

print(f"You scored {score} out of {len(questions)}!")