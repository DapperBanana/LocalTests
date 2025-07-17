
import heapq
from collections import defaultdict

def huffman_encoding(data):
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1
        
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    huffman_dict = {char: code for char, code in heap[0][1:]}
    
    encoded_data = ''.join([huffman_dict[char] for char in data])
    
    return encoded_data, huffman_dict

def huffman_decoding(data, huffman_dict):
    reverse_dict = {code: char for char, code in huffman_dict.items()}
    
    decoded_data = ''
    code = ''
    for bit in data:
        code += bit
        if code in reverse_dict:
            decoded_data += reverse_dict[code]
            code = ''
    
    return decoded_data

if __name__ == "__main__":
    data = "hello world"
    encoded_data, huffman_dict = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, huffman_dict)
    
    print("Original data:", data)
    print("Encoded data:", encoded_data)
    print("Decoded data:", decoded_data)
