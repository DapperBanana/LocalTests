letion(id='chatcmpl-9e5oMHb8rbr0yldbjeqVDGQ6OkpVQ', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import heapq
from collections import defaultdict

# Function to generate huffman codes
def generate_huffman_codes(freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Function to compress text using huffman codes
def huffman_compress(text):
    freq = defaultdict(int)
    for symbol in text:
        freq[symbol] += 1
    
    huffman_codes = generate_huffman_codes(freq)
    
    compressed_text = ""
    for symbol in text:
        for code in huffman_codes:
            if symbol == code[0]:
                compressed_text += code[1]
    
    return compressed_text, huffman_codes

# Test the program
text = "hello world"
compressed_text, huffman_codes = huffman_compress(text)
print("Original text:", text)
print("Compressed text:", compressed_text)', role='assistant', function_call=None, tool_calls=None))], created=1719342486, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=306, prompt_tokens=20, total_tokens=326)