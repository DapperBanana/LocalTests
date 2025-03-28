
def compress(input_text):
    compressed_text = ""
    count = 1
    for i in range(1, len(input_text)):
        if input_text[i] == input_text[i-1]:
            count += 1
        else:
            compressed_text += input_text[i-1] + str(count)
            count = 1
    compressed_text += input_text[-1] + str(count)
    
    return compressed_text

def decompress(compressed_text):
    decompressed_text = ""
    i = 0
    while i < len(compressed_text):
        character = compressed_text[i]
        count = int(compressed_text[i+1])
        decompressed_text += character * count
        i += 2
    return decompressed_text

input_text = "AAABBBCCCDDDEEEE"
compressed_text = compress(input_text)
print("Compressed text:", compressed_text)

decompressed_text = decompress(compressed_text)
print("Decompressed text:", decompressed_text)
