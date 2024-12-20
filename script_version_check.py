
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

    print(f'File compressed successfully. Compressed data saved in {output_file}')

def decompress_file(input_file, output_file):
    with open(input_file, 'r') as f:
        compressed_data = f.read()

    decompressed_data = ''
    i = 0
    while i < len(compressed_data):
        count = int(compressed_data[i])
        decompressed_data += compressed_data[i+1] * count
        i += 2

    with open(output_file, 'w') as f:
        f.write(decompressed_data)

    print(f'File decompressed successfully. Decompressed data saved in {output_file}')

# Test the compression and decompression
input_file = 'test.txt'
output_file = 'compressed_test.txt'

compress_file(input_file, output_file)
print('')

input_file = 'compressed_test.txt'
output_file = 'decompressed_test.txt'

decompress_file(input_file, output_file)
