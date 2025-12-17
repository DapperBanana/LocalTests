using System;

namespace SpaceExplorationGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Space Exploration!");
            Console.Write("Enter your spaceship's name: ");
            string shipName = Console.ReadLine();

            int fuel = 100;
            int progress = 0;
            const int goalDistance = 100;
            Random rand = new Random();

            Console.WriteLine($"Ready for launch, Captain of {shipName}!");
            Console.WriteLine($"Your goal is to travel {goalDistance} light-years.\n");

            while (progress < goalDistance && fuel > 0)
            {
                Console.WriteLine($"Current progress: {progress} light-years");
                Console.WriteLine($"Remaining fuel: {fuel}");
                Console.WriteLine("Choose an action:");
                Console.WriteLine("1. Thrust forward");
                Console.WriteLine("2. Rest");
                Console.WriteLine("3. Check status");
                Console.Write("Enter your choice: ");
                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        int fuelConsumption = rand.Next(10, 21);
                        int distanceTravelled = rand.Next(5, 16);

                        if (fuel >= fuelConsumption)
                        {
                            fuel -= fuelConsumption;
                            progress += distanceTravelled;
                            Console.WriteLine($"You thrust forward and traveled {distanceTravelled} light-years!");
                        }
                        else
                        {
                            Console.WriteLine("Not enough fuel to thrust forward!");
                        }
                        break;
                    case "2":
                        Console.WriteLine("You take a rest, conserving fuel.");
                        break;
                    case "3":
                        Console.WriteLine($"--- Status ---");
                        Console.WriteLine($"Ship Name: {shipName}");
                        Console.WriteLine($"Progress: {progress}/{goalDistance} light-years");
                        Console.WriteLine($"Fuel: {fuel}");
                        Console.WriteLine("--------------");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please select 1, 2, or 3.");
                        break;
                }

                // Random event: encounter an asteroid field
                if (rand.Next(0, 10) < 2)
                {
                    Console.WriteLine("Alert! You encountered an asteroid field!");
                    int damage = rand.Next(10, 25);
                    fuel -= damage;
                    Console.WriteLine($"Your ship loses {damage} fuel in the collision.");
                }

                Console.WriteLine();
            }

            if (progress >= goalDistance)
            {
                Console.WriteLine($"Congratulations, Captain! You have successfully completed your mission in {shipName}.");
            }
            else
            {
                Console.WriteLine("Game over. You've run out of fuel before reaching your destination.");
            }
        }
    }
}