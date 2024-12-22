
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.workouts = []

    def record_steps(self, steps):
        self.steps += steps

    def record_calories(self, calories):
        self.calories += calories

    def record_workout(self, workout):
        self.workouts.append(workout)

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories}")
        print("Workouts:")
        for workout in self.workouts:
            print(workout)


def main():
    tracker = FitnessTracker()

    while True:
        print("\n1. Record Steps")
        print("2. Record Calories Burned")
        print("3. Record Workout")
        print("4. Display Stats")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            steps = int(input("Enter number of steps: "))
            tracker.record_steps(steps)
        elif choice == '2':
            calories = int(input("Enter amount of calories burned: "))
            tracker.record_calories(calories)
        elif choice == '3':
            workout = input("Enter workout type: ")
            tracker.record_workout(workout)
        elif choice == '4':
            tracker.display_stats()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
