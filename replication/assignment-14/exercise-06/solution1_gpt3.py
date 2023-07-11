import re

def findVowelStartWords(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
    
    pattern = r'\b[AEIOU][a-zA-Z]+\b'
    matches = re.findall(pattern, text)
    
    with open(output_file, 'w') as file:
        file.write('\n'.join(matches))


findVowelStartWords("Kornberg.txt", "Kornberg_Output_GPT3.txt")
findVowelStartWords("Gurdon.txt", "Gurdon_Output_GPT3.txt")
findVowelStartWords("Mendel.txt", "Mendel_Output_GPT3.txt")

