
from heapq import heappush, heappop, heapify
from collections import defaultdict

def build_frequency_table(text):
    frequency_table = defaultdict(int)
    for char in text:
        frequency_table[char] += 1
    return frequency_table

def build_huffman_tree(frequency_table):
    heap = [[weight, [char, ""]] for char, weight in frequency_table.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def build_encoding_table(huffman_tree):
    encoding_table = dict()
    for char, code in huffman_tree:
        encoding_table[char] = code
    return encoding_table

def encode_text(text, encoding_table):
    encoded_text = ''
    for char in text:
        encoded_text += encoding_table.get(char, '')
    return encoded_text

def compress_text(text):
    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    encoding_table = build_encoding_table(huffman_tree)
    encoded_text = encode_text(text, encoding_table)
    return encoded_text, encoding_table

def decompress_text(encoded_text, encoding_table):
    decoding_table = {code: char for char, code in encoding_table.items()}
    code = ''
    decoded_text = ''
    for bit in encoded_text:
        code += bit
        if code in decoding_table:
            decoded_text += decoding_table[code]
            code = ''
    return decoded_text

text = "abracadabra"
encoded_text, encoding_table = compress_text(text)
print("Original text:", text)
print("Encoded text:", encoded_text)
decoded_text = decompress_text(encoded_text, encoding_table)
print("Decoded text:", decoded_text)
