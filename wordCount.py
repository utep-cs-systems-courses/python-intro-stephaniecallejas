#! /usr/bin/env python3

# keeps track of the total the number of times each word occurs in the text file
# excluding white space and punctuation
# is case-insensitive
# print out to the output file (overwriting if it exists) the list of words sorted in descending order
# with their respective totals separated by a space, one word per line


import string
import sys
import re

input_File = sys.argv[1]
output_File = sys.argv[2]


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Correct usage: wordCount.py <input text file> <output file>")
        exit()

    # attempt to open input file and write in it
    with open(input_File, 'r') as inputFile:

        # Create an empty dictionary
        d = dict()

        for line in inputFile:
            # Remove the leading spaces and newline character
            line = line.strip()

            # Convert the characters in line to lowercase to avoid case mismatch
            line = line.lower()
            line = re.sub("-", " ", line)

            # Remove the punctuation marks from the line and hy
            line = re.sub(r"[,.;@#?!&$]+\ *", " ", line)
            line = line.translate(line.maketrans("", "", string.punctuation))

            # split line on whitespace and punctuation
            words = re.split('[ \t]', line)

            # print(words)
            for word in words:
                if word == "":
                    break
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1

    sorted(d.keys())
    text = open(output_File, "w+")
    with open(output_File, "w+")as outputFile:
        for key in sorted(d.keys()):
            text.write(key + " " + str(d[key]) + "\n")
    text.close()



