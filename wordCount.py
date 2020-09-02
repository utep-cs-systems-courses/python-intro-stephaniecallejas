#! /usr/bin/env python3

# keeps track of the total the number of times each word occurs in the text file
# excluding white space and punctuation
# is case-insensitive
# print out to the output file (overwriting if it exists) the list of words sorted in descending order
# with their respective totals separated by a space, one word per line


import string
import sys


if len(sys.argv) != 3:
   # print("")

    print("Correct usage: wordCountTest.py <input text file> <output text file>")
    exit()

input_File = sys.argv[1]
output_File = sys.argv[2]

# Open the file in read mode
#text = open("declaration.txt", "r")
with open(input_File, 'r') as inputFile:

# Create an empty dictionary
    d = dict()

# Loop through each line of the file
    for line in inputFile:
    # Remove the leading spaces and newline character
        line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
        line = line.lower()

    # Remove the punctuation marks from the line
        line = line.translate(line.maketrans(" ", " ", string.punctuation))

    # Split the line into words
        words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        if word is "":
            break
            # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
sorted(d.keys())
text = open(output_File, "w+")
#with open(output_File, "w") as outputFile:
for key in sorted(d.keys()):
    text.write(key + " " + str(d[key]) + "\n")
        #print(key, ":", d[key])
text.close()

#outputFile.write(word + " " + str(d[word]) + "\n")