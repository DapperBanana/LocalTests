
def compress_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    compressed_data = ""
    current_char = data[0]
    count = 1

    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            compressed_data += current_char + str(count)
            current_char = char
            count = 1

    compressed_data += current_char + str(count)

    with open(output_file, 'w') as f:
        f.write(compressed_data)

    print(f"File compressed successfully and saved as {output_file}")


def decompress_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()

    decompressed_data = ""

    for i in range(0, len(data), 2):
        char = data[i]
        count = int(data[i+1])
        decompressed_data += char * count

    with open(output_file, 'w') as f:
        f.write(decompressed_data)

    print(f"File decompressed successfully and saved as {output_file}")


# Example usage
input_file = "input.txt"
compressed_file = "compressed.txt"
decompressed_file = "decompressed.txt"

# Compress file
compress_file(input_file, compressed_file)

# Decompress file
decompress_file(compressed_file, decompressed_file)
