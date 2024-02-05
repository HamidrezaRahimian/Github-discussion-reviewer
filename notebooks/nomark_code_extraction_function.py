import re

def filter_python_expressions(text):
    output_list = []
    # Muster für Python-typische Ausdrücke
    pattern = r'\b(?:if|else|elif|for|while|def|class|import|from|try|except|finally)\b'
    
    # Finden aller Übereinstimmungen
    matches = re.finditer(pattern, text)
    
    # Durchlaufe die Übereinstimmungen
    section_ends = []

    for match in matches:
    # Suche nach dem vorherigen Absatz
        start = text.rfind('\n', 0, match.start()) + 1 if match.start() > 0 else 0
    
    # Suche nach dem nächsten Absatz
        end = text.find('\n\n', match.end()) if text.find('\n\n', match.end()) != -1 else len(text)
    
    # Suche nach dem nächsten Vorkommen von zwei aufeinanderfolgenden Linebreaks (leere Zeile)
        next_empty_line = text.find('\n\n', match.end())
    
    # Erstelle eine eindeutige ID für diesen Textabschnitt
        text_id = f"{start}-{end}"
    
    
        
        # Begrenze die Ausgabe bis zur nächsten leeren Zeile
        next_chars = text[match.end():next_empty_line] if next_empty_line != -1 else text[match.end():]
        if end not in section_ends:
            # Erstelle einen formatierten String und füge ihn zur Liste hinzu
                formatted_entry = (
                    f"Previous Characters: {text[start:match.start()]}\n"
                    f"Match: {text[match.start():match.end()]}\n"
                    f"Next Characters until Empty Line: {next_chars}\n"
                )
                output_list.append(formatted_entry)
                section_ends.append(end)   
                print (section_ends)    
    
    # Gib die Liste der gefundenen Informationen zurück
    return output_list



# Example text
sample_text = """
The purpos of this blog post is just to test out projekt capability of extracting code from posts.

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
            if i==2:
# Zeichne die Ränder des Quadrats
for i in range(seitenlänge):
    for j in range(seitenlänge):
        if i == 0 or i == seitenlänge - 1 or j == 0 or j == seitenlänge - 1:
            print(zeichen, end=' ')
        else:
            if i==1:
                print (" ", end=' ')
            if i==2:
            




            
```
123124131
testtesttesttesttesttest
test
test
test
test
```
"""

# Call the function with the example text
result = filter_python_expressions(sample_text)

# Print the result
for entry in result:
    print(entry)