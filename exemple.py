def rot13(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char  # caractères non alphabétiques inchangés
    return result

# Exemple de valeur obfusquée à décoder
valeur_obfusquee = "PlorelFrp"

# on décode la valeur
valeur_decodee = rot13(valeur_obfusquee)

print("Valeur obfusquée:", valeur_obfusquee)
print("Valeur décodée:", valeur_decodee)
