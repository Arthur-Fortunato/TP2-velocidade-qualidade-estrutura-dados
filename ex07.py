def insertion_sort(lista):
    comparacoes = 0
    deslocamentos = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        anterior = i - 1
        while anterior >= 0:
            comparacoes += 1
            if lista[anterior] > atual:
                lista[anterior + 1] = lista[anterior]
                deslocamentos += 1
                anterior -= 1
            else:
                break
        lista[anterior + 1] = atual
    return lista, comparacoes, deslocamentos


listas = [
    [1, 2, 3, 4, 5, 7, 6, 8, 9, 10],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
]

for lista in listas:
    original = lista.copy()
    ordenada, comparacoes, deslocamentos = insertion_sort(lista)

    print(f"\nOriginal: {original}")
    print(f"Ordenada: {ordenada}")
    print(f"Comparações: {comparacoes} | Deslocamentos: {deslocamentos}")