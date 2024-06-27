letion(id='chatcmpl-9enrQJActn4jkJoVZOAFSZKO8eaFD', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

# Quiz questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the powerhouse of the cell?": "Mitochondria",
    "What is the largest mammal in the world?": "Blue whale",
    "What is the closest planet to the Sun?": "Mercury"
}

# Function to display quiz questions, get user input, and check answers
def run_quiz():
    score = 0
    for question in questions:
        print(question)
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == questions[question].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {questions[question]}\n")

    print(f"You scored {score}/{len(questions)}")

# Function to shuffle quiz questions
def shuffle_questions():
    shuffled_questions = list(questions.keys())
    random.shuffle(shuffled_questions)
    
    return shuffled_questions

# Main function to run the quiz
def main():
    print("Welcome to the educational quiz!")
    print("Answer the following questions:")
    
    shuffled_questions = shuffle_questions()
    for question in shuffled_questions:
        print(question)
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == questions[question].lower():
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is: {questions[question]}\n")

    print("Quiz complete!")

if __name__ == "__main__":
    main()', role='assistant', function_call=None, tool_calls=None))], created=1719511812, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=348, prompt_tokens=21, total_tokens=369)