using System;
using System.Collections.Generic;

class FitnessTracker
{
    class Activity
    {
        public string Name { get; set; }
        public double Duration { get; set; } // in minutes
        public double CaloriesBurned { get; set; }
    }

    static List<Activity> activities = new List<Activity>();

    static void Main()
    {
        Console.WriteLine("Welcome to the Basic Fitness Tracking System!");

        bool exit = false;
        while (!exit)
        {
            Console.WriteLine("\nPlease select an option:");
            Console.WriteLine("1. Add Activity");
            Console.WriteLine("2. View Activities");
            Console.WriteLine("3. Total Calories Burned");
            Console.WriteLine("4. Exit");
            Console.Write("Enter your choice (1-4): ");
            string choice = Console.ReadLine();

            switch(choice)
            {
                case "1":
                    AddActivity();
                    break;
                case "2":
                    ViewActivities();
                    break;
                case "3":
                    TotalCalories();
                    break;
                case "4":
                    exit = true;
                    Console.WriteLine("Exiting the Fitness Tracker. Stay active!");
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please select again.");
                    break;
            }
        }
    }

    static void AddActivity()
    {
        Console.Write("Enter activity name: ");
        string name = Console.ReadLine();

        double duration = 0;
        while (true)
        {
            Console.Write("Enter duration in minutes: ");
            if (double.TryParse(Console.ReadLine(), out duration) && duration > 0)
                break;
            Console.WriteLine("Please enter a valid positive number for duration.");
        }

        double caloriesBurned = 0;
        while (true)
        {
            Console.Write("Enter calories burned for this activity: ");
            if (double.TryParse(Console.ReadLine(), out caloriesBurned) && caloriesBurned >= 0)
                break;
            Console.WriteLine("Please enter a valid non-negative number for calories.");
        }

        activities.Add(new Activity { Name = name, Duration = duration, CaloriesBurned = caloriesBurned });
        Console.WriteLine("Activity added successfully!");
    }

    static void ViewActivities()
    {
        if (activities.Count == 0)
        {
            Console.WriteLine("No activities recorded yet.");
            return;
        }

        Console.WriteLine("\nRecorded Activities:");
        for (int i = 0; i < activities.Count; i++)
        {
            var activity = activities[i];
            Console.WriteLine($"{i + 1}. {activity.Name} - {activity.Duration} mins, {activity.CaloriesBurned} calories");
        }
    }

    static void TotalCalories()
    {
        double total = 0;
        foreach (var activity in activities)
        {
            total += activity.CaloriesBurned;
        }
        Console.WriteLine($"Total calories burned across all activities: {total}");
    }
}