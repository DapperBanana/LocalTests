
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories_burned = 0
        self.distance = 0.0

    def add_steps(self, num_steps):
        self.steps += num_steps
        self.calories_burned += num_steps * 0.05  # Assuming 1 step burns 0.05 calories
        self.distance += num_steps * 0.0005  # Assuming 1 step covers 0.0005 miles

    def display_stats(self):
        print("Fitness Stats:")
        print("Steps taken:", self.steps)
        print("Calories burned:", round(self.calories_burned, 2))
        print("Distance covered (miles):", round(self.distance, 2))


def main():
    tracker = FitnessTracker()

    while True:
        print("\n1. Add steps")
        print("2. View stats")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num_steps = int(input("Enter the number of steps taken: "))
            tracker.add_steps(num_steps)
        elif choice == '2':
            tracker.display_stats()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
