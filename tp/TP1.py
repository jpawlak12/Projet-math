import math

################## 1.1 ##################

n = 2026
d = 7
quotient = n // d
reste = n % d
print(quotient, reste)
print(quotient*d+reste==n)

################## 1.2 ##################

n = 123456789
print(n%10)
print(n//10)

################## 2.1 ##################

ecart = 0.0
for i in range(1000):
    ecart = ecart + 0.1
print(ecart)
print(ecart - 100)

################## 2.2 ##################

def presque_egaux(a, b):
    return abs(a - b) <= 1e-9

print(presque_egaux(0.1 + 0.2, 0.3))

################## 3.1 ##################

for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)

################## 3.2 ##################

n = 100
resultat = 0
for i in range(1, n + 1):
    resultat = resultat + i
print(resultat)
print(n * (n + 1) // 2)

################## 4.1 ##################

def nombre_de_chiffres(n):
    compte = 1
    while n >= 10:
        n = n // 10
        compte =+ compte
    return compte

print(nombre_de_chiffres(2026))
print(nombre_de_chiffres(7))

################## 5.1 ##################

def heron(a, tolerance=1e-12):
    if a < 0:
        raise ValueError("choisiez une valeur valable")
    if a == 0:
        return 0.0
    x = float(a)
    tours = 0
    while True:
        suivant = 0.5 * (x + a / x)
        tours = tours + 1
        if abs(suivant - x) <= tolerance * abs(suivant):
            return suivant
        x = suivant

print(heron(2))
print(math.sqrt(2))