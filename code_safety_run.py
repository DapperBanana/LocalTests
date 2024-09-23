
def quiz():
    questions = [
        {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "What is the largest mammal in the world?", "options": ["Elephant", "Giraffe", "Blue whale", "Hippopotamus"], "answer": "Blue whale"},
        {"question": "Who painted the Mona Lisa?", "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], "answer": "Leonardo da Vinci"},
        {"question": "What is the hottest planet in our solar system?", "options": ["Earth", "Venus", "Mars", "Mercury"], "answer": "Venus"},
        {"question": "Which country is known as the Land of the Rising Sun?", "options": ["China", "India", "Japan", "Australia"], "answer": "Japan"}
    ]
    
    score = 0
    
    for i, question in enumerate(questions):
        print(f"Question {i+1}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{j+1}. {option}")
        
        user_answer = input("Enter the number corresponding to your answer: ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")
    
    print(f"Quiz completed! You scored: {score}/{len(questions)}")
    
quiz()
