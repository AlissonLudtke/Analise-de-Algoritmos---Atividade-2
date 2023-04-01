def buscaOrdenada(vetor, elemento):
    esquerda, direita = 1, len(vetor)
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio - 1] == elemento:
            return meio
        elif vetor[meio - 1] < elemento:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
