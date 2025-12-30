using System;

class Program
{
    static void Main()
    {
        // Initialize player and enemy stats
        Player player = new Player("Hero", 100, 20);
        Enemy enemy = new Enemy("Goblin", 80, 15);

        Console.WriteLine("A wild Goblin appears!");

        // Main game loop
        while (player.IsAlive() && enemy.IsAlive())
        {
            Console.WriteLine("\nYour HP: {0}", player.HP);
            Console.WriteLine("Enemy HP: {0}", enemy.HP);
            Console.WriteLine("Choose an action:\n1. Attack\n2. Heal");
            Console.Write("Enter choice: ");
            string choice = Console.ReadLine();

            if (choice == "1")
            {
                // Player attacks
                int damageDealt = player.Attack();
                enemy.TakeDamage(damageDealt);
                Console.WriteLine("You dealt {0} damage to the {1}.", damageDealt, enemy.Name);
            }
            else if (choice == "2")
            {
                // Player heals
                int healAmount = player.Heal();
                Console.WriteLine("You healed {0} HP.", healAmount);
            }
            else
            {
                Console.WriteLine("Invalid choice, try again.");
                continue;
            }

            // Check if enemy is defeated
            if (!enemy.IsAlive())
            {
                Console.WriteLine("You defeated the {0}!", enemy.Name);
                break;
            }

            // Enemy's turn to attack
            int enemyDamage = enemy.Attack();
            player.TakeDamage(enemyDamage);
            Console.WriteLine("The {0} attacked you for {1} damage.", enemy.Name, enemyDamage);

            // Check if player is defeated
            if (!player.IsAlive())
            {
                Console.WriteLine("You have been defeated...");
            }
        }
    }
}

// Player class
class Player
{
    public string Name { get; }
    public int HP { get; private set; }
    private int MaxHP;
    private int AttackPower;

    public Player(string name, int hp, int attack)
    {
        Name = name;
        HP = hp;
        MaxHP = hp;
        AttackPower = attack;
    }

    public int Attack()
    {
        // Could add randomness or critical hits here
        return AttackPower;
    }

    public int Heal()
    {
        int healAmount = 20;
        HP = Math.Min(HP + healAmount, MaxHP);
        return healAmount;
    }

    public void TakeDamage(int damage)
    {
        HP -= damage;
        if (HP < 0) HP = 0;
    }

    public bool IsAlive()
    {
        return HP > 0;
    }
}

// Enemy class
class Enemy
{
    public string Name { get; }
    public int HP { get; private set; }
    private int MaxHP;
    private int AttackPower;

    public Enemy(string name, int hp, int attack)
    {
        Name = name;
        HP = hp;
        MaxHP = hp;
        AttackPower = attack;
    }

    public int Attack()
    {
        // Could add randomness here
        return AttackPower;
    }

    public void TakeDamage(int damage)
    {
        HP -= damage;
        if (HP < 0) HP = 0;
    }

    public bool IsAlive()
    {
        return HP > 0;
    }
}