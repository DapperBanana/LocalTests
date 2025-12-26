using System;

public class BaseConverter
{
    public static string ConvertBase(string number, int fromBase, int toBase)
    {
        // Convert input number from the source base to an integer
        int decimalValue = Convert.ToInt32(number, fromBase);
        // Convert integer to target base
        return Convert.ToString(decimalValue, toBase);
    }
    
    public static void Main()
    {
        // Example usage:
        string number = "1011"; // Binary number
        int fromBase = 2;
        int toBase = 10; // Convert to decimal
        Console.WriteLine($"{number} from base {fromBase} to base {toBase} is {ConvertBase(number, fromBase, toBase)}");
        
        // Another example: hex to binary
        number = "1A";
        fromBase = 16;
        toBase = 2;
        Console.WriteLine($"{number} from base {fromBase} to base {toBase} is {ConvertBase(number, fromBase, toBase)}");
    }
}