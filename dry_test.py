
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0
    
    def track_steps(self, num_steps):
        self.steps += num_steps
    
    def track_calories(self, num_calories):
        self.calories += num_calories
    
    def track_distance(self, distance):
        self.distance += distance
    
    def display_stats(self):
        print("Fitness Tracker Stats:")
        print("Steps:", self.steps)
        print("Calories:", self.calories)
        print("Distance:", self.distance)

def main():
    tracker = FitnessTracker()
    
    while True:
        print("Fitness Tracking System")
        print("1. Track Steps")
        print("2. Track Calories")
        print("3. Track Distance")
        print("4. Display Stats")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            num_steps = int(input("Enter the number of steps: "))
            tracker.track_steps(num_steps)
        elif choice == '2':
            num_calories = int(input("Enter the number of calories: "))
            tracker.track_calories(num_calories)
        elif choice == '3':
            distance = float(input("Enter the distance (in km): "))
            tracker.track_distance(distance)
        elif choice == '4':
            tracker.display_stats()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
