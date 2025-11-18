
def main():
    print("Welcome to the Personality Quiz!")
    
    questions = [
        "What is your favorite color? (a) Red (b) Blue (c) Green",
        "What is your favorite animal? (a) Dog (b) Cat (c) Bird",
        "What is your favorite season? (a) Summer (b) Winter (c) Spring",
    ]
    
    responses = []
    
    for question in questions:
        answer = input(question + "\n")
        responses.append(answer)
    
    score = 0
    for response in responses:
        if response == 'a':
            score += 1
        elif response == 'b':
            score += 2
        elif response == 'c':
            score += 3
    
    if score <= 3:
        print("You are a calm and laid-back person.")
    elif score <= 6:
        print("You are a fun and energetic person.")
    else:
        print("You are a creative and imaginative person.")
    

if __name__ == "__main__":
    main()
