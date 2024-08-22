
import zlib

def compress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()
            
            compressed_data = zlib.compress(data)
            
            with open(output_file, 'wb') as out:
                out.write(compressed_data)
                
        print("File compressed successfully!")
        
    except FileNotFoundError:
        print("File not found!")

def decompress_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            compressed_data = f.read()
            
            decompressed_data = zlib.decompress(compressed_data)
            
            with open(output_file, 'wb') as out:
                out.write(decompressed_data)
                
        print("File decompressed successfully!")
        
    except FileNotFoundError:
        print("File not found!")

# Example usage
input_file = 'example.txt'
compressed_file = 'example.txt.gz'
decompressed_file = 'example_decompressed.txt'

compress_file(input_file, compressed_file)
decompress_file(compressed_file, decompressed_file)
