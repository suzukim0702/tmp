def process_text_file(input_file, output_file):
    try:
        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            for line in infile:
                # Ensure the line has enough characters
                if len(line) >= 32:
                    indicator = line[31]  # 32nd byte in 0-based indexing

                    if indicator == '1':
                        outfile.write(line[:259] + '\n')
                    elif indicator == '2':
                        outfile.write(line[:268] + '\n')
                    elif indicator in ('3', '4'):
                        outfile.write(line[:260] + '\n')
                    else:
                        raise ValueError(f"Unexpected value at 32nd byte: {indicator}")
                else:
                    raise ValueError("Line does not have at least 32 characters")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# process_text_file('input.txt', 'output.txt')
