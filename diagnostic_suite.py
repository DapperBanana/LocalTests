
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0

    def add_steps(self, steps):
        self.steps += steps
        self.calories += steps // 20

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print(f"Steps: {self.steps}")
        print(f"Calories Burned: {self.calories}")


def main():
    tracker = FitnessTracker()

    while True:
        print("1. Add Steps")
        print("2. Display Stats")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            steps = int(input("Enter the number of steps: "))
            tracker.add_steps(steps)
        elif choice == '2':
            tracker.display_stats()
        elif choice == '3':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
