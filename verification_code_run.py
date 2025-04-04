
class FitnessTracker:
    def __init__(self):
        self.calories_burned = 0
        self.steps_taken = 0
        self.distance_walked = 0
        self.workouts_completed = 0

    def record_workout(self, calories, steps, distance):
        self.calories_burned += calories
        self.steps_taken += steps
        self.distance_walked += distance
        self.workouts_completed += 1

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print("Calories Burned:", self.calories_burned)
        print("Steps Taken:", self.steps_taken)
        print("Distance Walked:", self.distance_walked)
        print("Workouts Completed:", self.workouts_completed)

# Create a FitnessTracker object
tracker = FitnessTracker()

while True:
    print("\nWelcome to the Fitness Tracker!")
    print("1. Record a workout")
    print("2. Display stats")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        calories = int(input("Enter calories burned: "))
        steps = int(input("Enter steps taken: "))
        distance = float(input("Enter distance walked (in miles): "))
        tracker.record_workout(calories, steps, distance)
        print("Workout recorded!")

    elif choice == '2':
        tracker.display_stats()

    elif choice == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
