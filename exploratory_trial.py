using System;

class SpaceExplorationGame
{
    static void Main()
    {
        Console.WriteLine("Welcome to the Space Exploration Game!");

        int spaceshipHealth = 100;
        int fuel = 100;
        int distanceTravelled = 0;
        bool gameRunning = true;

        while (gameRunning)
        {
            Console.WriteLine("\nCurrent Status:");
            Console.WriteLine($"Health: {spaceshipHealth}");
            Console.WriteLine($"Fuel: {fuel}");
            Console.WriteLine($"Distance Travelled: {distanceTravelled} light-years");
            Console.WriteLine("\nChoose an action:");
            Console.WriteLine("1. Travel");
            Console.WriteLine("2. Rest");
            Console.WriteLine("3. Check Status");
            Console.WriteLine("4. Quit");

            Console.Write("Enter your choice: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    if (fuel < 10)
                    {
                        Console.WriteLine("Not enough fuel to travel. Rest or find fuel.");
                    }
                    else
                    {
                        int travelDistance = new Random().Next(1, 6);
                        fuel -= 10;
                        distanceTravelled += travelDistance;
                        spaceshipHealth -= travelDistance; // traveling takes a toll
                        Console.WriteLine($"You traveled {travelDistance} light-years.");
                        if (spaceshipHealth <= 0)
                        {
                            Console.WriteLine("Your spaceship has been destroyed during the travel!");
                            gameRunning = false;
                        }
                    }
                    break;
                case "2":
                    Console.WriteLine("Restoring some health...");
                    int healAmount = new Random().Next(5, 21);
                    spaceshipHealth += healAmount;
                    if (spaceshipHealth > 100)
                        spaceshipHealth = 100;
                    Console.WriteLine($"Restored {healAmount} health points.");
                    break;
                case "3":
                    Console.WriteLine($"Status: Health={spaceshipHealth}, Fuel={fuel}, Distance={distanceTravelled} light-years");
                    break;
                case "4":
                    Console.WriteLine("Quitting the game. Safe travels!");
                    gameRunning = false;
                    break;
                default:
                    Console.WriteLine("Invalid choice. Try again.");
                    break;
            }

            // Random event: encounter an alien or find fuel
            if (gameRunning)
            {
                int eventChance = new Random().Next(1, 101);
                if (eventChance <= 20)
                {
                    Console.WriteLine("Encountered hostile aliens!");
                    int damage = new Random().Next(10, 31);
                    spaceshipHealth -= damage;
                    Console.WriteLine($"Aliens attacked! Your spaceship lost {damage} health points.");
                    if (spaceshipHealth <= 0)
                    {
                        Console.WriteLine("Your spaceship has been destroyed by aliens!");
                        gameRunning = false;
                    }
                }
                else if (eventChance <= 35)
                {
                    int foundFuel = new Random().Next(10, 31);
                    fuel += foundFuel;
                    Console.WriteLine($"You found a fuel depot! Gained {foundFuel} fuel.");
                }
            }
        }

        Console.WriteLine("Game Over. Thanks for playing!");
    }
}