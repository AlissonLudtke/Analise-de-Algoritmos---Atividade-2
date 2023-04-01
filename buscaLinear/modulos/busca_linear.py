def busca_linear(vetor, elemento):
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            return i
    return -1
