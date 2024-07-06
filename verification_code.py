
import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    pq = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(pq)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(pq, merged)

    return pq[0]

def build_encoding_table(root):
    encoding_table = {}
    
    def _build_encoding_table(node, code):
        if node.char is not None:
            encoding_table[node.char] = code
            return
        _build_encoding_table(node.left, code + '0')
        _build_encoding_table(node.right, code + '1')
    
    _build_encoding_table(root, '')
    return encoding_table

def compress(text):
    root = build_huffman_tree(text)
    encoding_table = build_encoding_table(root)
    
    encoded_text = ''.join(encoding_table[char] for char in text)
    
    return encoded_text, root

def decompress(encoded_text, root):
    decoded_text = []
    current = root

    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        
        if current.char is not None:
            decoded_text.append(current.char)
            current = root

    return ''.join(decoded_text)

if __name__ == "__main__":
    text = "hello world"
    
    encoded_text, root = compress(text)
    print(f"Compressed text: {encoded_text}")
    
    decoded_text = decompress(encoded_text, root)
    print(f"Decompressed text: {decoded_text}")
