import time
from modulos import gerar_vetor_aleatorio, busca_linear

TAMANHO_VETOR = 10
ELEMENTO_PROCURADO = 10

tempo_inicial = time.perf_counter()

vetor_aleatorio = gerar_vetor_aleatorio(TAMANHO_VETOR)
print("Vetor gerado: ", vetor_aleatorio)

resultado_busca = busca_linear(vetor_aleatorio, ELEMENTO_PROCURADO)
if resultado_busca != -1:
    print("O elemento", ELEMENTO_PROCURADO, "foi encontrado na posição", resultado_busca)
else:
    print("O elemento", ELEMENTO_PROCURADO, "não foi encontrado no vetor.")

tempo_final = time.perf_counter()
tempo_execucao = tempo_final - tempo_inicial

print("Tempo de execução: ", tempo_execucao)
