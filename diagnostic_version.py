
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0

    def log_steps(self, steps):
        self.steps += steps

    def log_calories(self, calories):
        self.calories += calories

    def log_distance(self, distance):
        self.distance += distance

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print("Steps:", self.steps)
        print("Calories burned:", self.calories)
        print("Distance covered:", self.distance, "km")


def main():
    tracker = FitnessTracker()

    while True:
        print("\nSelect an option:")
        print("1. Log Steps")
        print("2. Log Calories")
        print("3. Log Distance")
        print("4. Display Stats")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            steps = int(input("Enter number of steps: "))
            tracker.log_steps(steps)
        elif choice == '2':
            calories = int(input("Enter number of calories burned: "))
            tracker.log_calories(calories)
        elif choice == '3':
            distance = float(input("Enter distance covered (km): "))
            tracker.log_distance(distance)
        elif choice == '4':
            tracker.display_stats()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
