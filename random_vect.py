import BubbleSort, BubbleSortMelhorado, QuickSort, QuickSortMelhorado, InsertionSort
import ShellSort, SelectionSort, HeapSort, MergeSort
from scipy.ndimage import gaussian_filter1d
import time
import matplotlib.pyplot as plt
import random
import sys

sys.setrecursionlimit(10**5)  # Aumenta o limite de recursão para evitar problemas com grandes vetores

def vetor_aleatorio(num):
    return [random.randint(1, num) for _ in range(num)]  # Gera um vetor com valores aleatórios

def mtime(funcao_ord, vet):  # Função para medir o tempo de execução
    start = time.perf_counter()
    funcao_ord(vet)
    end = time.perf_counter()
    return end - start  # Retorna o tempo de execução

def plot_graph(vet_length, tempo_exe, title):
    plt.figure(figsize=(12, 8))
    plt.title(title)
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Tempo de Execução (s)")
    plt.grid(True)

    for ord_name, times in tempo_exe.items():
        filtro = gaussian_filter1d(times, sigma=1)  # Aplica filtro Gaussiano para suavizar
        plt.plot(vet_length, filtro, label=ord_name, linewidth=3)

    plt.legend(loc='best')  # Posiciona a legenda automaticamente no melhor lugar
    plt.show()  # Exibe o gráfico

def main():
    algoritmo_ordenacao = { # Aqui você escolhe os algoritmos que deseja comparar
        "Bubble Sort": BubbleSort.bubble_sort,
        "Bubble Sort Melhorado": BubbleSortMelhorado.bubble_sort,
        "Quick Sort": QuickSort.quick_sort,
        "Quick Sort Melhorado": QuickSortMelhorado.quick_sort,
        "Insertion Sort": InsertionSort.insertion_sort,
        "Shell Sort": ShellSort.shell_sort,
        "Selection Sort": SelectionSort.selection_sort,
        "Heap Sort": HeapSort.heap_sort,
        "Merge Sort": MergeSort.merge_sort,
    }

    vet_length = [1000, 5000, 10000, 15000, 20000, 25000]  # Tamanhos dos vetores para teste
    tempo_exe = {name: [] for name in algoritmo_ordenacao.keys()}

    for num in vet_length:
        vet = vetor_aleatorio(num)  # Gera vetor aleatório
        for ord_name, algo_func in algoritmo_ordenacao.items():
            tempo_levado = mtime(algo_func, vet)
            tempo_exe[ord_name].append(tempo_levado)

    plot_graph(vet_length, tempo_exe, "Comparação de Algoritmos de Ordenação - Vetor Aleatório")

if __name__ == "__main__":
    main()
