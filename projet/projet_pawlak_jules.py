import time
import math
import random

print("================================== Projet Chiffrement PAWLAK Jules ==================================")

message = input("\nEntrez le message à chiffrer (lettres majuscules uniquement) : ")
print("\nChoisissez l'algorithme :")
print("1. Affine (Chiffrement mathématique classique)")
print("2. RSA (Chiffrement asymétrique moderne)")
choix = input("Votre choix (1/2) : ")

print("\n" + "==================================")

if choix == '1': # Chiffrement affine 
    print("--- CHIFFREMENT AFFINE ---")

    a = int(input("Entrez le coefficient 'a' (doit être impair, sauf 13) : ")) # L'utilisateur choisis les coefficients
    b = int(input("Entrez le coefficient 'b' : ")) # L'utilisateur choisis les coefficients
    
    message_chiffre = ""
    for lettre in message:
        chiffre_clair = ord(lettre) - 65 # Permet de transformer la lettre en chiffre
        chiffre_crypte = (a * chiffre_clair + b) % 26 # y = (a * x + b) modulo 26
        message_chiffre += chr(chiffre_crypte + 65) # contaténation du chiffre dans le message
    print(f"\nMessage chiffré : {message_chiffre}")
    
    # l'inverse modulaire de 'a' modulo 26 permet de déchiffrer le chiffre.
    # La fonction pow(a, -1, 26) sert a trouver l'inverse modulaire.
    inverse_a = pow(a, -1, 26)
    
    debut = time.perf_counter() # on commence le temps a mesurer
    message_dechiffre = ""
    
    for lettre in message_chiffre:
        chiffre_crypte = ord(lettre) - 65
        chiffre_clair = (inverse_a * (chiffre_crypte - b)) % 26 # On prend les opérations inverses
        message_dechiffre += chr(chiffre_clair + 65)
        
    fin = time.perf_counter() # on arrete le chronometre
    
    print(f"Message déchiffré : {message_dechiffre}")
    print(f"Temps de déchiffrement : {(fin - debut)*1000:.4f} millisecondes")

elif choix == '2': # Chiffrement RSA
    print("--- CHIFFREMENT RSA ---")
    print("Création automatique des clés...")
    
    # On prend deux nombres premiers au hasard (p et q)
    # On donne une petite liste pré-calculée
    nombres_premiers = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157]
    p = random.choice(nombres_premiers)
    q = random.choice(nombres_premiers)
    while p == q: # permet d'avoir p et q different
        q = random.choice(nombres_premiers)
    n = p * q
    phi = (p - 1) * (q - 1)
    # On choisit e (la clé de verrouillage)
    e = 3
    while math.gcd(e, phi) != 1:
        e += 2
    # On calcule d (la clé secrète de déverrouillage)
    d = pow(e, -1, phi)
    print(f"Clé publique (pour verrouiller) : n={n}, e={e}")
    print(f"Clé privée (pour déverrouiller) : d={d}")
    
    message_chiffre = [] # En RSA, on stocke des grands nombres, pas des lettres
    for lettre in message:
        # On prend le code de la lettre (ex: A=65)
        code_lettre = ord(lettre)
        
        # La formule de chiffrement est : C = (code_lettre puissance e) modulo n
        bloc_crypte = (code_lettre ** e) % n
        message_chiffre.append(bloc_crypte)
        
    print(f"\nMessage chiffré (nombres) : {message_chiffre}")

    debut = time.perf_counter()
    message_dechiffre = ""
    
    for bloc_crypte in message_chiffre:
        # La formule de déchiffrement est : code = (bloc_crypte puissance d) modulo n
        code_lettre = (bloc_crypte ** d) % n
        message_dechiffre += chr(code_lettre)
        
    fin = time.perf_counter()
    
    print(f"Message déchiffré : {message_dechiffre}")
    print(f"Temps de déchiffrement : {(fin - debut)*1000:.4f} millisecondes")

else:
    print("Choix invalide.")