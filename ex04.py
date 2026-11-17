def letra_ausente(texto):
    presentes = {}
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    for letra in texto.lower():
        if letra in alfabeto:
            presentes[letra] = True
    for letra in alfabeto:
        if letra not in presentes:
            return letra
    return None

texto1 = "abcdefghijklmnopqrstuvwxy" 
texto2 = "ABCDEFGHIJKLMNOPQRSTUVWXY"
texto3 = "ab1cd2e123!#$ fghijklmnopqrstuvwxyz"
texto4 = "abcdefghijklmnopqrstuvwxyz"

print(f"Texto 1: {letra_ausente(texto1)}")
print(f"Texto 2: {letra_ausente(texto2)}")
print(f"Texto 3: {letra_ausente(texto3)}")
print(f"Texto 4: {letra_ausente(texto4)}")