
def compress_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    compressed_data = ''
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            compressed_data += str(count) + data[i-1]
            count = 1
    compressed_data += str(count) + data[-1]

    with open(output_file, 'w') as f:
        f.write(compressed_data)

    print('File compressed successfully.')

def decompress_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    decompressed_data = ''
    for i in range(0, len(data), 2):
        count = int(data[i])
        decompressed_data += data[i+1] * count

    with open(output_file, 'w') as f:
        f.write(decompressed_data)

    print('File decompressed successfully.')

# Test the compression and decompression functions
input_file = 'input.txt'
output_file = 'compressed.txt'
compressed_file = 'decompressed.txt'

compress_file(input_file, output_file)
decompress_file(output_file, compressed_file)
