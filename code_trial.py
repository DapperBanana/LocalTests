
def ask_question(question, options, correct_answer):
    print(question)
    print("Options:")
    for i, option in enumerate(options):
        print(str(i+1) + ". " + option)
    
    answer = input("Enter the correct option number: ")
    
    if options[int(answer) - 1] == correct_answer:
        return True
    else:
        return False

# Define quiz questions, options, and correct answers
questions = [
    "What is the capital of France?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the powerhouse of the cell?"
]

options = [
    ["Paris", "London", "Berlin", "Madrid"],
    ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
    ["Mitochondria", "Nucleus", "Ribosome", "Endoplasmic reticulum"]
]

correct_answers = ["Paris", "William Shakespeare", "Mitochondria"]

# Run the quiz
score = 0
for i in range(len(questions)):
    if ask_question(questions[i], options[i], correct_answers[i]):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print("Quiz complete! You scored {} out of {}".format(score, len(questions)))
