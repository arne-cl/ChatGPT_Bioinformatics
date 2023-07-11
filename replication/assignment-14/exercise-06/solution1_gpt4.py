import re

def findVowelStartWords(input_file, output_file):
    # Open the input and output files.
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        # Read the input file line by line.
        for line in in_file:
            # Use a regular expression to find all multi-letter words that start with an uppercase vowel.
            words = re.findall(r'(?<=\s)[AEIOU][A-Za-z]*\b', line)
            for word in words:
                # Write each matching word to the output file on a separate line.
                out_file.write(word + '\n')


findVowelStartWords("Kornberg.txt", "Kornberg_Output_GPT4.txt")
findVowelStartWords("Gurdon.txt", "Gurdon_Output_GPT4.txt")
findVowelStartWords("Mendel.txt", "Mendel_Output_GPT4.txt")
