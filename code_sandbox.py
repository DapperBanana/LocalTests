
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.steps = 0
        self.calories = 0
        self.distance = 0

    def log_steps(self, num_steps):
        self.steps += num_steps

    def log_calories(self, num_calories):
        self.calories += num_calories

    def log_distance(self, num_km):
        self.distance += num_km

    def display_stats(self):
        print(f"Fitness Tracker for {self.name}:")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories}")
        print(f"Total Distance Covered: {self.distance} km")


# Main program
name = input("Enter your name: ")
tracker = FitnessTracker(name)

while True:
    print("\n1. Log Steps")
    print("2. Log Calories")
    print("3. Log Distance")
    print("4. Display Stats")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        steps = int(input("Enter number of steps: "))
        tracker.log_steps(steps)
    elif choice == "2":
        calories = int(input("Enter number of calories burned: "))
        tracker.log_calories(calories)
    elif choice == "3":
        distance = float(input("Enter distance in km: "))
        tracker.log_distance(distance)
    elif choice == "4":
        tracker.display_stats()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
