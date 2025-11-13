
import heapq
from collections import defaultdict

def huffman_encoding(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    heap = [[freq, [char, ""]] for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    codes = dict(heap[0][1:])
    encoded_text = ''.join([codes[char] for char in text])

    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    inv_codes = {v: k for k, v in codes.items()}

    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in inv_codes:
            decoded_text += inv_codes[current_code]
            current_code = ""

    return decoded_text

# Example usage
text = "hello world"
encoded_text, codes = huffman_encoding(text)
print("Encoded text:", encoded_text)
decoded_text = huffman_decoding(encoded_text, codes)
print("Decoded text:", decoded_text)
