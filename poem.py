import json
import markovify
import sys
import random
import re

def poem_content():
    # Get raw text as string.
    corpus = sys.argv[1]
    with open("./works/" + corpus) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text, state_size=2)

    # Generate the poem
    content = ""
    sentences = int(sys.argv[2])
    line_endings = ["","","","","","","","","","","-",":","--",";",",",".",",",",",".",".","?","!"]
    poem_endings = [".",".",".","!"]

    for i in range(sentences):
        # re.sub is used to strip chapter:verse for biblical texts
        content += re.sub(r'^\d*:\d*\s','',text_model.make_short_sentence(50, tries=100)[:-1])
        if i < sentences - 1:
          content += random.choice(line_endings)
        else:
          content += random.choice(poem_endings)
        content += "\n"

    return content

if __name__ == '__main__':
    print(poem_content())
