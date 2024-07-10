
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
        self.distance = 0
        self.workouts = []

    def add_steps(self, steps):
        self.steps += steps

    def add_calories(self, calories):
        self.calories += calories

    def add_distance(self, distance):
        self.distance += distance

    def record_workout(self, workout):
        self.workouts.append(workout)

    def display_stats(self):
        print("Fitness Tracker Stats:")
        print("Total Steps:", self.steps)
        print("Total Calories Burned:", self.calories)
        print("Total Distance Covered:", self.distance)
        print("Workouts Recorded:", len(self.workouts))
        print("Recent Workouts:")
        for workout in self.workouts[-5:]:
            print(workout)


# Create a FitnessTracker object
tracker = FitnessTracker()

# Simulate some activities
tracker.add_steps(5000)
tracker.add_calories(200)
tracker.add_distance(2.5)
tracker.record_workout("30 mins of running")
tracker.record_workout("1 hour of weightlifting")

# Display stats
tracker.display_stats()
