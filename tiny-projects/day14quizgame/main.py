def main():

    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    
    quiz = [

    {"question" : "What is the out of: print(3 * 2 + 1)?", "answer" : "7"},
    {"question" : "Which data type stores True or False?", "answer" : "Boolean"},
    {"question" : "What symbol starts a comment in Python?", "answer" : "#"},
    {"question" : "What is the file extension for Python files?", "answer" : ".py"},
    {"question" : "Which function gets user input?", "answer" : "input()"}

    ]

    score = 0

    for i, question in enumerate(quiz, start =1):
        print(question["question"])
        user_answer = input("What is your answer?").lower()
        if user_answer == question["answer"].lower():
            print(GREEN + "Correct" + RESET)
            score += 1
        else:
            print(RED + "Wrong" + RESET)
    total_questions = len(quiz)
    percentage = (score / total_questions) * 100
    print(f"You got {score} out of 5 correct")
    print(f"Your score: {percentage}%")

main()

