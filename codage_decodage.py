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

def main():
    print("=== Programme ROT13 ===")
    print("Choisissez le mode :")
    print("1. Codage (message clair → ROT13)")
    print("2. Décodage (message ROT13 → clair)")

    choix = input("Entrez 1 ou 2 : ").strip()

    if choix not in ['1', '2']:
        print("Choix invalide. Le programme va s'arrêter.")
        return

    message = input("Entrez le message : ")
    resultat = rot13(message)

    if choix == '1':
        print("\nMessage codé en ROT13 :")
    else:
        print("\nMessage décodé depuis ROT13 :")
    
    print(resultat)

if __name__ == "__main__":
    main()
