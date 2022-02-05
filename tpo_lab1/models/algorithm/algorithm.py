# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i,
# что является индексом в arr[]. n - размер кучи
def heapify(array, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and array[i] < array[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and array[largest] < array[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # свап

        # Применяем heapify к корню.
        heapify(array, n, largest)


# Основная функция для сортировки массива заданного размера
def heap_sort(array):
    n = len(array)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(array, n, i)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # свап
        heapify(array, i, 0)
