class Stack:
    def __init__(self, capacidade):
        self.pilha = []
        self.capacidade = capacidade

    def inserir(self, elemento):
        if len(self.pilha) >= self.capacidade:
            print("Overflow --> Pilha cheia.")
        else:
            self.pilha.append(elemento)

    def remover(self):
        if len(self.pilha) == 0:
            print("Underflow --> Pilha vazia.")
        else:
            return self.pilha.pop()

    def mostrar(self):
        print(f"Estado atual da pilha: {self.pilha}")

pilha = Stack(2)
pilha.inserir(5)
pilha.mostrar()
pilha.inserir(10)
pilha.mostrar()
pilha.inserir(15) 
pilha.mostrar()

pilha.remover()
pilha.mostrar()
pilha.remover()
pilha.mostrar()
pilha.remover() 