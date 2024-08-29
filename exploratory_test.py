
import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        data = f_in.read()
        compressed_data = zlib.compress(data)

    with open(output_file, 'wb') as f_out:
        f_out.write(compressed_data)

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        compressed_data = f_in.read()
        decompressed_data = zlib.decompress(compressed_data)

    with open(output_file, 'wb') as f_out:
        f_out.write(decompressed_data)

# Example usage
input_file = 'example.txt'
compressed_file = 'example_compressed.txt'
decompressed_file = 'example_decompressed.txt'

compress_file(input_file, compressed_file)
decompress_file(compressed_file, decompressed_file)
