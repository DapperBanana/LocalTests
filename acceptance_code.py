
def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    compressed_data = bytearray()
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_data.append(count)
            compressed_data.append(data[i-1])
            count = 1

    compressed_data.append(count)
    compressed_data.append(data[-1])

    with open(output_file, 'wb') as f:
        f.write(compressed_data)


def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        compressed_data = f.read()

    decompressed_data = bytearray()
    for i in range(0, len(compressed_data), 2):
        count = compressed_data[i]
        value = compressed_data[i + 1]
        for _ in range(count):
            decompressed_data.append(value)

    with open(output_file, 'wb') as f:
        f.write(decompressed_data)


input_file = 'input.txt'
compressed_file = 'compressed.txt'
decompressed_file = 'decompressed.txt'

compress_file(input_file, compressed_file)
decompress_file(compressed_file, decompressed_file)
