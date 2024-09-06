
def compress(input_string):
    compressed_string = ""
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed_string += str(count) + input_string[i - 1]
            count = 1
    compressed_string += str(count) + input_string[-1]
    return compressed_string

def decompress(compressed_string):
    decompressed_string = ""
    for i in range(0, len(compressed_string), 2):
        count = int(compressed_string[i])
        decompressed_string += compressed_string[i + 1] * count
    return decompressed_string

input_string = "AAABBBCCCDDD"
print("Input String:", input_string)

compressed_string = compress(input_string)
print("Compressed String:", compressed_string)

decompressed_string = decompress(compressed_string)
print("Decompressed String:", decompressed_string)
