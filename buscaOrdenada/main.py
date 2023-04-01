import random
from modulos import bubbleSort, buscaOrdenada, time

TAMANHO_VETOR = 500000
ELEMENTO_PROCURADO = 500000
TAMANHO_RAND = 500000

tempo_inicial = time.perf_counter()

vetor = random.sample(range(1,TAMANHO_RAND+1), TAMANHO_VETOR)

bubbleSort(vetor)

resultado = buscaOrdenada(vetor, ELEMENTO_PROCURADO)
if resultado != -1:
    print(vetor, "\nO elemento", ELEMENTO_PROCURADO, "foi encontrado na posição:", resultado)
else:
    print("O elemento", ELEMENTO_PROCURADO, "não foi encontrado no vetor:", vetor)

tempo_final = time.perf_counter()
tempo_execucao = tempo_final - tempo_inicial

print("Tempo de execução:", tempo_execucao)
