def selection_sort(lista):
    comparacoes = 0
    trocas = 0
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
        trocas += 1
    return lista, comparacoes, trocas

listas = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 1, 3, 2, 5]
]

for lista in listas:
    original = lista.copy()
    ordenada, comparacoes, trocas = selection_sort(lista)

    print(f"\nOriginal: {original}")
    print(f"Ordenada: {ordenada}")
    print(f"Comparações: {comparacoes} | Trocas: {trocas}")