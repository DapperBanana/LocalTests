
from heapq import heappush, heappop, heapify

def frequency_count(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def build_tree(freq):
    heap = [[weight, [char, '']] for char, weight in freq.items()]
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

def huffman_encoding(text):
    if len(text) == 0:
        return '', None
    freq = frequency_count(text)
    tree = build_tree(freq)
    encoded_text = ''.join([char[1] for char in tree for _ in range(freq[char[0]])])
    return encoded_text, tree

def huffman_decoding(encoded_text, tree):
    if len(encoded_text) == 0:
        return ''
    decoded_text = ''
    current_node = tree
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node[0]
        else:
            current_node = current_node[1]
        if type(current_node[0]) == str:
            decoded_text += current_node[0]
            current_node = tree
    return decoded_text

def main():
    text = input("Enter the text to compress: ")
    encoded_text, tree = huffman_encoding(text)
    print("Encoded text:", encoded_text)
    
    decoded_text = huffman_decoding(encoded_text, tree)
    print("Decoded text:", decoded_text)

if __name__ == '__main__':
    main()
