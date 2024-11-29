"""import de sys"""
import sys


#### Fonctions secondaires
sys.setrecursionlimit(10000)

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    current_letter =s[0]
    compteur = 1
    res = []
    for letter in s[1:]:
        if letter == current_letter:
            compteur += 1
        else:
            res.append((current_letter, compteur))
            current_letter = letter
            compteur = 1
    res.append((current_letter, compteur))
    return res


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:  # Si la chaîne est vide, retourner la liste vide
        return []
    def encode_recursive(s, index, letter, ctr, res):
        if index == len(s):
            res.append((letter, ctr))
            return res
        if s[index] == letter:
            return encode_recursive(s, index + 1, letter, ctr + 1, res)

        res.append((letter, ctr))
        return encode_recursive(s, index + 1, s[index], 1, res)
    return encode_recursive(s, 1, s[0], 1, [])
#### Fonction principale


def main():
    """methode qui test les fonction artcode"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
