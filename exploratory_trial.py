
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.steps = 0
        self.distance = 0.0
        self.calories = 0

    def walk(self, steps):
        self.steps += steps
        self.distance += steps * 0.000762
        self.calories += steps // 20

    def display_stats(self):
        print("Fitness Tracker for", self.name)
        print("Steps taken:", self.steps)
        print("Distance covered:", round(self.distance, 2), "km")
        print("Calories burned:", self.calories)

# Main program
name = input("Enter your name: ")
tracker = FitnessTracker(name)

while True:
    print("\nMenu:")
    print("1. Walk")
    print("2. Display stats")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        steps = int(input("Enter the number of steps walked: "))
        tracker.walk(steps)
    elif choice == "2":
        tracker.display_stats()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
