
import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as file_in:
        data = file_in.read()
        compressed_data = zlib.compress(data)
    
    with open(output_file, 'wb') as file_out:
        file_out.write(compressed_data)
    
    print(f"{input_file} has been compressed and saved as {output_file}")

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as file_in:
        compressed_data = file_in.read()
        decompressed_data = zlib.decompress(compressed_data)
    
    with open(output_file, 'wb') as file_out:
        file_out.write(decompressed_data)
    
    print(f"{input_file} has been decompressed and saved as {output_file}")

input_file = "input.txt"
compressed_file = "compressed.dat"
decompressed_file = "decompressed.txt"

# Compress file
compress_file(input_file, compressed_file)

# Decompress file
decompress_file(compressed_file, decompressed_file)
