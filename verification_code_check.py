
def compress_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()

    compressed_data = ''
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_data += str(count) + data[i - 1]
            count = 1

    compressed_data += str(count) + data[-1]

    with open(output_file, 'w') as file:
        file.write(compressed_data)

    print('File compressed successfully.')

def decompress_file(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()

    decompressed_data = ''
    for i in range(0, len(data), 2):
        count = int(data[i])
        character = data[i + 1]
        decompressed_data += character * count

    with open(output_file, 'w') as file:
        file.write(decompressed_data)

    print('File decompressed successfully.')

# Example usage
input_file = 'input.txt'
compressed_output_file = 'compressed_output.txt'
decompressed_output_file = 'decompressed_output.txt'

compress_file(input_file, compressed_output_file)
decompress_file(compressed_output_file, decompressed_output_file)
