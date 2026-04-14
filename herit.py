"""
inheritance_finder.py

Reads the origin.txt file  and finds all occurrences of words related to heritability.
Then, will output the line number and matched word to a new file.
"""

import re


def find_heritability_words(input_file, output_file):
    """
    Search for heritability-related words in a text file and write results to another file.

    Parameters:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output file.
    """
    
    pattern = re.compile(r'\b(inherit\w*|herit\w*)\b', re.IGNORECASE)

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            matches = pattern.findall(line)

            for match in matches:
                outfile.write(f"{line_number}\t{match}\n")


def main():
    """
    Main function to execute the script.
    """
    input_path = "origin.txt"
    output_path = "heritability_results.txt"

    find_heritability_words(input_path, output_path)
    print(f"Results written to {output_path}")


if __name__ == "__main__":
    main()
