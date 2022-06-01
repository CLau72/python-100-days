import pandas

# Read alphabet CSV into a pandas DataFrame
alphabet_df = pandas.read_csv("./nato_phonetic_alphabet.csv")
# Create dictionary of letter:NATO translation pairs
nato_alphabet = {row.letter:row.code for index, row in alphabet_df.iterrows()}

# Take in a string and give the NATO phonetic sound for each letter
def nato_translate():
    input_str = input("Enter value to translate: ").upper()

    try:
        translation = [nato_alphabet[letter] for letter in input_str]
    except KeyError:
        print("Only input letters")
        nato_translate()
    else:
        print(translation)

# Prompt for input and print list of phonetic sounds

nato_translate()
