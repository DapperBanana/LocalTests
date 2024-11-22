
import datetime

class FitnessTracker:
    def __init__(self):
        self.data = {}

    def add_activity(self, activity, duration):
        if activity in self.data:
            self.data[activity] += duration
        else:
            self.data[activity] = duration

        print(f"Added {duration} minutes of {activity}.")

    def view_activities(self):
        print("Your fitness activities:")
        for activity, duration in self.data.items():
            print(f"{activity}: {duration} minutes")

    def total_duration(self):
        total_dur = sum(self.data.values())
        print(f"Total duration: {total_dur} minutes")

# Create a FitnessTracker object
tracker = FitnessTracker()

# Add activities
tracker.add_activity("Running", 30)
tracker.add_activity("Yoga", 45)
tracker.add_activity("Weight lifting", 60)

# View activities and total duration
tracker.view_activities()
tracker.total_duration()
