using System;
using System.Collections.Generic;

class PlaylistManager
{
    static List<string> playlist = new List<string>();

    static void Main()
    {
        bool running = true;
        while (running)
        {
            Console.WriteLine("\n--- Music Playlist Manager ---");
            Console.WriteLine("1. Add Song");
            Console.WriteLine("2. Remove Song");
            Console.WriteLine("3. View Playlist");
            Console.WriteLine("4. Exit");
            Console.Write("Select an option (1-4): ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    AddSong();
                    break;
                case "2":
                    RemoveSong();
                    break;
                case "3":
                    ViewPlaylist();
                    break;
                case "4":
                    running = false;
                    Console.WriteLine("Exiting the Playlist Manager. Goodbye!");
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please select again.");
                    break;
            }
        }
    }

    static void AddSong()
    {
        Console.Write("Enter the song title to add: ");
        string song = Console.ReadLine();
        if (!string.IsNullOrWhiteSpace(song))
        {
            playlist.Add(song);
            Console.WriteLine($"'{song}' added to the playlist.");
        }
        else
        {
            Console.WriteLine("Empty input. No song added.");
        }
    }

    static void RemoveSong()
    {
        Console.Write("Enter the song title to remove: ");
        string song = Console.ReadLine();
        if (playlist.Remove(song))
        {
            Console.WriteLine($"'{song}' removed from the playlist.");
        }
        else
        {
            Console.WriteLine($"'{song}' not found in the playlist.");
        }
    }

    static void ViewPlaylist()
    {
        Console.WriteLine("\n--- Current Playlist ---");
        if (playlist.Count == 0)
        {
            Console.WriteLine("The playlist is empty.");
        }
        else
        {
            for (int i = 0; i < playlist.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {playlist[i]}");
            }
        }
    }
}