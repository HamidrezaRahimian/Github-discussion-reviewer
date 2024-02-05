from spellchecker import SpellChecker


def correct_spelling(discussion_body):
    spell = SpellChecker()

    # Split the text into words hohahahaaa
    words = text.split()

    # Identify misspelled words ()unkown word in text will be considered as misspelled
    misspelled = spell.unknown(words)

    # lets Correct the misspelled words baby!________________________________________________
    #make a list to save the corrected word inside
    corrected_text = []

    for word in words:
        if word in misspelled: #misspelled = spell.unknown(words)
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
   # miss spelled correction is done_________________________________________________________
            
    # Join the corrected words back into a sentence
    corrected_text = ' '.join(corrected_text)

    return corrected_text


