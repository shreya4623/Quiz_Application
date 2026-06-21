import random


QUESTIONS = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": ["class", "def", "func", "lambda"],
        "answer": 1,
    },
    {
        "question": "Which data type is ordered and mutable?",
        "options": ["tuple", "str", "list", "int"],
        "answer": 2,
    },
    {
        "question": "What does random.shuffle() do?",
        "options": [
            "Returns a new shuffled list",
            "Shuffles a list in place",
            "Picks one random item",
            "Sorts a list randomly",
        ],
        "answer": 1,
    },
    {
        "question": "How do you access the first item in a list named items?",
        "options": ["items[1]", "items.first()", "items[0]", "items(0)"],
        "answer": 2,
    },
    {
        "question": "Which module provides random number utilities?",
        "options": ["math", "random", "os", "sys"],
        "answer": 1,
    },
    {
        "question": "What is the result of len([10, 20, 30])?",
        "options": ["30", "10", "3", "6"],
        "answer": 2,
    },
    {
        "question": "Which symbol starts a single-line comment in Python?",
        "options": ["//", "#", "--", "/*"],
        "answer": 1,
    },
    {
        "question": "What type does 3.14 have?",
        "options": ["int", "float", "str", "bool"],
        "answer": 1,
    },
]


def randomize_questions(questions):
    """Return a new list with questions in random order."""
    shuffled = questions.copy()
    random.shuffle(shuffled)
    return shuffled


def display_question(question, question_number, total_questions):
    """Print a multiple-choice question and its options."""
    print(f"\nQuestion {question_number} of {total_questions}")
    print(question["question"])
    print()

    for index, option in enumerate(question["options"]):
        print(f"  {index + 1}. {option}")


def get_user_answer(option_count):
    """Read and validate the user's answer choice."""
    while True:
        choice = input(f"Enter your answer (1-{option_count}): ").strip()

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice_number = int(choice)
        if 1 <= choice_number <= option_count:
            return choice_number - 1

        print(f"Please choose a number between 1 and {option_count}.")


def calculate_score(questions, user_answers):
    """Count how many answers are correct."""
    score = 0

    for question, user_answer in zip(questions, user_answers):
        if user_answer == question["answer"]:
            score += 1

    return score


def display_results(score, total_questions, questions, user_answers):
    """Show the final score and a short review."""
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 40)
    print("QUIZ RESULTS")
    print("=" * 40)
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.0f}%")

    if percentage == 100:
        print("Excellent! Perfect score!")
    elif percentage >= 70:
        print("Great job! You passed the quiz.")
    else:
        print("Keep practicing. Review the questions below.")

    print("\nReview:")
    for index, (question, user_answer) in enumerate(
        zip(questions, user_answers), start=1
    ):
        correct_index = question["answer"]
        correct_text = question["options"][correct_index]
        user_text = question["options"][user_answer]
        status = "Correct" if user_answer == correct_index else "Wrong"

        print(f"\n{index}. {question['question']}")
        print(f"   Your answer: {user_text}")
        if status == "Wrong":
            print(f"   Correct answer: {correct_text}")
        print(f"   Result: {status}")


def run_quiz(questions):
    """Run the full quiz flow."""
    quiz_questions = randomize_questions(questions)
    user_answers = []
    total_questions = len(quiz_questions)

    print("Welcome to the Python Quiz!")
    print("Answer each multiple-choice question by typing its number.")

    for index, question in enumerate(quiz_questions, start=1):
        display_question(question, index, total_questions)
        answer = get_user_answer(len(question["options"]))
        user_answers.append(answer)

    score = calculate_score(quiz_questions, user_answers)
    display_results(score, total_questions, quiz_questions, user_answers)


def main():
    run_quiz(QUESTIONS)


if __name__ == "__main__":
    main()
