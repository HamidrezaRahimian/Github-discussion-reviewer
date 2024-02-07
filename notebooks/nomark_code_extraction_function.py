import re

def filter_python_expressions(text):
    max_hinweis_länge=12
    # Finde Zeichenketten, die auf nicht explizit formatierten Code hinweisen können
    codehinweise = re.finditer(r'```(\w+)?\s*([\s\S]*?)\s*```|(\b(?:def|class|for|while|if|else|elif|try|except|import|from|print|return|console.log)\b)([^\n]*)', text)
    
    # Extrahiere eindeutige Zeichenketten mit Zeilennummer und Format
    eindeutige_codehinweise = []
    aktuelles_format = None

    for match in codehinweise:
        formatierung, codeblock, codehinweis, zeile = match.group(1), match.group(2), match.group(3), match.group(4)
        
        # Wenn ein Codeblock gefunden wurde, setze das Format
        if formatierung:
            aktuelles_format = formatierung
        elif codehinweis:
            # Kürze oder verlängere den Codehinweis, um die maximale Länge zu erreichen
            if len(codehinweis) < max_hinweis_länge:
                codehinweis = codehinweis + '_' * (max_hinweis_länge - len(codehinweis))
            else:
                codehinweis = codehinweis[:max_hinweis_länge]
            
            # Füge den Codehinweis mit Zeile und Format zur Liste hinzu
            eindeutige_codehinweise.append({
                'Codehinweis': codehinweis,
                '>>>>Zeile<<<<': zeile.strip()
            })

    return eindeutige_codehinweise
