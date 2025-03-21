
from heapq import heappush, heappop, heapify
from collections import defaultdict

def build_huffman_tree(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    
    heap = [[freq, [char, ""]] for char, freq in freq_dict.items()]
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

def encode(text, huffman_codes):
    encoded_text = ""
    for char in text:
        encoded_text += huffman_codes[char]
    
    return encoded_text

def decode(encoded_text, huffman_codes):
    reversed_codes = {code: char for char, code in huffman_codes.items()}
    
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in reversed_codes:
            decoded_text += reversed_codes[code]
            code = ""
    
    return decoded_text

# Example usage
text = "hello world"
huffman_tree = build_huffman_tree(text)
huffman_codes = {char: code for char, code in huffman_tree}

encoded_text = encode(text, huffman_codes)
decoded_text = decode(encoded_text, huffman_codes)

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
