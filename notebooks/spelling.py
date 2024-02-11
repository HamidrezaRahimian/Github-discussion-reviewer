from spellchecker import SpellChecker


def correct_spelling(text):
    spell = SpellChecker()

    # Split the text into words hohahahaaa
    words = text.split()

    # Identify misspelled words ()unkown word in text will be considered as misspelled
    misspelled = spell.unknown(words)

    # lets Correct the misspelled words baby!________________________________________________
    #make a list to save the corrected word inside
    corrected_text = []
    print (1)
    for word in words:
        if word in misspelled: #misspelled = spell.unknown(words)
            print (2)
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
   # miss spelled correction is done_________________________________________________________
            
    # Join the corrected words back into a sentence
   

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
corrected_text = correct_spelling(text)
print(corrected_text)