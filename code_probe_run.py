public class PalindromeChecker
{
    public static bool IsPalindrome(string input)
    {
        if (input == null)
            return false;

        int left = 0;
        int right = input.Length - 1;

        while (left < right)
        {
            if (input[left] != input[right])
                return false;
            left++;
            right--;
        }

        return true;
    }
}