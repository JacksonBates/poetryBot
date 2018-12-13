import json
import markovify
import sys
import random

def poem_content():
    # Get raw text as string.
    with open("./corpus.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text, state_size=2)

    content = ""
    sentences = int(sys.argv[1])
    line_endings = ["","","","","","","","","","","-",":","--",";",",",".",",",",",".",".","?","!"]
    poem_endings = [".",".",".","!"]

    for i in range(sentences):
        content += text_model.make_short_sentence(50, tries=100)[:-1]
        if i < sentences - 1:
          content += random.choice(line_endings)
        else:
          content += random.choice(poem_endings)
        content += "\n"

    return content

if __name__ == '__main__':
    print(poem_content())