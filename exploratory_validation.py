
def compress_file(input_file, output_file):
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

input_file = "input.txt"
output_file = "output.txt"

compress_file(input_file, output_file)
