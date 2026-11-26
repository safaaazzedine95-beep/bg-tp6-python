
# TP6 - PRAVAN - Exercice 1 (avec le module json)

import json  # Importation d'un module (slide 46)
              # Encodage et décodage JSON (slide 33)

# Liste de tuples : stockage de plusieurs éléments dans une seule variable (slide 28)
students = [
    (1000, "JOHN", "DOE", 14, 5),
    (2000, "BOB", "CARLTON", 7, 1),
    (3000, "RAYANE", "SMITH", 13, 3),
]


# Déclaration d'une fonction avec paramètre et valeur de retour (slides 40 et 41)
# Le paramètre note est de type float et le résultat est de type booléen.
def B(note: float) -> bool:
    if note >= 10:  # Condition if (slide 35)
        return True
    return False


# Déclaration d'une fonction avec paramètre et valeur de retour (slides 40 et 41)
# La fonction A reçoit une liste et retourne une chaîne JSON.
def A(students: list) -> str:
    resultat = []

    for s in students:  # Boucle for pour parcourir une liste (slide 39)
        mat = s[0]  # Accès à un élément par son index (slide 26)
        note = s[3]

        if B(note):  # Appel d'une fonction (slide 40)
            resultat.append({"mat": mat, "result": "ADMIS"})
        else:  # Condition if / else (slide 35)
            resultat.append({"mat": mat, "result": "AJOURNE"})

    # Transformation de la liste de dictionnaires en JSON (slide 33)
    return json.dumps(resultat)


# Déclaration d'une fonction sans paramètre (slide 40)
# La fonction C appelle A, qui appelle à son tour B.
def C():
    # Appel de la fonction A (slide 40)
    resultat_json = A(students)

    # Décodage du JSON en liste Python avec json.loads() (slide 33)
    donnees = json.loads(resultat_json)

    # Parcours de la liste avec une boucle for (slide 39)
    for item in donnees:
        # Affichage avec print() et utilisation d'une chaîne formatée (f-string)
        print(f"{item['mat']}: {item['result']}")


# Point d'entrée du programme Python (slide 55)
if __name__ == "__main__":
    C()
