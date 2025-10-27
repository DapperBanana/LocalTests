
class FitnessTracker:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.steps = 0
        self.calories = 0

    def track_steps(self, steps):
        self.steps += steps

    def track_calories(self, calories):
        self.calories += calories

    def get_summary(self):
        return f"Name: {self.name}\nAge: {self.age}\nWeight: {self.weight} kg\nHeight: {self.height} cm\nSteps: {self.steps}\nCalories: {self.calories}"

# Create a new fitness tracker
tracker = FitnessTracker("John Doe", 25, 70, 175)

print("Fitness Tracker")
print("-------------")

while True:
    print("\n1. Track steps")
    print("2. Track calories")
    print("3. View summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        steps = int(input("Enter the number of steps: "))
        tracker.track_steps(steps)
        print("Steps tracked successfully!")

    elif choice == "2":
        calories = int(input("Enter the number of calories burned: "))
        tracker.track_calories(calories)
        print("Calories tracked successfully!")

    elif choice == "3":
        print(tracker.get_summary())

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
