
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories_burned = 0
        self.distance = 0

    def record_steps(self, steps):
        self.steps += steps
        self.calories_burned += steps // 20  
        self.distance += steps // 2000  # assuming 2000 steps = 1 km

    def show_stats(self):
        print("Fitness Tracker Stats:")
        print("Steps taken:", self.steps)
        print("Calories burned:", self.calories_burned)
        print("Distance covered (in km):", self.distance)


# Main program loop
tracker = FitnessTracker()

while True:
    print("\n1. Record steps")
    print("2. Show stats")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        steps = int(input("Enter number of steps taken: "))
        tracker.record_steps(steps)
        print("Steps recorded successfully!")

    elif choice == '2':
        tracker.show_stats()

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please try again.")
