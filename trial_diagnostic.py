
import random

def generate_word_list():
    words = ["PYTHON", "PROGRAM", "CROSSWORD", "PUZZLE", "RANDOM", "GENERATE"]
    return words

def generate_crossword(words):
    crossword = [[' ' for _ in range(10)] for _ in range(10)]
    
    for word in words:
        direction = random.choice(["across", "down"])
        if direction == "across":
            row = random.randint(0, 9)
            col = random.randint(0, 10 - len(word))
            for i in range(len(word)):
                crossword[row][col + i] = word[i]
        else:
            row = random.randint(0, 10 - len(word))
            col = random.randint(0, 9)
            for i in range(len(word)):
                crossword[row + i][col] = word[i]
    
    return crossword

def print_crossword(crossword):
    for row in crossword:
        print("".join(row))

def main():
    words = generate_word_list()
    crossword = generate_crossword(words)
    print_crossword(crossword)

if __name__ == "__main__":
    main()
