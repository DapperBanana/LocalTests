using System;
using System.Net;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a string to validate as IPv6 address:");
        string input = Console.ReadLine();

        if (IsValidIPv6(input))
        {
            Console.WriteLine("The string is a valid IPv6 address.");
        }
        else
        {
            Console.WriteLine("The string is NOT a valid IPv6 address.");
        }
    }

    static bool IsValidIPv6(string address)
    {
        IPAddress ip;
        return IPAddress.TryParse(address, out ip) && ip.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6;
    }
}