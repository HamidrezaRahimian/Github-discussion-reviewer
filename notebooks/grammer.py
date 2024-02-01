from spellchecker import SpellChecker

spell = SpellChecker()

misspelled = ["helo im goonna die berthday"]
for word in misspelled:
    print("original word: " + word)
    #print("corrected word: " + spell.correction(word))


    print("corrected word: " + spell.correction(misspelled))