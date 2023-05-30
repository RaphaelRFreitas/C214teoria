# Classe base para os algoritmos de ordenação
class SortingAlgorithm:
    def sort(self, data):
        pass


# Implementação do Bubble Sort
class BubbleSort(SortingAlgorithm):
    def sort(self, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]


# Implementação do Insertion Sort
class InsertionSort(SortingAlgorithm):
    def sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key


# Implementação do Merge Sort
class MergeSort(SortingAlgorithm):
    def sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.sort(left_half)
            self.sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1


# Classe que utiliza o algoritmo de ordenação selecionado
class Sorter:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def sort_data(self, data):
        self.algorithm.sort(data)


# Exemplo de uso
data = [5, 2, 9, 1, 6]

# Utilizando Bubble Sort
algorithm = BubbleSort()
sorter = Sorter(algorithm)
sorter.sort_data(data)
print("Bubble Sort:", data)

# Utilizando Insertion Sort
algorithm = InsertionSort()
sorter = Sorter(algorithm)
sorter.sort_data(data)
print("Insertion Sort:", data)

# Utilizando Merge Sort
algorithm = MergeSort()
sorter = Sorter(algorithm)
sorter.sort_data(data)
print("Merge Sort:", data)
