def quiz_game():
    questions = {
        "How to say 'bureau de change' in Mandarin?": "兑换处",
        "How to say 'default (setting)' in Mandarin?": "缺省",
        "What does '沮丧' mean?": "Depressed",
        "How to say 'rational' in Mandarin?": "合理",
        "How to say 'to disappear' in Mandarin?": "消失"
    }

    score = 0
    for question, correct_answer in questions.items():
        print("\n" + question)
        user_answer = input("Your answer: ").strip()
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the quiz game!")
    quiz_game()
    print("Thanks for playing!")