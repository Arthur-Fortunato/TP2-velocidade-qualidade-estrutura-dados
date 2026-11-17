def primeira_letra_unica(texto):
    frequencias = {}
    for char in texto:
        if char in frequencias:
            frequencias[char] += 1
        else:
            frequencias[char] = 1
    for char in texto:
        if frequencias[char] == 1:
            return char
    return None

textos = [
    "abacaxi",
    "aabbccde",
    "programa",
    "aabbcc",
    "python"
]

# teste
for texto in textos:
    print(f"Texto: {texto} --> Primeiro não repetido: {primeira_letra_unica(texto)}")