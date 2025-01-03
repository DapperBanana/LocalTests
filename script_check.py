
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.total_steps = 0
        self.total_calories = 0
        self.total_distance = 0

    def add_steps(self, steps):
        self.total_steps += steps
        self.total_calories += steps * 0.05
        self.total_distance += steps * 0.000762

    def get_stats(self):
        return f"{self.name}'s Stats - Total Steps: {self.total_steps}, Total Calories Burned: {self.total_calories}, Total Distance: {self.total_distance} km"


# Main program
def main():
    tracker_name = input("Enter your name: ")
    tracker = FitnessTracker(tracker_name)

    while True:
        action = input("\nChoose an action - (a)dd steps, (s)how stats, (q)uit: ")

        if action == 'a':
            steps = int(input("Enter the number of steps: "))
            tracker.add_steps(steps)
        elif action == 's':
            print(tracker.get_stats())
        elif action == 'q':
            print("Quitting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
