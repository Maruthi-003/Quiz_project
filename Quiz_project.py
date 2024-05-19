# Constants for the quiz
CORRECT_ANSWER_POINTS = 4
INCORRECT_ANSWER_POINTS = -1
NUM_QUESTIONS = 5
MAX_SCORE = NUM_QUESTIONS * CORRECT_ANSWER_POINTS

# Questions that are going to be asked
questions = [
    "What is the correct file extension for Python files?",
    "How do you print Hello, World! in Python?",
    "Which of the following is a correct way to create a list in Python?",
    "What is the output of the following code: `print(type(5))`?",
    "How do you start a comment in Python?"
]

# Options for the above questions
options = [
    [".py", ".python", ".pyt", ".pt"],
    ['print("Hello, World!")', 'echo "Hello, World!"', 'printf("Hello, World!")', 'cout << "Hello, World!"'],
    ["list = {1, 2, 3}", "list = (1, 2, 3)", "list = [1, 2, 3]", "list = <1, 2, 3>"],
    ["<class 'float'>", "<class 'str'>", "<class 'int'>", "<class 'list'>"],
    ["//", "#", "/*", "<!--"]
]

# Correct answers for the questions
correct_answers = [1, 1, 3, 3, 2]

# Function to display the welcome message and instructions
def display_welcome_message():
    print("Welcome to the Python quiz")
    print("-------------Instructions--------------")
    print(f"This quiz contains {NUM_QUESTIONS} basic questions related to Python programming.")
    print("Each question contains 4 options and a single correct answer.")
    print("Please respond with one of the following options: 1, 2, 3, or 4.")
    print(f"Each correct answer awards {CORRECT_ANSWER_POINTS} points, while each incorrect answer deducts {INCORRECT_ANSWER_POINTS} point.")

# Function to get valid input from the user
def get_valid_input(prompt, valid_range):
    while True:
        try:
            guess = int(input(prompt))
            if guess in valid_range:
                return guess
            else:
                print(f"Please enter a number between {valid_range[0]} and {valid_range[-1]}")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to evaluate the user's answer and update the score
def evaluate(guess, correct_answer, score):
    if guess == correct_answer:
        print(f"Correct, you have scored {CORRECT_ANSWER_POINTS} points")
        score += CORRECT_ANSWER_POINTS
    else:
        print("Oops, you have chosen the incorrect option")
        print(f"The correct answer is option {correct_answer}")
        score += INCORRECT_ANSWER_POINTS
    return score

# Function to provide a complement based on the user's total score
def provide_complement(score):
    if score == MAX_SCORE:
        return "Excellent! You got all answers right!"
    elif 15 <= score < MAX_SCORE:
        return "Good job! Keep it up!"
    elif 10 <= score < 15:
        return "Nice effort! You're getting there!"
    elif 5 <= score < 10:
        return "Keep trying! Practice makes perfect!"
    else:
        return "Don't give up! Keep learning and you'll improve!"

# Main function to conduct the quiz
def quiz(questions, options):
    score = 0
    display_welcome_message()

    # Loop through each question
    for i in range(NUM_QUESTIONS):
        print(f"{i + 1}. {questions[i]}")
        # Display the options for the current question
        for j in range(len(options[i])):
            print(f"{j + 1}) {options[i][j]}")
        # Get the user's answer and evaluate it
        guess = get_valid_input("Please select one of the options provided above: ", range(1, 5))
        score = evaluate(guess, correct_answers[i], score)
    
    # Display the user's total score and complement
    print(f"Your total score is {score}/{MAX_SCORE}")
    print(provide_complement(score))

# Run the quiz
quiz(questions, options)
