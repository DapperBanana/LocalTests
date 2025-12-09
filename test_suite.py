using System;

namespace VirtualPet
{
    class Program
    {
        static void Main(string[] args)
        {
            VirtualPet pet = new VirtualPet("Buddy");
            bool playing = true;

            Console.WriteLine("Welcome to the Virtual Pet Simulator!");

            while (playing)
            {
                Console.WriteLine($"\nWhat would you like to do with {pet.Name}?");
                Console.WriteLine("1. Feed");
                Console.WriteLine("2. Play");
                Console.WriteLine("3. Rest");
                Console.WriteLine("4. Quit");
                Console.Write("Enter your choice (1-4): ");

                string input = Console.ReadLine();

                switch (input)
                {
                    case "1":
                        pet.Feed();
                        break;
                    case "2":
                        pet.Play();
                        break;
                    case "3":
                        pet.Rest();
                        break;
                    case "4":
                        playing = false;
                        Console.WriteLine("Thanks for playing!");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }

                pet.Tick(); // Update pet's state after each action
                Console.WriteLine(pet.GetStatus());
            }
        }
    }

    class VirtualPet
    {
        public string Name { get; private set; }
        private int Hunger;
        private int Happiness;
        private int Energy;

        public VirtualPet(string name)
        {
            Name = name;
            Hunger = 50;    // 0 (full) to 100 (starving)
            Happiness = 50; // 0 (sad) to 100 (happy)
            Energy = 50;    // 0 (exhausted) to 100 (energetic)
        }

        public void Feed()
        {
            Hunger -= 20;
            if (Hunger < 0) Hunger = 0;
            Console.WriteLine($"{Name} has been fed.");
        }

        public void Play()
        {
            if (Energy >= 20)
            {
                Happiness += 20;
                Energy -= 20;
                Console.WriteLine($"You played with {Name}. They seem happier!");
            }
            else
            {
                Console.WriteLine($"{Name} is too tired to play.");
            }
        }

        public void Rest()
        {
            Energy += 30;
            if (Energy > 100) Energy = 100;
            Hunger += 10; // Resting makes the pet a bit hungrier
            if (Hunger > 100) Hunger = 100;
            Console.WriteLine($"{Name} is resting.");
        }

        public void Tick()
        {
            // Increase hunger and decrease happiness over time
            Hunger += 5;
            if (Hunger > 100) Hunger = 100;

            Happiness -= 5;
            if (Happiness < 0) Happiness = 0;

            Energy += 2; // Resting increases energy slowly
            if (Energy > 100) Energy = 100;
        }

        public string GetStatus()
        {
            return $"Status of {Name}:\nHunger: {Hunger}\nHappiness: {Happiness}\nEnergy: {Energy}";
        }
    }
}