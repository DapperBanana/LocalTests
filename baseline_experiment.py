
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.steps = 0
        self.calories = 0

    def record_steps(self, num_steps):
        self.steps += num_steps

    def record_calories(self, num_calories):
        self.calories += num_calories

    def display_stats(self):
        print(f"Fitness Stats for {self.name}:")
        print(f"Steps: {self.steps}")
        print(f"Calories: {self.calories}")

# Main program loop
tracker_name = input("Enter your name: ")
tracker = FitnessTracker(tracker_name)

while True:
    print("\nChoose an option:")
    print("1. Record steps")
    print("2. Record calories")
    print("3. Display stats")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num_steps = int(input("Enter number of steps: "))
        tracker.record_steps(num_steps)
    elif choice == "2":
        num_calories = int(input("Enter number of calories burned: "))
        tracker.record_calories(num_calories)
    elif choice == "3":
        tracker.display_stats()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
