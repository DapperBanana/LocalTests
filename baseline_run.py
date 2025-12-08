using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number to check if it's a vampire number:");
        string input = Console.ReadLine();
        if (ulong.TryParse(input, out ulong number))
        {
            if (IsVampireNumber(number))
                Console.WriteLine($"{number} is a vampire number.");
            else
                Console.WriteLine($"{number} is not a vampire number.");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid positive integer.");
        }
    }

    static bool IsVampireNumber(ulong number)
    {
        string numStr = number.ToString();
        int len = numStr.Length;

        // Vampire numbers have even number of digits
        if (len % 2 != 0)
            return false;

        int halfLen = len / 2;

        // Generate all permutations of the number's digits
        var digits = numStr.ToCharArray();
        Array.Sort(digits);
        var permutations = GetPermutations(digits, 0);

        foreach (var perm in permutations)
        {
            // Skip permutations with leading zero in the fangs
            if (perm[0] == '0' || perm[halfLen] == '0')
                continue;

            string firstFangStr = new string(perm, 0, halfLen);
            string secondFangStr = new string(perm, halfLen, halfLen);

            if (ulong.TryParse(firstFangStr, out ulong fang1) &&
                ulong.TryParse(secondFangStr, out ulong fang2))
            {
                if (fang1 * fang2 == number)
                {
                    // Check if fangs are not both palindromic and are valid fangs
                    // (Additional criteria can be added here if needed)
                    return true;
                }
            }
        }
        return false;
    }

    // Helper method to generate permutations of a char array
    static System.Collections.Generic.IEnumerable<char[]> GetPermutations(char[] array, int start)
    {
        if (start == array.Length - 1)
        {
            yield return (char[])array.Clone();
        }
        else
        {
            for (int i = start; i < array.Length; i++)
            {
                Swap(ref array[start], ref array[i]);
                foreach (var perm in GetPermutations(array, start + 1))
                {
                    yield return perm;
                }
                Swap(ref array[start], ref array[i]);
            }
        }
    }

    static void Swap(ref char a, ref char b)
    {
        if (a == b) return;
        char temp = a;
        a = b;
        b = temp;
    }
}