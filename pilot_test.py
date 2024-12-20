
def compress_file(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.read()
    
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
    
    with open(output_file, 'w') as f:
        f.write(compressed_data)

input_file = "example.txt"
output_file = "compressed_file.txt"

compress_file(input_file, output_file)
