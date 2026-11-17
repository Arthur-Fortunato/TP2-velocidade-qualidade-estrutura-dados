def intersecao(lista1, lista2):
    tabela = {}
    resultado = []
    for numero in lista1:
        tabela[numero] = True
    for numero in lista2:
        if numero in tabela:
            resultado.append(numero)
            tabela.pop(numero)
    return resultado

# teste
import random
tamanhos = [100, 1000, 10000]

for tamanho in tamanhos:
    lista1 = random.choices(range(1, tamanho * 2), k=tamanho)
    lista2 = random.choices(range(1, tamanho * 2), k=tamanho)
    resultado = intersecao(lista1, lista2)

    print(f"\nTamanho da lista: {tamanho}")
    print(f"Quantidade de elementos em comum: {len(resultado)}")
    print(f"Interseção: {resultado[:10]}")