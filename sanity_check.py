
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories_burned = 0
        self.distance = 0
        self.active_minutes = 0
    
    def record_activity(self, steps, calories, distance, active_minutes):
        self.steps += steps
        self.calories_burned += calories
        self.distance += distance
        self.active_minutes += active_minutes
    
    def display_stats(self):
        print("Fitness Tracker Stats:")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories_burned}")
        print(f"Total Distance: {self.distance} miles")
        print(f"Total Active Minutes: {self.active_minutes} minutes")


def main():
    tracker = FitnessTracker()

    while True:
        print("\nOptions:")
        print("1. Record Activity")
        print("2. Display Stats")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            steps = int(input("Enter number of steps: "))
            calories = int(input("Enter number of calories burned: "))
            distance = float(input("Enter distance (in miles): "))
            active_minutes = int(input("Enter number of active minutes: "))
            tracker.record_activity(steps, calories, distance, active_minutes)
        elif choice == '2':
            tracker.display_stats()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
