
from heapq import heappush, heappop, heapify
from collections import defaultdict

def build_huffman_tree(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapify(heap)
    
    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
            
        heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])
    
    return sorted(heappop(heap)[1:], key=lambda x: (len(x[-1]), x))

def compress(text, huffman_codes):
    compressed_text = ''
    for char in text:
        compressed_text += huffman_codes[char]
    return compressed_text

def decompress(compressed_text, huffman_codes):
    decompressed_text = ''
    code = ''
    for bit in compressed_text:
        code += bit
        for char, value in huffman_codes.items():
            if value == code:
                decompressed_text += char
                code = ''
                break
    return decompressed_text

def main():
    text = "hello world"
    
    huffman_tree = build_huffman_tree(text)
    huffman_codes = {char: code for char, code in huffman_tree}
    print("Huffman Codes:", huffman_codes)
    
    compressed_text = compress(text, huffman_codes)
    print("Compressed Text:", compressed_text)
    
    decompressed_text = decompress(compressed_text, huffman_codes)
    print("Decompressed Text:", decompressed_text)
    
    print("Original text matches decompressed text:", text == decompressed_text)

if __name__ == '__main__':
    main()
