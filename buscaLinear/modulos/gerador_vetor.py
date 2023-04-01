import random

TAMANHO_RAND = 10

def gerar_vetor_aleatorio(tamanho):
    vetor = []
    for i in range(tamanho):
        num_aleatorio = random.randint(1, TAMANHO_RAND)
        while num_aleatorio in vetor:
            num_aleatorio = random.randint(1, TAMANHO_RAND)
        vetor.append(num_aleatorio)
    return vetor
