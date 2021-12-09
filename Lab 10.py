# Programmers: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date: 12/2/21
# Lab Number: 10
# Program Inputs: A file containing morse code
# Program Outputs: The decoded file in english

# Loads file morsecode.txt into a dictionary
def load_morse_dictionary():
    dictionary = {}
    file = open("morsecode.txt", "r")
    for line in file:
        key, value = line.split()
        dictionary[key] = value
    return dictionary
# Decodes morse code through dictionary
def decode_file(filename, morse_dict):
    coded = ''
    morse_dict = dict(morse_dict)
    open(filename)
    for line in filename():
        coded += line + ''
    d_value = ''
    letter = ''
    for letter in coded:
        counter = 0
        if letter == '':
            letter += letter
        else:
            counter = counter + 1
            if counter == 2:
                d_value = d_value + ''
    return d_value
# Define main function to run program
def main():
    morse_dict = load_morse_dictionary()
    filename = input("Input a file to decode: ")
    result = decode_file(filename, morse_dict)
    print(result)

main()