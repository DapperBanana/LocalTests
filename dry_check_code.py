using System;

public class PalindromicSubstring
{
    public static string LongestPalindrome(string s)
    {
        if (string.IsNullOrEmpty(s))
            return "";

        int start = 0, maxLength = 1;

        for (int i = 0; i < s.Length; i++)
        {
            // Check for odd length palindrome
            ExpandAroundCenter(s, i, i, ref start, ref maxLength);
            // Check for even length palindrome
            ExpandAroundCenter(s, i, i + 1, ref start, ref maxLength);
        }

        return s.Substring(start, maxLength);
    }

    private static void ExpandAroundCenter(string s, int left, int right, ref int start, ref int maxLength)
    {
        while (left >= 0 && right < s.Length && s[left] == s[right])
        {
            if (right - left + 1 > maxLength)
            {
                start = left;
                maxLength = right - left + 1;
            }
            left--;
            right++;
        }
    }

    public static void Main()
    {
        string input = "babad";
        Console.WriteLine($"Longest palindromic substring of '{input}' is: '{LongestPalindrome(input)}'");
    }
}