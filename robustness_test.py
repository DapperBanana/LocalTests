
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0

    def record_activity(self, steps, calories, distance):
        self.steps += steps
        self.calories += calories
        self.distance += distance

    def display_stats(self):
        print("Fitness Stats:")
        print("Steps:", self.steps)
        print("Calories burned:", self.calories)
        print("Distance covered:", self.distance, "km")


def main():
    tracker = FitnessTracker()

    while True:
        print("\n1. Record Activity")
        print("2. Display Stats")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            steps = int(input("Enter number of steps taken: "))
            calories = int(input("Enter number of calories burned: "))
            distance = float(input("Enter distance covered (in km): "))
            tracker.record_activity(steps, calories, distance)
            print("Activity recorded successfully!")

        elif choice == "2":
            tracker.display_stats()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
