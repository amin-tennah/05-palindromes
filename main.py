'''Code d'un palyndrome'''
#### Fonction secondaire


def ispalindrome(p):
    """
    gjr
    """
    p = p.lower()
    accents = "àâäéèêëîïôöùûüç-.:?!,';_"
    sans_accents = "aaaeeeeiioouuuc         "
    table = str.maketrans(accents, sans_accents)
    cleaned_string = p.translate(table).replace(" ", "")
    return cleaned_string == cleaned_string[::-1]

#### Fonction principale


def main():
    """
    le main
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
