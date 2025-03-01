
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0

    def add_steps(self, steps):
        self.steps += steps
        self.calories += steps // 20
        self.distance += steps // 2000

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print(f"Steps: {self.steps}")
        print(f"Calories burned: {self.calories}")
        print(f"Distance covered: {self.distance} km")


def main():
    tracker = FitnessTracker()

    while True:
        print("\n1. Add steps")
        print("2. Display stats")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            steps = int(input("Enter the number of steps: "))
            tracker.add_steps(steps)
            print("Steps added!")

        elif choice == '2':
            tracker.display_stats()

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main()

