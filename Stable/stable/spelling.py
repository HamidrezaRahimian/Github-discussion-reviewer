from spellchecker import SpellChecker


from autocorrect import Speller

def correct_spelling(text):
    # Initialize Speller object
    spell = Speller()

    # Correct the spelling in the text
    corrected_text = spell(text)

    return corrected_text


text = """The purpos of this blog post is just to test out projekt capability of extracting code from posts.

```
testtesttesttesttesttest
test
test
test
test
```

import requests
import re
from string_extraction_function import extract_text_between_strings
from text_search_function import search_string_in_text
from code_extraction_function import  extract_code_blocks
from print_codeblocks_function import print_code_blocks

# Zeichne die Ränder des Quadrats
for i in range(seitenlänge):
    for j in range(seitenlänge):
        if i == 0 or i == seitenlänge - 1 or j == 0 or j == seitenlänge - 1:
            print(zeichen, end=' ')
        else:
            if i==1:
                print (" ", end=' ')
            if i==2:"""
#corrected_text = correct_spelling(text)
#print(corrected_text)