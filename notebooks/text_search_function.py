# In text_search_functions.py
def search_string_in_text(text, search_strings, label):
    for search_string in search_strings:
        if search_string.lower() in text.lower():
            print(f'Zeichenfolge "{search_string}" gefunden in {label}: {text}')
