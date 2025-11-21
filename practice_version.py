
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.steps = 0
        self.calories = 0

    def record_steps(self, steps):
        self.steps += steps

    def record_calories(self, calories):
        self.calories += calories

    def display_stats(self):
        print(f"Fitness Stats for {self.name}:")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories}")

# Create a fitness tracker for a user named "John"
john_fitness_tracker = FitnessTracker("John")

# Simulate recording steps and calories for a workout
john_fitness_tracker.record_steps(5000)
john_fitness_tracker.record_calories(300)

# Display the fitness stats for John
john_fitness_tracker.display_stats()
