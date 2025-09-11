
def main():
    print("Welcome to the Personality Quiz!")
    
    questions = [
        "1. When faced with a difficult decision, are you more likely to: \n a) Follow your head \n b) Follow your heart",
        "2. How do you typically handle stress: \n a) Stay calm and rational \n b) Seek emotional support from others",
        "3. Which describes you best: \n a) Introverted, prefer alone time \n b) Extroverted, thrive in social settings"
    ]
    
    answers = []
    
    for question in questions:
        answer = input(question)
        while answer.lower() not in ['a', 'b']:
            print("Please enter a valid answer (a or b)")
            answer = input(question)
        answers.append(answer)
    
    a_count = answers.count('a')
    b_count = answers.count('b')
    
    if a_count > b_count:
        print("You are more logical and introverted")
    elif b_count > a_count:
        print("You are more emotional and extroverted")
    else:
        print("You are a balance of both traits")
    
if __name__ == "__main__":
    main()
