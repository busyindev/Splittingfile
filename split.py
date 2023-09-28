import os

if __name__ == "__main__":

    input_file = '08DPS8UFULL.096000'  # Replace with your input file path
    output_directory = 'Outfile'  # Replace with your desired output directory path
    chunk_size = 2 * 1024 * 1024
    with open(input_file, 'rb') as f:
        index = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            output_file = os.path.join(output_directory, f'part_{index}.dat')
            with open(output_file, 'wb') as out:
                out.write(chunk)
            index += 1
    print("Done!")
