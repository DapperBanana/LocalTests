
from heapq import heappush, heappop, heapify
from collections import defaultdict

def build_huffman_tree(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
        
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapify(heap)
    
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
    return sorted(heappop(heap)[1:], key=lambda x: (len(x[-1]), x))

def huffman_encode(text):
    huffman_tree = build_huffman_tree(text)
    encoding = {char: code for char, code in huffman_tree}
    encoded_text = ''.join(encoding[char] for char in text)
    
    return encoded_text, encoding

def huffman_decode(encoded_text, encoding):
    decoding = {code: char for char, code in encoding.items()}
    current_code = ''
    decoded_text = ''
    
    for bit in encoded_text:
        current_code += bit
        if current_code in decoding:
            decoded_text += decoding[current_code]
            current_code = ''
    
    return decoded_text

text = "hello world"
encoded_text, encoding = huffman_encode(text)
print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", huffman_decode(encoded_text, encoding))
