
def count_words(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the contents of the file
            contents = file.read()
        
        # Split the contents into words
        words = contents.split()
        
        # Count the number of words
        word_count = len(words)
        
        # Print the result
        print(f'The file "{filename}" contains {word_count} words.')
    
    except FileNotFoundError:
        print(f'Error: File "{filename}" not found.')


# Usage example
count_words('sample.txt')
