
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.calories_burned = 0
        self.steps_taken = 0
        self.distance_covered = 0
        self.water_consumed = 0

    def add_calories(self, calories):
        self.calories_burned += calories

    def add_steps(self, steps):
        self.steps_taken += steps

    def add_distance(self, distance):
        self.distance_covered += distance

    def add_water(self, water):
        self.water_consumed += water

    def display_stats(self):
        print(f"{self.name}'s Fitness Stats:")
        print(f"Calories Burned: {self.calories_burned}")
        print(f"Steps Taken: {self.steps_taken}")
        print(f"Distance Covered: {self.distance_covered} km")
        print(f"Water Consumed: {self.water_consumed} ml")


def main():
    name = input("Enter your name: ")
    tracker = FitnessTracker(name)

    while True:
        print("\n1. Add Calories")
        print("2. Add Steps")
        print("3. Add Distance")
        print("4. Add Water Consumed")
        print("5. Display Stats")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calories = int(input("Enter the number of calories burned: "))
            tracker.add_calories(calories)
        elif choice == '2':
            steps = int(input("Enter the number of steps taken: "))
            tracker.add_steps(steps)
        elif choice == '3':
            distance = float(input("Enter the distance covered (in km): "))
            tracker.add_distance(distance)
        elif choice == '4':
            water = int(input("Enter the amount of water consumed (in ml): "))
            tracker.add_water(water)
        elif choice == '5':
            tracker.display_stats()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
