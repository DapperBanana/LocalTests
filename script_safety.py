letion(id='chatcmpl-95dBIAeLKNO9U7HGbMQnxJoMavyvF', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def personality_quiz():
    print("Welcome to the Personality Quiz!")
    print("Answer the following questions to determine your personality type.")

    # Questions
    questions = ["1. What is your favorite color? (a) Red (b) Blue (c) Green",
                 "2. What is your ideal way to spend a weekend? (a) Going to a party (b) Hiking in nature (c) Relaxing at home",
                 "3. How do you handle stress? (a) Working out (b) Meditating (c) Talking to a friend",
                 "4. What motivates you? (a) Success (b) Personal growth (c) Helping others"]

    # Answers
    answers = []

    # Ask questions and get user input
    for question in questions:
        print(question)
        answer = input("Enter your choice (a, b, or c): ")
        answers.append(answer)

    # Calculate personality type based on answers
    result = {"a": "Type A - Ambitious and competitive",
              "b": "Type B - Laid-back and introspective",
              "c": "Type C - Compassionate and empathetic"}

    # Count occurrence of each answer
    counts = {answer: answers.count(answer) for answer in answers}

    most_common_answer = max(counts, key=counts.get)
    personality_type = result[most_common_answer]

    print("\nYour personality type is: " + personality_type)

personality_quiz()', role='assistant', function_call=None, tool_calls=None))], created=1711129280, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=310, prompt_tokens=20, total_tokens=330)