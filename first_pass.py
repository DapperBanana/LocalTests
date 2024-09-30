
class FitnessTracker:
    def __init__(self, username):
        self.username = username
        self.steps = 0
        self.calories = 0
        self.workouts = []

    def add_steps(self, steps):
        self.steps += steps

    def add_calories(self, calories):
        self.calories += calories

    def add_workout(self, workout):
        self.workouts.append(workout)

    def display_stats(self):
        print(f"Username: {self.username}")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories}")
        print("Workouts:")
        for workout in self.workouts:
            print(f"- {workout}")


# Main program
tracker = FitnessTracker("John")

while True:
    print("1. Add steps")
    print("2. Add calories")
    print("3. Add workout")
    print("4. Display stats")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        steps = int(input("Enter number of steps: "))
        tracker.add_steps(steps)
    elif choice == 2:
        calories = int(input("Enter number of calories: "))
        tracker.add_calories(calories)
    elif choice == 3:
        workout = input("Enter workout: ")
        tracker.add_workout(workout)
    elif choice == 4:
        tracker.display_stats()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
