
# TP6 - PRAVAN - Exercice 2 : comptes bancaires (avec le module json)

import json  # Importation du module json pour encoder et décoder les données JSON (slide 33)

# Liste de dictionnaires : chaque dictionnaire contient les informations d'un compte (slides 31, 32)
C = [
    {"nom": "compte1", "solde": 3000},
    {"nom": "compte2", "solde": 500},
    {"nom": "compte3", "solde": 1000},
]


# Déclaration d'une fonction avec paramètres et valeur de retour (slides 40, 41)
# La fonction deposer reçoit un compte et une somme, puis retourne un JSON.
def deposer(c: dict, somme: float) -> str:
    if somme <= 0:  # Condition if pour vérifier si le montant est valide (slide 35)
        return json.dumps({"erreur": "montant invalide"})
    c["solde"] = c["solde"] + somme
    return json.dumps({"compte": c["nom"], "solde": c["solde"]})


# Déclaration d'une fonction avec paramètres et valeur de retour (slides 40, 41)
# La fonction retirer permet de retirer une somme du solde d'un compte.
def retirer(c: dict, somme: float) -> str:
    if somme <= 0:  # Vérification du montant avec une condition if (slide 35)
        return json.dumps({"erreur": "montant invalide"})
    if somme > c["solde"]:  # Vérification du solde disponible (slide 35)
        return json.dumps({"erreur": "solde insuffisant"})
    c["solde"] = c["solde"] - somme
    return json.dumps({"compte": c["nom"], "solde": c["solde"]})


# Déclaration d'une fonction avec paramètres et valeur de retour (slides 40, 41)
# La fonction afficher calcule et affiche le solde total des comptes.
def afficher(c: list) -> str:
    total = 0
    for compte in c:  # Boucle for pour parcourir la liste des comptes (slide 38)
        total = total + compte["solde"]
    print("Solde total :", total)
    return json.dumps({"total": total})


# Déclaration d'une fonction qui retourne une liste de dictionnaires au format JSON.
# La fonction filtre les comptes dont le solde est supérieur ou égal à 1000.
def filtre1000(c: list) -> str:
    resultat = []
    for compte in c:  # Parcours de la liste avec une boucle for (slide 38)
        if compte["solde"] >= 1000:  # Condition if (slide 35)
            resultat.append({"compte": compte["nom"], "solde": compte["solde"]})
    return json.dumps(resultat)  # Transformation de la liste de dictionnaires en JSON (slide 33)


# Déclaration d'une fonction avec un paramètre (slide 40)
# Cette fonction retourne le solde d'un compte pour l'utiliser comme clé de tri.
def get_solde(compte):
    return compte["solde"]


# Déclaration d'une fonction avec paramètres et valeur de retour (slides 40, 41)
# Tri des comptes par solde décroissant.
def trier(c: list) -> str:
    tries = sorted(c, key=get_solde, reverse=True)  # Tri d'une liste (notion liée au slide 27)
    resultat = []
    for compte in tries:  # Parcours de la liste triée avec une boucle for (slide 38)
        resultat.append({"compte": compte["nom"], "solde": compte["solde"]})
    return json.dumps(resultat)  # Encodage de la liste de dictionnaires en JSON (slide 33)


# Point d'entrée du programme : exécution des tests des fonctions (slide 55)
if __name__ == "__main__":
    print(deposer(C[1], 700))
    print(retirer(C[0], 500))
    print(retirer(C[2], 5000))
    print(afficher(C))
    print(filtre1000(C))
    print(trier(C))
