
from collections import Counter
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_encoding_table(root, current_code, encoding_table):
    if root:
        if root.char is not None:
            encoding_table[root.char] = current_code
        build_encoding_table(root.left, current_code + '0', encoding_table)
        build_encoding_table(root.right, current_code + '1', encoding_table)

def huffman_encode(text):
    if not text:
        return '', None

    root = build_huffman_tree(text)
    encoding_table = {}
    build_encoding_table(root, '', encoding_table)

    encoded_text = ''.join(encoding_table[char] for char in text)
    
    return encoded_text, root

def huffman_decode(encoded_text, root):
    if not encoded_text:
        return ''

    current = root
    decoded_text = ''
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root

    return decoded_text

# Test the program
text = 'aabbbccccddddeeee'
encoded_text, tree = huffman_encode(text)
decoded_text = huffman_decode(encoded_text, tree)

print('Original text:', text)
print('Encoded text:', encoded_text)
print('Decoded text:', decoded_text)
