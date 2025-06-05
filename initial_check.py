
def compress(data):
    compressed_data = ''
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            compressed_data += str(count) + data[i-1]
            count = 1
    compressed_data += str(count) + data[-1]
    return compressed_data

def decompress(data):
    decompressed_data = ''
    i = 0
    while i < len(data):
        count = int(data[i])
        char = data[i+1]
        decompressed_data += char * count
        i += 2
    return decompressed_data

# Test the compression and decompression functions
data = 'AAAABBBCCDAA'
compressed_data = compress(data)
print('Compressed data:', compressed_data)
decompressed_data = decompress(compressed_data)
print('Decompressed data:', decompressed_data)
