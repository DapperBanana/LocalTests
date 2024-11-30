
import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = Counter(text)
    heap = [Node(char, freq) for char, freq in freq_dict.items()]

    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_encoding_dict(node, encoding, prefix=""):
    if node:
        if node.char:
            encoding[node.char] = prefix
        build_encoding_dict(node.left, encoding, prefix + "0")
        build_encoding_dict(node.right, encoding, prefix + "1")

def huffman_compress(text):
    root = build_huffman_tree(text)
    encoding = {}
    build_encoding_dict(root, encoding)

    compressed_text = "".join(encoding[char] for char in text)
    return compressed_text, encoding

def huffman_decompress(compressed_text, encoding):
    decoding = {code: char for char, code in encoding.items()}
    
    current_code = ""
    decompressed_text = ""
    for bit in compressed_text:
        current_code += bit
        if current_code in decoding:
            decompressed_text += decoding[current_code]
            current_code = ""
    
    return decompressed_text

if __name__ == "__main__":
    text = "Hello, World!"
    
    compressed_text, encoding = huffman_compress(text)
    print("Compressed text:", compressed_text)
    
    decompressed_text = huffman_decompress(compressed_text, encoding)
    print("Decompressed text:", decompressed_text)
