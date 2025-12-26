using System;
using System.Collections.Generic;

namespace TextBasedSocialMedia
{
    class Program
    {
        static List<string> posts = new List<string>();
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the Text-based Social Media Platform!");

            bool exit = false;
            while (!exit)
            {
                Console.WriteLine("\nPlease choose an option:");
                Console.WriteLine("1. Create a Post");
                Console.WriteLine("2. View Posts");
                Console.WriteLine("3. Exit");
                Console.Write("Your choice: ");

                string choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        CreatePost();
                        break;
                    case "2":
                        ViewPosts();
                        break;
                    case "3":
                        exit = true;
                        Console.WriteLine("Thank you for using the platform. Goodbye!");
                        break;
                    default:
                        Console.WriteLine("Invalid choice. Please try again.");
                        break;
                }
            }
        }

        static void CreatePost()
        {
            Console.WriteLine("Enter your post content:");
            string content = Console.ReadLine();

            if (!string.IsNullOrWhiteSpace(content))
            {
                posts.Add(content);
                Console.WriteLine("Post added successfully!");
            }
            else
            {
                Console.WriteLine("Post cannot be empty.");
            }
        }

        static void ViewPosts()
        {
            if (posts.Count == 0)
            {
                Console.WriteLine("No posts to display.");
            }
            else
            {
                Console.WriteLine("\n--- All Posts ---");
                for (int i = 0; i < posts.Count; i++)
                {
                    Console.WriteLine($"{i + 1}. {posts[i]}");
                }
                Console.WriteLine("-----------------\n");
            }
        }
    }
}