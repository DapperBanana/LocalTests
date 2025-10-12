
def compress(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    compressed_data = ""
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

    print(f"File compressed successfully to {output_file}")

def decompress(input_file, output_file):
    with open(input_file, 'r') as f:
        compressed_data = f.read()

    decompressed_data = ""
    for i in range(0, len(compressed_data), 2):
        count = int(compressed_data[i])
        char = compressed_data[i+1]
        decompressed_data += char * count

    with open(output_file, 'w') as f:
        f.write(decompressed_data)

    print(f"File decompressed successfully to {output_file}")

# Example usage
input_file = "input.txt"
compressed_file = "compressed.txt"
decompressed_file = "decompressed.txt"

compress(input_file, compressed_file)
decompress(compressed_file, decompressed_file)
