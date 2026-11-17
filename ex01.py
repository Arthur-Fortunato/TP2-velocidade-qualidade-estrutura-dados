def aninhado(lista):
    maior_salvo = None
    comparacoes = 0
    for numero in lista:
        quantidade = 0
        for outro in lista:
            comparacoes += 1
            if numero == outro:
                quantidade += 1
        if quantidade == 1:
            if maior_salvo is None or numero > maior_salvo:
                maior_salvo = numero
    return maior_salvo, comparacoes

def hash(lista):
    frequencias = {}
    acessos = 0
    for numero in lista:
        acessos += 1
        if numero in frequencias:
            frequencias[numero] += 1
            acessos += 1
        else:
            frequencias[numero] = 1
            acessos += 1
    maior_salvo = None
    for numero, quantidade in frequencias.items():
        acessos += 1
        if quantidade == 1:
            if maior_salvo is None or numero > maior_salvo:
                maior_salvo = numero
    return maior_salvo, acessos

# teste
import random
tamanhos = [10, 100, 500]

for tamanho in tamanhos:
    numeros = random.choices(range(1, 101), k=tamanho)
    resultado1, comparacoes = aninhado(numeros)
    resultado2, acessos = hash(numeros)
    
    print(f"\nTamanho da lista: {tamanho}")
    print(f"Quadrático --> maior número(único) é {resultado1} | Comparações: {comparacoes}")
    print(f"Hash Table --> maior número(único) é {resultado2} | Acessos: {acessos}")
    print(f"Resultados iguais: {resultado1 == resultado2}")