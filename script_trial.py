
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

    def __eq__(self, other):
        return self.freq == other.freq

def build_huffman_tree(text):
    freq_map = Counter(text)
    min_heap = []
    for char, freq in freq_map.items():
        heapq.heappush(min_heap, Node(char, freq))

    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        merge_node = Node(None, left.freq + right.freq)
        merge_node.left = left
        merge_node.right = right
        heapq.heappush(min_heap, merge_node)

    return min_heap[0]

def build_encoding_table(root, encoding, current_encoding=""):
    if root is None:
        return
    if root.char is not None:
        encoding[root.char] = current_encoding
    build_encoding_table(root.left, encoding, current_encoding + "0")
    build_encoding_table(root.right, encoding, current_encoding + "1")

def huffman_compress(text):
    root = build_huffman_tree(text)
    encoding = {}
    build_encoding_table(root, encoding)
    compressed_text = ""
    for char in text:
        compressed_text += encoding[char]
    return compressed_text, root

def huffman_decompress(compressed_text, root):
    decoded_text = ""
    current_node = root
    for bit in compressed_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root
    return decoded_text

if __name__ == "__main__":
    text = "hello world"
    compressed_text, root = huffman_compress(text)
    print(f"Original text: {text}")
    print(f"Compressed text: {compressed_text}")
    decompressed_text = huffman_decompress(compressed_text, root)
    print(f"Decompressed text: {decompressed_text}")
