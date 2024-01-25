def extract_text_between_strings(text, start_string, end_string):
    """
    Extrahiert den Text zwischen zwei Zeichenfolgen.
    """
    start_index = text.find(start_string)
    end_index = text.find(end_string, start_index + len(start_string))
    
    if start_index != -1 and end_index != -1:
        extracted_text = text[start_index + len(start_string):end_index]
        return extracted_text.strip()
    else:
        return None
