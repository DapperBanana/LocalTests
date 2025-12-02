using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter a number to check if it is a vampire number:");
        string input = Console.ReadLine();
        if (long.TryParse(input, out long number))
        {
            bool isVampire = IsVampireNumber(number);
            Console.WriteLine($"{number} is {(isVampire ? "" : "not ")}a vampire number.");
        }
        else
        {
            Console.WriteLine("Invalid input.");
        }
    }

    static bool IsVampireNumber(long num)
    {
        string numStr = num.ToString();
        int len = numStr.Length;

        // Vampire numbers have even number of digits >= 2
        if (len % 2 != 0 || len < 2)
            return false;

        int halfLen = len / 2;
        var permutations = GetPermutations(numStr.ToCharArray(), 0, len);

        foreach (var perm in permutations)
        {
            string firstPart = new string(perm, 0, halfLen);
            string secondPart = new string(perm, halfLen, halfLen);

            // Skip if either part ends with '0'
            if (firstPart.EndsWith("0") && secondPart.EndsWith("0"))
                continue;

            long fang1 = long.Parse(firstPart);
            long fang2 = long.Parse(secondPart);

            // Fangs must be a proper factorization
            if (fang1 * fang2 == num)
            {
                // Check for trailing zeros
                if (fang1.ToString().EndsWith("0") && fang2.ToString().EndsWith("0"))
                    continue;

                // Check if fangs are a permutation of the original number's digits
                string combinedFangs = fang1.ToString() + fang2.ToString();
                char[] combinedFangsArr = combinedFangs.ToCharArray();
                Array.Sort(combinedFangsArr);

                char[] numDigits = numStr.ToCharArray();
                Array.Sort(numDigits);

                if (new string(combinedFangsArr) == new string(numDigits))
                {
                    return true;
                }
            }
        }

        return false;
    }

    static System.Collections.Generic.IEnumerable<char[]> GetPermutations(char[] array, int index, int length)
    {
        if (index == length - 1)
        {
            yield return (char[])array.Clone();
        }
        else
        {
            for (int i = index; i < length; i++)
            {
                Swap(ref array[index], ref array[i]);
                foreach (var perm in GetPermutations(array, index + 1, length))
                {
                    yield return perm;
                }
                Swap(ref array[index], ref array[i]);
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