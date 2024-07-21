
import zipfile

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as file_in:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as file_out:
            file_out.write(input_file)

def decompress_file(input_file, output_file):
    with zipfile.ZipFile(input_file, 'r') as file_in:
        file_in.extractall(output_file)

# Test the compression algorithm
input_filename = 'sample_file.txt'
output_filename = 'compressed_file.zip'

# Compress file
compress_file(input_filename, output_filename)

# Decompress file
output_folder = 'decompressed_files'
decompress_file(output_filename, output_folder)
