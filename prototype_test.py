using System;

public class PalindromeFinder
{
    public static string LongestPalindrome(string s)
    {
        if (string.IsNullOrEmpty(s))
            return "";

        int start = 0, maxLength = 1;

        for (int i = 0; i < s.Length; i++)
        {
            // Check for odd length palindromes
            int len1 = ExpandAroundCenter(s, i, i);
            // Check for even length palindromes
            int len2 = ExpandAroundCenter(s, i, i + 1);

            int longerLen = Math.Max(len1, len2);
            if (longerLen > maxLength)
            {
                maxLength = longerLen;
                start = i - (longerLen - 1) / 2;
            }
        }

        return s.Substring(start, maxLength);
    }

    private static int ExpandAroundCenter(string s, int left, int right)
    {
        while (left >= 0 && right < s.Length && s[left] == s[right])
        {
            left--;
            right++;
        }
        // When the while loop breaks, left and right are one step beyond the palindrome boundaries
        return right - left - 1;
    }

    // Example usage:
    public static void Main()
    {
        string input = "babad";
        Console.WriteLine("Longest palindromic substring: " + LongestPalindrome(input));
    }
}