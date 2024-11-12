
from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        return self.freq < other.freq

class HuffmanCoding:
    def __init__(self, text):
        self.text = text
        self.frequency = dict(Counter(text))

    def build_tree(self):
        heap = [Node(char, freq) for char, freq in self.frequency.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            left_node = heapq.heappop(heap)
            right_node = heapq.heappop(heap)
            merged_node = Node(None, left_node.freq + right_node.freq)
            merged_node.left_child = left_node
            merged_node.right_child = right_node
            heapq.heappush(heap, merged_node)

        return heap[0]

    def build_code_table(self):
        root = self.build_tree()
        code_table = {}
        
        def traverse(node, code):
            if node.char:
                code_table[node.char] = code
            else:
                traverse(node.left_child, code + '0')
                traverse(node.right_child, code + '1')

        traverse(root, '')
        return code_table

    def compress(self):
        code_table = self.build_code_table()
        compressed_text = ''.join(code_table[char] for char in self.text)
        return compressed_text

    def decompress(self, compressed_text):
        code_table = {code: char for char, code in self.build_code_table().items()}
        code = ''
        decompressed_text = ''
        
        for bit in compressed_text:
            code += bit
            if code in code_table:
                decompressed_text += code_table[code]
                code = ''
        
        return decompressed_text

# Test the program
text = "hello world"
huffman = HuffmanCoding(text)
compressed_text = huffman.compress()
decompressed_text = huffman.decompress(compressed_text)

print("Original text:", text)
print("Compressed text:", compressed_text)
print("Decompressed text:", decompressed_text)
