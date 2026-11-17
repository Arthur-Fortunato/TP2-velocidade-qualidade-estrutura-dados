def primeiro_duplicado(lista):
    tabela = {}
    for palavra in lista:
        if palavra in tabela:
            return palavra
        else:
            tabela[palavra] = True
    return None

# teste
lista1 = ["banana", "uva", "maça", "laranja", "uva"]
lista2 = ["azul", "verde", "amarelo", "vermelho", "azul"]
lista3 = ["python", "java", "c", "java", "c++"]

print(f"Primeiro duplicado da lista 1: {primeiro_duplicado(lista1)}")
print(f"Primeiro duplicado da lista 2: {primeiro_duplicado(lista2)}")
print(f"Primeiro duplicado da lista 3: {primeiro_duplicado(lista3)}")