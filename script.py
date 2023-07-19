def remove_duplicates(input_file, output_file):
    lines_seen = set()  # Set to store unique lines

    with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
        for line in file_in:
            if line not in lines_seen:
                file_out.write(line)
                lines_seen.add(line)

    print("Duplicate lines removed successfully.")

# Example usage
input_file = 'final-article-url.txt'
output_file = 'output.txt'
remove_duplicates(input_file, output_file)
