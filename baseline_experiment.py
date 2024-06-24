
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.calories_burned = 0
        self.steps_taken = 0
        self.workouts_completed = 0

    def record_activity(self, activity_type, amount):
        if activity_type == 'calories':
            self.calories_burned += amount
        elif activity_type == 'steps':
            self.steps_taken += amount
        elif activity_type == 'workouts':
            self.workouts_completed += amount
        else:
            print("Invalid activity type")

    def display_stats(self):
        print("Fitness Tracker for", self.name)
        print("Calories burned:", self.calories_burned)
        print("Steps taken:", self.steps_taken)
        print("Workouts completed:", self.workouts_completed)


def main():
    user_name = input("Enter your name: ")
    user_tracker = FitnessTracker(user_name)

    while True:
        print("\n1. Record Calories Burned")
        print("2. Record Steps Taken")
        print("3. Record Workouts Completed")
        print("4. Display Stats")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calories = int(input("Enter the number of calories burned: "))
            user_tracker.record_activity('calories', calories)
        elif choice == '2':
            steps = int(input("Enter the number of steps taken: "))
            user_tracker.record_activity('steps', steps)
        elif choice == '3':
            workouts = int(input("Enter the number of workouts completed: "))
            user_tracker.record_activity('workouts', workouts)
        elif choice == '4':
            user_tracker.display_stats()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
