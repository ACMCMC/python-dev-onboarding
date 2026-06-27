# calcul TVA — vieux module, plus appele depuis v3 mais on garde

def tva_ligne(*, ht, taux):
    return round(ht * taux, 2)


def ttc(*, ht, taux):
    return ht + tva_ligne(ht=ht, taux=taux)
