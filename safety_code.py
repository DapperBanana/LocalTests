
import zlib

def compress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f_in:
            data = f_in.read()
            compressed_data = zlib.compress(data)
            with open(output_file, 'wb') as f_out:
                f_out.write(compressed_data)
        print(f"File {input_file} compressed and saved as {output_file}")
    except FileNotFoundError:
        print("File not found.")

def decompress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f_in:
            compressed_data = f_in.read()
            data = zlib.decompress(compressed_data)
            with open(output_file, 'wb') as f_out:
                f_out.write(data)
        print(f"File {input_file} decompressed and saved as {output_file}")
    except FileNotFoundError:
        print("File not found.")

# Example usage
input_file = 'example.txt'
compressed_file = 'example.txt.gz'
decompressed_file = 'example_decompressed.txt'

compress_file(input_file, compressed_file)

decompress_file(compressed_file, decompressed_file)
