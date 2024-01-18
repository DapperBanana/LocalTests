
from heapq import heappop, heappush
from collections import Counter, namedtuple

# Represents a node in the Huffman tree
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

# Represents a leaf node in the Huffman tree
class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

# Compresses the input text using Huffman coding
def compress(text):
    # Count the frequency of each character in the text
    freq = Counter(text)

    # Build the heap from the frequency counts
    heap = []
    for char, count in freq.items():
        heap.append((count, len(heap), Leaf(char)))

    # Create a Huffman tree from the heap
    while len(heap) > 1:
        count1, _, left = heappop(heap)
        count2, _, right = heappop(heap)
        heappush(heap, (count1 + count2, len(heap), Node(left, right)))

    code = {}
    if heap:
        [(count, _, root)] = heap
        root.walk(code, "")
    
    # Compress the text using the Huffman code
    compressed_text = "".join(code[char] for char in text)
    
    return compressed_text, code

# Decompresses the compressed text using the Huffman code
def decompress(compressed_text, code):
    rev_code = {v: k for k, v in code.items()}
    decoded_text = ""
    current_code = ""
    
    for bit in compressed_text:
        current_code += bit
        if current_code in rev_code:
            char = rev_code[current_code]
            decoded_text += char
            current_code = ""
    
    return decoded_text

# Example usage
text = "hello world"
compressed_text, code = compress(text)
print(f"Compressed text: {compressed_text}")
print(f"Huffman code: {code}")

decoded_text = decompress(compressed_text, code)
print(f"Decoded text: {decoded_text}")
