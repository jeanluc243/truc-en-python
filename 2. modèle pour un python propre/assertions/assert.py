"""
voici un example simple qui montre comment les assertions peut devenir pratique
c'est un exemple qui peut subvenir en developpement de tom programs.

Suppose que tu developpe un magasin en ligne avec python.
tu es en train de travailler sur la fonctionnalited de payement , et eventuellement 
tu ecris le code suivant pour la aplliquer_reduction :
"""

def appliquer_reduction(produit, reduction):
    prix = int(produit['prix'] * (1.0 - reduction))
    assert 0 <= prix <= produit['prix']
    return prix

#----------------------------------------------------

chaussure = {'nom' : 'jeans', 'prix' : 1400 }

appliquer_reduction(chaussure, 0.25)

