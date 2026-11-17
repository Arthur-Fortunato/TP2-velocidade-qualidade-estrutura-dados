class Queue:
    def __init__(self, capacidade):
        self.fila = [None] * capacidade
        self.capacidade = capacidade
        self.inicio = 0
        self.fim = 0
        self.tamanho = 0

    def inserir(self, elemento):
        if self.tamanho == self.capacidade:
            print("Overflow --> Fila cheia.")
        else:
            self.fila[self.fim] = elemento
            self.fim = (self.fim + 1) % self.capacidade
            self.tamanho += 1

    def remover(self):
        if self.tamanho == 0:
            print("Underflow --> Fila vazia.")
        else:
            elemento = self.fila[self.inicio]
            self.fila[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.capacidade
            self.tamanho -= 1
            return elemento

    def mostrar(self):
        print(f"Fila: {self.fila}")
        print(f"Início: {self.inicio} - Fim: {self.fim} - Tamanho: {self.tamanho}")

fila = Queue(2)
fila.mostrar()

fila.inserir(5)
fila.mostrar()
fila.inserir(10)
fila.mostrar()
fila.inserir(15)
fila.mostrar()

print(f"Removido: {fila.remover()}")
fila.mostrar()
fila.inserir(15)
fila.mostrar()

print(f"Removido: {fila.remover()}")
fila.mostrar()
print(f"Removido: {fila.remover()}")
fila.mostrar()

fila.remover()  