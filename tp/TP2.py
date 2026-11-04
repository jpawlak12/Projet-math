################## 1.1 ##################

def diviseurs(n):
    resultat = []
    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)
    return resultat

print(diviseurs(28))

################## 2.1 ##################

def pgcd_naif(a, b):
    div = 1
    for d in range(1, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            div = d
    return div

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(pgcd_naif(1071, 462), pgcd(1071, 462))

################## 3.1 ##################

for n in (10_007, 100_003, 1_000_003):
    t_naif = duree(est_premier_naif, n)
    t_rac = duree(est_premier, n)
    printf(n" : naif "t_naif" s | racine "t_rac" s")

################## 4.1 ##################

debut = time.perf_counter()
p = crible(100_000)
t_crible = time.perf_counter() - debut

debut = time.perf_counter()
combien = sum(1 for n in range(100_001) if est_premier(n))
t_un_par_un = time.perf_counter() - debut

print(len(p), combien)
printf("crible "t_crible" s | pour un "t_un_par_un:.4f" s")

################## 5.1 ##################

def facteurs(n):
    resultat = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat.append(d)
            n = n // d
        d = d + 1
    if n > 1:
        resultat.append(n)
    return resultat

f = facteurs(360)
print(f)

produit = 1
for x in f:
    produit = produit * x
print(produit)