################## 1.1 ##################

def transposee(A):
    lignes = len(A)
    colonnes = len(A[0])
    return [[A[i][j] for i in range(lignes)] for j in range(colonnes)]

print(transposee([[1, 2, 3], [4, 5, 6]]))

################## 2.1 ##################

def produit(A, B):
    n, p = len(A), len(A[0])
    if len(B) != p:
        raise ValueError("mauvaises valeurs")
    q = len(B[0])
    Coef = [[0] * q for i in range(n)]
    for i in range(n):
        for j in range(q):
            resultat = 0
            for k in range(p):
                resultat = resultat + A[i][k] * B[k][j]
            Coef[i][j] = resultat
    return Coef

print(produit([[1, 2], [3, 4]], [[0, 1], [1, 0]]))

################## 2.2 ##################


import random
import time

random.seed(42)

def matrice_aleatoire(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

for n in (40, 80, 120):
    A = matrice_aleatoire(n)
    B = matrice_aleatoire(n)
    debut = time.perf_counter()
    produit(A, B)
    print(f"n = {n:>3} : {time.perf_counter() - debut:.4f} s")

################## 3.1 ##################

n = 120
A = matrice_aleatoire(n)
B = matrice_aleatoire(n)

debut = time.perf_counter()
produit(A, B)
t_python = time.perf_counter() - debut

An, Bn = np.array(A), np.array(B)
debut = time.perf_counter()
An @ Bn
t = time.perf_counter() - debut

printf("python pur "t_python" s")
printf("numpy "t" s")
print("rapport :", round(t_python / max(t, 1e-9)))

#############################

'''
Bloquage sur le pivot de gauss
'''
