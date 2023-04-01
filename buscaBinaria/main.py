from busca_binaria import BuscaBinaria
import time

if __name__ == '__main__':
    TAMANHO_VETOR = 10
    ELEMENTO_PROCURADO = 1
    TAMANHO_RAND = 10

    busca = BuscaBinaria(TAMANHO_VETOR, ELEMENTO_PROCURADO, TAMANHO_RAND)
    busca.gerar_vetor_aleatorio()

    inicio = time.time()
    busca.bubble_sort()
    posicao = busca.busca_binaria()
    fim = time.time()

    if posicao != -1:
        print(f"O elemento {ELEMENTO_PROCURADO} foi encontrado na posição {posicao} do vetor.")
    else:
        print(f"O elemento {ELEMENTO_PROCURADO} não foi encontrado no vetor.")


    print(f"Tempo de execução: {fim - inicio:.6f} segundos.")
