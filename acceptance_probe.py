
import zlib

def compress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f_in:
            data = f_in.read()
            compressed_data = zlib.compress(data)
            
        with open(output_file, 'wb') as f_out:
            f_out.write(compressed_data)
        
        print(f'File {input_file} compressed successfully to {output_file}')
        
    except FileNotFoundError:
        print('File not found. Please provide a valid file path')

# Example usage
input_file = 'example.txt'
output_file = 'example_compressed.txt'
compress_file(input_file, output_file)
