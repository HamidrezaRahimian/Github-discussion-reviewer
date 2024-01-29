import re


def filter_python_expressions(text):
    output_set = set()
    # Muster für Python-typische Ausdrücke
    pattern = r'\b(?:if|else|elif|for|while|def|class|import|from|try|except|finally)\b'
    
    # Finden aller Übereinstimmungen
    matches = re.finditer(pattern, text)
    
    # Durchlaufe die Übereinstimmungen
    for match in matches:
        # Suche nach dem vorherigen Absatz
        start = text.rfind('\n', 0, match.start()) + 1 if match.start() > 0 else 0
        
        # Suche nach dem nächsten Absatz
        end = text.find('\n', match.end()) if text.find('\n', match.end()) != -1 else len(text)
        
        # Erstelle eine eindeutige ID für diesen Textabschnitt
        text_id = f"{start}-{end}"
        
        # Überprüfe, ob dieser Textabschnitt bereits ausgegeben wurde
        if text_id not in output_set:
            print(f"Vorherige Zeichen bis zum Absatz: {text[start:match.start()]}")
            print(f"Übereinstimmung: {text[match.start():match.end()]}")
            print(f"Bis zum nächsten Absatz: {text[match.end():end]}")
            print("\n")
            
            # Füge die Text-ID zur Liste der ausgegebenen Texte hinzu
            output_set.add(text_id)
