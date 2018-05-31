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

with open(filepath, "r") as paragraphtxt:
    paragraph = paragraphtxt.read()
# print(paragraph)
    
    words = paragraph.split()
    # print(words)
    wordcount = len(words)
    # print(wordcount)



  



print(f"Paragraph Analysis")
print(f"------------------")
print(f"Approximate Word Count: {int(wordcount)}")
# print(f"Approximate Sentence Count:" )
# print(f"Average Letter Count:" )
# print(f"Average Sentence Length:" )