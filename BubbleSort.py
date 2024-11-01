def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Compara o elemento atual com o próximo elemento
            if arr[j] > arr[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
