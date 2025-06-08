
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories_burned = 0
    
    def record_steps(self, steps):
        self.steps += steps
    
    def calculate_calories_burned(self):
        self.calories_burned = self.steps // 20
    
    def display_stats(self):
        print("Total Steps:", self.steps)
        print("Calories Burned:", self.calories_burned)


fitness_tracker = FitnessTracker()

while True:
    print("\nFitness Tracking System")
    print("1. Record Steps")
    print("2. View Stats")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        steps = int(input("Enter the number of steps: "))
        fitness_tracker.record_steps(steps)
        fitness_tracker.calculate_calories_burned()
    elif choice == '2':
        fitness_tracker.display_stats()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
