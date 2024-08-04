
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0
        self.workouts = []

    def log_workout(self, workout_type, duration, distance):
        self.workouts.append({
            'type': workout_type,
            'duration': duration,
            'distance': distance
        })
        self.update_stats(duration, distance)

    def update_stats(self, duration, distance):
        self.steps += int(distance * 2000)  # Assume 1 km = 2000 steps
        self.distance += distance
        self.calories += int(duration * 100)  # Assume 1 minute = 100 calories

    def display_stats(self):
        print("Steps taken: ", self.steps)
        print("Distance covered: ", self.distance, "km")
        print("Calories burned: ", self.calories)
        print("\nWorkout History:")
        for workout in self.workouts:
            print("Type: ", workout['type'])
            print("Duration: ", workout['duration'], "minutes")
            print("Distance: ", workout['distance'], "km")
            print("---------------------")


# Main program
fitness_tracker = FitnessTracker()

while True:
    print("\nFitness Tracking System\n")
    print("1. Log Workout")
    print("2. Display Stats")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        workout_type = input("Enter workout type: ")
        duration = int(input("Enter duration (in minutes): "))
        distance = float(input("Enter distance (in km): "))
        fitness_tracker.log_workout(workout_type, duration, distance)
        print("Workout logged successfully!")

    elif choice == '2':
        fitness_tracker.display_stats()

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please try again.")
