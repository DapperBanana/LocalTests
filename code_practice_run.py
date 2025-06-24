
from heapq import heappush, heappop, heapify
from collections import defaultdict

def build_freq_table(text):
    freq_table = defaultdict(int)
    for char in text:
        freq_table[char] += 1
    return freq_table

def build_huffman_tree(freq_table):
    heap = [[weight, [char, ""]] for char, weight in freq_table.items()]
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
    encoding_table = {}
    for char, code in huffman_tree:
        encoding_table[char] = code
    return encoding_table

def compress_text(text, encoding_table):
    return ''.join(encoding_table[char] for char in text)

def decompress_text(compressed_text, huffman_tree):
    decompressed_text = ""
    code_map = {code: char for char, code in huffman_tree}
    code = ""
    for bit in compressed_text:
        code += bit
        if code in code_map:
            decompressed_text += code_map[code]
            code = ""
    return decompressed_text

if __name__ == "__main__":
    text = "abcdefg"
    freq_table = build_freq_table(text)
    huffman_tree = build_huffman_tree(freq_table)
    encoding_table = build_encoding_table(huffman_tree)

    compressed_text = compress_text(text, encoding_table)
    decompressed_text = decompress_text(compressed_text, huffman_tree)

    print("Original text:", text)
    print("Compressed text:", compressed_text)
    print("Decompressed text:", decompressed_text)
