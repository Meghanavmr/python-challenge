# Import a text file filled with a paragraph of your choosing.

# Assess the passage for each of the following:

# Approximate word count

# Approximate sentence count

# Approximate letter count (per word)

# Average sentence length (in words)



import os
import re
import string

filepath = os.path.join("paragraph.txt")

paragraph=""

words = []
lines = []
letters =[]
# avgletter = 0


with open(filepath, "r") as paragraphtxt:
    paragraph = paragraphtxt.read()
# print(paragraph)
    
words = paragraph.split()
#     # # print(words)
wordcount = len(words)
#     # print(wordcount)

lines = re.split("(?<=[.!?]) +", paragraph)
linecount = len(lines)
avgsentlength = wordcount/ linecount
# print(round(avgsentlength,2))


for letter in paragraph:
    letters.append(letter)
    # letters = re.split('\n', paragraph)
    lettercount = len(letters)
    avgletter = lettercount/wordcount 
    # print(round(avgletter,2))
        

  
# word/ sentence = sentence len
# lettercount/ number of words


print(f"Paragraph Analysis")
print(f"------------------")
print(f"Approximate Word Count: {int(wordcount)}")
print(f"Approximate Sentence Count:{int(linecount)}" )
print(f"Average Letter Count:{int(round(avgletter, 2))}" )
print(f"Average Sentence Length:{int(round(avgsentlength, 2))}" )