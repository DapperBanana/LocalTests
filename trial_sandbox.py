
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0
        self.minutes_active = 0

    def add_steps(self, steps):
        self.steps += steps
        self.calories += steps * 0.05
        self.distance += steps * 0.0005

    def add_activity(self, minutes):
        self.minutes_active += minutes
        self.calories += minutes * 5

    def display_stats(self):
        print("Steps taken:", self.steps)
        print("Calories burned:", self.calories)
        print("Distance covered (in km):", self.distance)
        print("Minutes active:", self.minutes_active)

if __name__ == "__main__":
    tracker = FitnessTracker()

    while True:
        print("\nFitness Tracking System")
        print("1. Add steps")
        print("2. Add activity")
        print("3. Display stats")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            steps = int(input("Enter the number of steps taken: "))
            tracker.add_steps(steps)
        elif choice == "2":
            minutes = int(input("Enter the number of minutes spent in activity: "))
            tracker.add_activity(minutes)
        elif choice == "3":
            tracker.display_stats()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
