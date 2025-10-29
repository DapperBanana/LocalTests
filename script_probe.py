
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.workouts = []

    def record_steps(self, num_steps):
        self.steps += num_steps

    def record_calories(self, num_calories):
        self.calories += num_calories

    def add_workout(self, workout):
        self.workouts.append(workout)

    def display_stats(self):
        print("Fitness Stats:")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories}")
        print("Workouts:")
        for workout in self.workouts:
            print(f"- {workout}")


def main():
    tracker = FitnessTracker()

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Record Steps")
        print("2. Record Calories")
        print("3. Add Workout")
        print("4. Display Stats")
        print("5. Quit")

        choice = input("Enter choice: ")

        if choice == '1':
            num_steps = int(input("Enter number of steps: "))
            tracker.record_steps(num_steps)
        elif choice == '2':
            num_calories = int(input("Enter number of calories: "))
            tracker.record_calories(num_calories)
        elif choice == '3':
            workout = input("Enter workout: ")
            tracker.add_workout(workout)
        elif choice == '4':
            tracker.display_stats()
        elif choice == '5':
            print("Exiting Fitness Tracker. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
