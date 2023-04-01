import random

class BuscaBinaria:

    def __init__(self, tamanho_vetor, elemento_procurado, tamanho_rand):
        self.tamanho_vetor = tamanho_vetor
        self.elemento_procurado = elemento_procurado
        self.tamanho_rand = tamanho_rand
        self.vetor = []

    def gerar_vetor_aleatorio(self):
        while len(self.vetor) < self.tamanho_vetor:
            numero = random.randint(0, self.tamanho_rand)
            if numero not in self.vetor:
                self.vetor.append(numero)

    def bubble_sort(self):
        n = len(self.vetor)
        for i in range(n):
            for j in range(n-i-1):
                if self.vetor[j] > self.vetor[j+1]:
                    self.vetor[j], self.vetor[j+1] = self.vetor[j+1], self.vetor[j]

    def busca_binaria(self):
        esquerda, direita = 0, len(self.vetor) - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if self.vetor[meio] == self.elemento_procurado:
                return meio
            elif self.vetor[meio] < self.elemento_procurado:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return -1
