def bubbleSort(vetor):
    n = len(vetor)
    for i in range(n):
        for j in range(1, n-i):
            if vetor[j] < vetor[j-1]:
                vetor[j], vetor[j-1] = vetor[j-1], vetor[j]
