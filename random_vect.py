import BubbleSort, BubbleSortMelhorado, QuickSort, QuickSortMelhorado, InsertionSort
import ShellSort, SelectionSort, HeapSort, MergeSort
import time
import matplotlib.pyplot as plt
import pandas as pd
import random
import sys

sys.setrecursionlimit(10**5)

def random_vector(num):
    return [random.randint(1, num) for _ in range(num)]

def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

def plot_graph(vet_length, algorithm_times, title):
    plt.figure(figsize=(12, 8))
    plt.title(title)
    plt.xlabel("Tamanho do Vetor")
    plt.ylabel("Tempo de Execução (s)")
    plt.grid(True)

    for algo_name, times in algorithm_times.items():
        plt.plot(vet_length, times, label=algo_name, linewidth=3)

    plt.legend()
    plt.show()  # Exibe o gráfico interativamente

def main():
    sorting_algorithms = {
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

    vet_length = [1000, 5000, 10000, 15000, 20000, 25000]
    algorithm_times = {name: [] for name in sorting_algorithms.keys()}

    for num in vet_length:
        arr = random_vector(num)
        for algo_name, algo_func in sorting_algorithms.items():
            time_taken = measure_time(algo_func, arr)
            algorithm_times[algo_name].append(time_taken)

    plot_graph(vet_length, algorithm_times, "Comparação de Algoritmos de Ordenação - Vetor Aleatório")

if __name__ == "__main__":
    main()
