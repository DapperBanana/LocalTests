// Binary search function in C#
public class BinarySearch
{
    public static int Search(int[] sortedArray, int target)
    {
        int left = 0;
        int right = sortedArray.Length - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;

            if (sortedArray[mid] == target)
                return mid;
            else if (sortedArray[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        // Target not found
        return -1;
    }

    // Example usage
    public static void Main()
    {
        int[] sortedList = { 1, 3, 5, 7, 9, 11, 13 };
        int targetValue = 7;
        int index = Search(sortedList, targetValue);
        if (index != -1)
            Console.WriteLine($"Found {targetValue} at index {index}.");
        else
            Console.WriteLine($"{targetValue} not found in the list.");
    }
}