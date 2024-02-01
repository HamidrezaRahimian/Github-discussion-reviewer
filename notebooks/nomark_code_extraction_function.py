import re

def filter_python_expressions(text):
    output_list = []
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
        
        # Suche nach dem nächsten Vorkommen von zwei aufeinanderfolgenden Linebreaks (leere Zeile)
        next_empty_line = text.find('\n\n', match.end())
        
        # Erstelle eine eindeutige ID für diesen Textabschnitt
        text_id = f"{start}-{end}"
        
        # Überprüfe, ob dieser Textabschnitt bereits ausgegeben wurde
        if text_id not in output_list:
            # Begrenze die Ausgabe bis zur nächsten leeren Zeile
            next_chars = text[match.end():next_empty_line] if next_empty_line != -1 else text[match.end():]
            
            # Erstelle einen formatierten String und füge ihn zur Liste hinzu
            formatted_entry = (
                f"Previous Characters: {text[start:match.start()]}\n"
                f"Match: {text[match.start():match.end()]}\n"
                f"Next Characters until Empty Line: {next_chars}\n"
            )
            output_list.append(formatted_entry)

    # Gib die Liste der gefundenen Informationen zurück
    return output_list