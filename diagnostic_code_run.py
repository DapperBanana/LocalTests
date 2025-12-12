using System;

class Program
{
    static void Main()
    {
        // Initialize player and enemy stats
        int playerHealth = 100;
        int enemyHealth = 100;
        int playerDamage = 20;
        int enemyDamage = 15;
        Random rand = new Random();

        Console.WriteLine("Welcome to the Basic Text-Based RPG Battle!");

        while (playerHealth > 0 && enemyHealth > 0)
        {
            Console.WriteLine($"\nYour Health: {playerHealth} | Enemy Health: {enemyHealth}");
            Console.WriteLine("Choose your action: ");
            Console.WriteLine("1. Attack");
            Console.WriteLine("2. Defend");
            Console.Write("Enter choice (1 or 2): ");

            string input = Console.ReadLine();

            if (input == "1")
            {
                // Player attacks
                int damageDealt = rand.Next(playerDamage - 5, playerDamage + 6);
                enemyHealth -= damageDealt;
                Console.WriteLine($"You dealt {damageDealt} damage to the enemy!");

                if (enemyHealth <= 0)
                {
                    Console.WriteLine("You defeated the enemy! Victory!");
                    break;
                }
            }
            else if (input == "2")
            {
                // Player defends (reduces damage next turn)
                Console.WriteLine("You brace for the enemy's attack, reducing damage this turn.");
            }
            else
            {
                Console.WriteLine("Invalid choice, please select 1 or 2.");
                continue;
            }

            // Enemy attacks
            int enemyAttackDamage = rand.Next(enemyDamage - 3, enemyDamage + 4);
            if (input == "2")
            {
                enemyAttackDamage /= 2; // Damage reduction if defending
            }

            playerHealth -= enemyAttackDamage;
            Console.WriteLine($"The enemy attacked and dealt {enemyAttackDamage} damage!");

            if (playerHealth <= 0)
            {
                Console.WriteLine("You have been defeated! Game Over.");
                break;
            }
        }

        Console.WriteLine("\nGame Over. Thanks for playing!");
    }
}