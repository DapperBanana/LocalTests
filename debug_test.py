
from heapq import heappush, heappop, heapify
from collections import defaultdict

def frequency(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    return freq

def huffman_encoding(text):
    freq = frequency(text)
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapify(heap)
    
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    huffman_code = {char: code for char, code in heap[0][1:]}
    
    encoded_text = ''.join(huffman_code[char] for char in text)
    
    return encoded_text, huffman_code

def huffman_decoding(encoded_text, huffman_code):
    reversed_code = {code: char for char, code in huffman_code.items()}
    decoded_text = ''
    code = ''
    
    for bit in encoded_text:
        code += bit
        if code in reversed_code:
            decoded_text += reversed_code[code]
            code = ''
    
    return decoded_text

text = "Hello, World!"
encoded_text, huffman_code = huffman_encoding(text)
decoded_text = huffman_decoding(encoded_text, huffman_code)

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
