
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0
        self.workouts = []

    def log_workout(self, workout_type, duration, calories):
        self.workouts.append((workout_type, duration, calories))
        self.calories += calories

    def log_steps(self, steps):
        self.steps += steps
        self.distance += steps * 0.00075

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print(f"Total steps: {self.steps}")
        print(f"Total calories burned: {self.calories} kcal")
        print(f"Total distance: {self.distance:.2f} miles\n")
        print("Workouts:")
        for i, workout in enumerate(self.workouts, start=1):
            print(f"Workout {i}: {workout[0]}, Duration: {workout[1]} mins, Calories burned: {workout[2]} kcal")

# Create an instance of FitnessTracker
tracker = FitnessTracker()

while True:
    print("1. Log Workout")
    print("2. Log Steps")
    print("3. Display Stats")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        workout_type = input("Enter workout type: ")
        duration = int(input("Enter duration in minutes: "))
        calories = int(input("Enter calories burned: "))
        tracker.log_workout(workout_type, duration, calories)
    elif choice == '2':
        steps = int(input("Enter number of steps: "))
        tracker.log_steps(steps)
    elif choice == '3':
        tracker.display_stats()
    elif choice == '4':
        print("Exiting the Fitness Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
