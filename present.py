nom = input("entrez votre nom: ")
age = int(input("entrez votre age: "))
Taille = float(input("entrez votre taille: "))
Stage = input("ETes vous en stage? (oui/non): ")
print(f"bonjour {nom},vous avez {age} ans et vous mesurez {Taille} m.")
if Stage == "oui":
    print("Vous êtes en stage.")
else:
    print("Vous n'êtes pas en stage.")
