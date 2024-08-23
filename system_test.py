
import zlib

def compress_file(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as f_in:
            data = f_in.read()
            compressed_data = zlib.compress(data)
        
        with open(output_filename, 'wb') as f_out:
            f_out.write(compressed_data)
        
        print(f'File {input_filename} compressed and saved to {output_filename}')
    
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')


def decompress_file(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as f_in:
            compressed_data = f_in.read()
        
            decompressed_data = zlib.decompress(compressed_data)
        
        with open(output_filename, 'wb') as f_out:
            f_out.write(decompressed_data)
        
        print(f'File {input_filename} decompressed and saved to {output_filename}')
    
    except FileNotFoundError:
        print('File not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

# Example usage
input_filename = 'example.txt'
compressed_filename = 'compressed_example.txt'
decompressed_filename = 'decompressed_example.txt'

compress_file(input_filename, compressed_filename)
decompress_file(compressed_filename, decompressed_filename)
