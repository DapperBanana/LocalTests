
class PersonalityQuiz:
    def __init__(self):
        self.questions = [
            "1. What is your favorite color?\nA. Red\nB. Blue\nC. Green",
            "2. What is your favorite animal?\nA. Dog\nB. Cat\nC. Bird",
            "3. How do you like to spend your free time?\nA. Reading\nB. Watching TV\nC. Outdoor activities"
        ]
        self.responses = []

    def ask_question(self, question):
        print(question)
        answer = input("Enter your choice (A/B/C): ")
        self.responses.append(answer)

    def run_quiz(self):
        for question in self.questions:
            self.ask_question(question)

        score = self.calculate_score()
        result = self.generate_result(score)
        print(result)

    def calculate_score(self):
        score = 0
        for response in self.responses:
            if response == 'A':
                score += 1
            elif response == 'B':
                score += 2
            elif response == 'C':
                score += 3
        return score

    def generate_result(self, score):
        if score <= 4:
            return "You are introverted and calm."
        elif score <= 8:
            return "You are balanced and easy-going."
        else:
            return "You are outgoing and energetic."


quiz = PersonalityQuiz()
quiz.run_quiz()
