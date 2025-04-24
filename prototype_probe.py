
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.hours_slept = 0

    def add_steps(self, steps):
        self.steps += steps

    def add_calories(self, calories):
        self.calories += calories

    def add_hours_slept(self, hours):
        self.hours_slept += hours

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print("Total Steps:", self.steps)
        print("Total Calories Burned:", self.calories)
        print("Total Hours Slept:", self.hours_slept)


def main():
    tracker = FitnessTracker()

    while True:
        print("\nFitness Tracking Menu:")
        print("1. Add Steps")
        print("2. Add Calories Burned")
        print("3. Add Hours Slept")
        print("4. Display Stats")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            steps = int(input("Enter the number of steps taken: "))
            tracker.add_steps(steps)
        elif choice == "2":
            calories = int(input("Enter the number of calories burned: "))
            tracker.add_calories(calories)
        elif choice == "3":
            hours = float(input("Enter the number of hours slept: "))
            tracker.add_hours_slept(hours)
        elif choice == "4":
            tracker.display_stats()
        elif choice == "5":
            print("Exiting Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
