
from heapq import heappush, heappop, heapify
from collections import defaultdict

def huffman_coding(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1

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

    huffman_dict = dict(heappop(heap)[1:])
    compressed_text = ''.join([huffman_dict[char] for char in text])
    
    return compressed_text, huffman_dict

def huffman_decoding(compressed_text, huffman_dict):
    reversed_huffman_dict = {v: k for k, v in huffman_dict.items()}
    decoded_text = ''
    code = ''
    for bit in compressed_text:
        code += bit
        if code in reversed_huffman_dict:
            decoded_text += reversed_huffman_dict[code]
            code = ''
    
    return decoded_text

text = "the quick brown fox jumps over the lazy dog"
compressed_text, huffman_dict = huffman_coding(text)
decoded_text = huffman_decoding(compressed_text, huffman_dict)

print("Original text:", text)
print("Compressed text:", compressed_text)
print("Decoded text:", decoded_text)
