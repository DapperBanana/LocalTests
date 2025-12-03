using System;
using System.Collections.Generic;

public class BlackjackGame
{
    static Random rand = new Random();

    public static void Main()
    {
        Console.WriteLine("Welcome to Basic Text Blackjack!");

        while (true)
        {
            List<int> deck = CreateDeck();
            ShuffleDeck(deck);

            List<int> playerHand = new List<int>();
            List<int> dealerHand = new List<int>();

            // Deal initial two cards to player and dealer
            playerHand.Add(DrawCard(deck));
            playerHand.Add(DrawCard(deck));
            dealerHand.Add(DrawCard(deck));
            dealerHand.Add(DrawCard(deck));

            Console.WriteLine($"Your Hand: {String.Join(", ", playerHand)} (Total: {CalculateTotal(playerHand)})");
            Console.WriteLine($"Dealer's Visible Card: {dealerHand[0]}");

            // Player's turn
            bool playerBust = false;
            while (true)
            {
                if (CalculateTotal(playerHand) == 21)
                {
                    Console.WriteLine("Blackjack! You got 21!");
                    break;
                }

                Console.Write("Hit or Stand? (h/s): ");
                string input = Console.ReadLine().ToLower();

                if (input == "h")
                {
                    playerHand.Add(DrawCard(deck));
                    Console.WriteLine($"Your Hand: {String.Join(", ", playerHand)} (Total: {CalculateTotal(playerHand)})");
                    if (CalculateTotal(playerHand) > 21)
                    {
                        Console.WriteLine("Bust! You exceeded 21.");
                        playerBust = true;
                        break;
                    }
                }
                else if (input == "s")
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid input. Please enter 'h' or 's'.");
                }
            }

            // Dealer's turn
            if (!playerBust)
            {
                Console.WriteLine($"Dealer's Hand: {String.Join(", ", dealerHand)} (Total: {CalculateTotal(dealerHand)})");
                while (CalculateTotal(dealerHand) < 17)
                {
                    dealerHand.Add(DrawCard(deck));
                    Console.WriteLine($"Dealer hits: {String.Join(", ", dealerHand)} (Total: {CalculateTotal(dealerHand)})");
                }

                if (CalculateTotal(dealerHand) > 21)
                {
                    Console.WriteLine("Dealer busts! You win!");
                }
                else
                {
                    int playerTotal = CalculateTotal(playerHand);
                    int dealerTotal = CalculateTotal(dealerHand);
                    if (playerTotal > dealerTotal)
                        Console.WriteLine("You win!");
                    else if (playerTotal < dealerTotal)
                        Console.WriteLine("Dealer wins!");
                    else
                        Console.WriteLine("It's a tie!");
                }
            }
            Console.WriteLine("Play again? (y/n): ");
            if (Console.ReadLine().ToLower() != "y")
                break;
        }

        Console.WriteLine("Thanks for playing!");
    }

    static List<int> CreateDeck()
    {
        // Creates a standard 52-card deck with values 2-10, J=10, Q=10, K=10, A=11
        List<int> deck = new List<int>();
        for (int i = 0; i < 4; i++) // four suits
        {
            for (int value = 2; value <= 10; value++)
            {
                deck.Add(value);
            }
            // Face cards values J, Q, K
            deck.AddRange(new int[] { 10, 10, 10 }); // J, Q, K
            // Ace
            deck.Add(11);
        }
        return deck;
    }

    static void ShuffleDeck(List<int> deck)
    {
        for (int i = 0; i < deck.Count; i++)
        {
            int j = rand.Next(i, deck.Count);
            int temp = deck[i];
            deck[i] = deck[j];
            deck[j] = temp;
        }
    }

    static int DrawCard(List<int> deck)
    {
        int card = deck[0];
        deck.RemoveAt(0);
        return card;
    }

    static int CalculateTotal(List<int> hand)
    {
        int total = 0;
        int aceCount = 0;
        foreach (int card in hand)
        {
            total += card;
            if (card == 11)
                aceCount++;
        }
        // Adjust for Aces if total > 21
        while (total > 21 && aceCount > 0)
        {
            total -= 10;
            aceCount--;
        }
        return total;
    }
}