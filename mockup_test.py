
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.steps = 0
        self.calories = 0

    def add_steps(self, steps):
        self.steps += steps

    def add_calories(self, calories):
        self.calories += calories

    def display_stats(self):
        print(f"{self.name}'s Fitness Stats:")
        print(f"Steps: {self.steps}")
        print(f"Calories Burned: {self.calories}")

# Main program
def main():
    name = input("Enter your name: ")
    user = FitnessTracker(name)

    while True:
        print("\nFitness Tracking Menu:")
        print("1. Add steps")
        print("2. Add calories burned")
        print("3. Display stats")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            steps = int(input("Enter the number of steps taken: "))
            user.add_steps(steps)
        elif choice == "2":
            calories = int(input("Enter the number of calories burned: "))
            user.add_calories(calories)
        elif choice == "3":
            user.display_stats()
        elif choice == "4":
            print("Exiting... Thank you for using the fitness tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
