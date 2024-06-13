
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.steps = 0
        self.calories = 0
        self.distance = 0

    def add_steps(self, steps):
        self.steps += steps

    def add_calories(self, calories):
        self.calories += calories

    def add_distance(self, distance):
        self.distance += distance

    def show_stats(self):
        print(f"Fitness Tracker for {self.name}")
        print("---------------------------")
        print(f"Steps: {self.steps}")
        print(f"Calories Burned: {self.calories}")
        print(f"Distance Covered: {self.distance} miles")

# Main program
name = input("Enter your name: ")
tracker = FitnessTracker(name)

while True:
    print("\nChoose an option:")
    print("1. Add steps")
    print("2. Add calories burned")
    print("3. Add distance covered")
    print("4. Show stats")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == '1':
        steps = int(input("Enter number of steps: "))
        tracker.add_steps(steps)
    elif choice == '2':
        calories = int(input("Enter number of calories burned: "))
        tracker.add_calories(calories)
    elif choice == '3':
        distance = float(input("Enter distance covered in miles: "))
        tracker.add_distance(distance)
    elif choice == '4':
        tracker.show_stats()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
