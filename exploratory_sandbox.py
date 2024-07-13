
from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = dict(Counter(text))
    min_heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(min_heap)
    
    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        combined_freq = left.freq + right.freq
        new_node = Node(None, combined_freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(min_heap, new_node)
        
    return min_heap[0]

def encode(tree, mapping, current_code=""):
    if tree is not None:
        if tree.char is not None:
            mapping[tree.char] = current_code
        encode(tree.left, mapping, current_code + "0")
        encode(tree.right, mapping, current_code + "1")

def huffman_compress(text):
    root = build_huffman_tree(text)
    mapping = {}
    encode(root, mapping)
    
    encoded_text = "".join(mapping[char] for char in text)
    
    return encoded_text, mapping

def huffman_decompress(encoded_text, mapping):
    reverse_mapping = {v: k for k, v in mapping.items()}
    
    code = ""
    decoded_text = ""
    for bit in encoded_text:
        code += bit
        if code in reverse_mapping:
            decoded_text += reverse_mapping[code]
            code = ""
    
    return decoded_text

# Test the program
text = "hello world"
encoded_text, mapping = huffman_compress(text)
print("Encoded Text:", encoded_text)
decoded_text = huffman_decompress(encoded_text, mapping)
print("Decoded Text:", decoded_text)
