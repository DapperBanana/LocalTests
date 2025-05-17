
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
    freq = Counter(text)
    nodes = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(nodes)
    
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(nodes, merged)
        
    return nodes[0]

def build_codes(node, prefix="", codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = prefix
        build_codes(node.left, prefix + "0", codes)
        build_codes(node.right, prefix + "1", codes)
    
    return codes

def compress(text, codes):
    compressed_text = "".join(codes[char] for char in text)
    return compressed_text

def decompress(compressed_text, node):
    decompressed_text = ""
    current_node = node
    
    for bit in compressed_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decompressed_text += current_node.char
            current_node = node
    
    return decompressed_text

text = "hello world"
huffman_tree = build_huffman_tree(text)
codes = build_codes(huffman_tree)
compressed_text = compress(text, codes)
decompressed_text = decompress(compressed_text, huffman_tree)

print("Original text:", text)
print("Compressed text:", compressed_text)
print("Decompressed text:", decompressed_text)
