import BubbleSort, BubbleSortMelhorado, QuickSort, QuickSortMelhorado, InsertionSort
import ShellSort, SelectionSort, HeapSort, MergeSort
from scipy.ndimage import gaussian_filter1d
import time
import matplotlib.pyplot as plt
import sys



sys.setrecursionlimit(10**5) #Não estoura o limite de recursão

def inversely_ordered_vector(num):
    return list(range(num, 0, -1))  # Gera um vetor inversamente ordenado

def mtime(funcao_ord, vet): # Função para medir o tempo de execução
    start = time.perf_counter()
    funcao_ord(vet)
    end = time.perf_counter()
    return end - start # Retorna o tempo de execução

def plot_graph(vet_length, tempo_exe, title):
    plt.figure(figsize=(12, 8))
    plt.title(title)
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Tempo de Execução (s)")
    plt.grid(True)

    for ord_name, times in tempo_exe.items():
        filtro = gaussian_filter1d(times, sigma=1) # Aplica um filtro gaussiano para suavizar o gráfico
        plt.plot(vet_length, filtro, label=ord_name, linewidth=3)

    plt.legend(loc='best') # Adiciona a legenda ao gráfico no melhor lugar que ele julga
    plt.savefig("ordenado_inversamente.png") # Salva o gráfico em uma imagem
    plt.show()  # Exibe o gráfico interativamente

def main():
    algoritmo_ordenacao = { #Aqui é onde você irá escolher os algoritmos que deseja ver o tempo de execução, basta adicionar ou remover da lista
        # "Bubble Sort": BubbleSort.bubble_sort,
        # "Bubble Sort Melhorado": BubbleSortMelhorado.bubble_sort,
        # "Quick Sort": QuickSort.quick_sort,
        # "Quick Sort Melhorado": QuickSortMelhorado.quick_sort,
        # "Insertion Sort": InsertionSort.insertion_sort,
        # "Shell Sort": ShellSort.shell_sort,
        # "Selection Sort": SelectionSort.selection_sort,
        # "Heap Sort": HeapSort.heap_sort,
        "Merge Sort": MergeSort.merge_sort,
    }

    vet_length = [1000, 5000, 10000, 15000, 20000, 25000] # Tamanhos dos vetores que serão testados
    tempo_exe = {name: [] for name in algoritmo_ordenacao.keys()}

    for num in vet_length:
        vet = inversely_ordered_vector(num)  # Gerar vetor inversamente ordenado
        for ord_name, algo_func in algoritmo_ordenacao.items():
            tempo_levado = mtime(algo_func, vet)
            tempo_exe[ord_name].append(tempo_levado)

    plot_graph(vet_length, tempo_exe, "Comparação de Algoritmos de Ordenação - Vetor Inversamente Ordenado")

if __name__ == "__main__":
    main()
