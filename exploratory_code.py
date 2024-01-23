
import heapq
import os
from collections import defaultdict


def compress(file_path):
    # Step 1: Read the file and determine the frequency of each character
    character_frequency = defaultdict(int)
    with open(file_path, 'r', encoding='utf8') as file:
        data = file.read()
        for char in data:
            character_frequency[char] += 1

    # Step 2: Build the Huffman tree
    heap = [[weight, [char, ""]] for char, weight in character_frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)
        for pair in low1[1:]:
            pair[1] = '0' + pair[1]
        for pair in low2[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low1[0] + low2[0]] + low1[1:] + low2[1:])

    huffman_tree = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    # Step 3: Generate compressed data
    compressed_data = ""
    for char in data:
        for code in huffman_tree:
            if char == code[0]:
                compressed_data += code[1]

    # Step 4: Pad the compressed data and generate the header
    padding_length = 8 - (len(compressed_data) % 8)
    padding = "0" * padding_length
    padded_compressed_data = compressed_data + padding

    header = '{0:08b}'.format(padding_length)
    for char, code in huffman_tree:
        header += '{0:08b}'.format(ord(char)) + code

    # Step 5: Write the compressed data to disk
    compressed_file_path = os.path.splitext(file_path)[0] + ".huff"
    with open(compressed_file_path, 'wb') as file:
        file.write(bytes(int(padded_compressed_data[i:i + 8], 2) for i in range(0, len(padded_compressed_data), 8)))

    return compressed_file_path


def decompress(compressed_file_path):
    # Read the compressed file
    with open(compressed_file_path, 'rb') as file:
        header = file.read(10)
        padding_length = int(header[:8], 2)

        # Retrieve the header information
        huffman_tree = []
        i = 8
        while i < len(header):
            char = chr(int(header[i:i + 8], 2))
            code_length = int(header[i + 8:i + 16], 2)
            code = header[i + 16:i + 16 + code_length]
            huffman_tree.append((char, code))
            i += 16 + code_length

        # Build the Huffman tree
        huffman_tree = sorted(huffman_tree, key=lambda p: (len(p[-1]), p))
        huffman_tree = [[char, ""] + list(code) for char, code in huffman_tree]
        
        # Decompress the data
        decompressed_data = ""
        next_char_code = ""
        for byte in file.read():
            byte_code = bin(byte)[2:].rjust(8, '0')
            for bit in byte_code:
                next_char_code += bit
                for char, code in huffman_tree:
                    if next_char_code == code:
                        if char == '\x00':
                            return decompressed_data
                        decompressed_data += char
                        next_char_code = ""

    return decompressed_data
