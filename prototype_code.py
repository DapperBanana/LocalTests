
def compress_file(input_file, output_file):
    with open(input_file, 'r') as file_in:
        data = file_in.read()

    compressed_data = ""
    current_char = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed_data += current_char + str(count)
            current_char = data[i]
            count = 1

    compressed_data += current_char + str(count)

    with open(output_file, 'w') as file_out:
        file_out.write(compressed_data)

input_file = 'input.txt'
output_file = 'output.txt'

compress_file(input_file, output_file)
