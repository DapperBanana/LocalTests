
import heapq
from collections import defaultdict

def create_frequency_dict(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

def huffman_encoding(text):
    frequency = create_frequency_dict(text)
    huffman_tree = build_huffman_tree(frequency)
    huffman_codes = huffman_tree[1:]
    encoded_text = ''.join([code for char in text for symbol, code in huffman_codes if symbol == char])
    return encoded_text, huffman_tree

def huffman_decoding(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node[1]
        else:
            current_node = current_node[2]
        if isinstance(current_node, str):
            decoded_text += current_node
            current_node = huffman_tree
    return decoded_text

text = "hello world"
encoded_text, huffman_tree = huffman_encoding(text)
print("Original text:", text)
print("Encoded text:", encoded_text)
decoded_text = huffman_decoding(encoded_text, huffman_tree)
print("Decoded text:", decoded_text)
