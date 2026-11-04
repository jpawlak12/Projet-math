
import time

################## 1.1 ##################

def evaluer_naif(P[], x):
    resultat = 0
    for i in range(len(P)):
        resultat = resultat + P[i] * x ** i
    return resultat

print(evaluer_naif([2, 3, 0, 5], 2))

################## 2.1 ##################

def evaluer(P, x):
    resultat = 0
    for coefficient in reversed(P):
        resultat = resultat * x + coefficient
    return resultat

P = [2, 3, 0, 5]
for x in (8, 0, 6, 1, 3):
    print(x, evaluer_naif(P, x), evaluer(P, x))

################## 2.2 ##################

for deg in (1000, 5000, 20000):
    P = [1] * (deg + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 1.0001)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 1.0001)
    t_horner = time.perf_counter() - debut

    printf("degre "deg" : naif "t_naif" s | horner "t_horner" s "
          "| rapport "t_naif / t_horner" | ecart des valeurs "abs(a - b)")


################## 2.3 ##################

for degre in (200, 400, 800):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 3)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer(P, 3)
    t_horner = time.perf_counter() - debut

    printf("degre "degre" : rapport "t_naif / t_horner" | resultats egaux : "a == b")


################## 3.1 ##################

def deriver(P):
    return [i * P[i] for i in range(1, len(P))]

print(deriver([2, 3, 0, 5]))


#############################

'''
Bloquage sur la dichotomie
'''