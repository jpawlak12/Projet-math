################## 1.1 ##################

def lettre_vers_nombre(c):
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    return chr(ord("A") + n % 26)

print(lettre_vers_nombre("C"), nombre_vers_lettre(2))
print((nombre_vers_lettre(lettre_vers_nombre("C"))))

#############################

'''
La suite du TP5 na pas pu etre abbordé convenablement a cause d'un trop gros temps consacré pour les autres TP

'''