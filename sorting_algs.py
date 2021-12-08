import random
import sys

sys.setrecursionlimit(100000)

# Extra sorts
def counting_sort(input_array, place_value):
    # init count array
    count_array = [0] * 10
    # get input array's size and init output_array
    input_size = len(input_array)
    output_array = [0] * input_size

    # fin place elements
    for i in range(input_size):
        place_element = (input_array[i] // place_value) % 10
        count_array[int(place_element)] += 1

    # sum up all previos values in count_array
    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    # reconstruct output array
    i = input_size - 1
    while i >= 0:
        current_element = input_array[i]
        place_element = (input_array[i] // place_value) % 10
        count_array[int(place_element)] -= 1
        new_position = count_array[int(place_element)]
        output_array[int(new_position)] = current_element
        i -= 1

    return output_array


def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        value = input_array[i]
        j = i - 1
        while j >= 0 and value < input_array[j]:
            input_array[j + 1] = input_array[j]
            j = j - 1
        input_array[j + 1] = value


# поразрядная сортировка
# возвращает итоговую перестановку эелементов массива A
# для того, чтобы можно было переставить элементы в любом другом массиве
def radix_argsort(input_array):
    # Step 1: find maximum element
    maximum_element = max(input_array)

    # Step 2: find number of digits in maximum element
    D = len(str(maximum_element))

    # Step 3: init place_value
    place_value = 1

    # Step 4: apply counting sort to each D
    output_array = input_array
    while D > 0:
        output_array = counting_sort(output_array, place_value)
        place_value *= 10
        D -= 1

    return output_array


def bucket_argsort(input_array):
    def insertion_sort(input_array):
        for i in range(1, len(input_array)):
            value = input_array[i]
            j = i - 1
            while j >= 0 and value < input_array[j]:
                input_array[j + 1] = input_array[j]
                j = j - 1
            input_array[j + 1] = value
            
    # check that graph not empty
    if input_array == []:
        return []
        
    # convert input array
    input_array = [(i, j) for i, j in enumerate(input_array)]
    # get max value and bucket's size
    max_value = max([i[1] for i in input_array])
    array_len = len(input_array)
    size = max_value / array_len + 1

    # Create empty buckets
    buckets_list = []
    for i in range(array_len):
        buckets_list.append([])

    # Put elements into the buckets
    for i in range(array_len):
        j = int(input_array[i][1] / size)
        if j != len(input_array):
            buckets_list[j].append(input_array[i])
        else:
            buckets_list[len(input_array) - 1].append(input_array[i])

    # Sort each bucket
    for i in range(array_len):
        insertion_sort(buckets_list[i])

    # Concat all buckets
    output_array = []
    for x in range(len(input_array)):
        output_array = output_array + buckets_list[x]

    return [i[0] for i in output_array] 


# QUICKSORT
def quick_argsort(array): 
    array = [(i, j) for i, j in enumerate(array)]
    random.shuffle(array)
    res = _quicksort(array, 0, len(array) - 1)
    return [i[0] for i in res]


def _partition(array, start, end):
    pivot = array[end][1]
    i = start - 1
    for j in range(start, end):
        if array[j][1] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def _insertion_sort(input_array, start, end):
    for i in range(start, end + 1):
        value = input_array[i][1]
        value_insert = input_array[i]
        j = i - 1
        while j >= 0 and value < input_array[j][1]:
            input_array[j + 1] = input_array[j]
            j = j - 1
        input_array[j + 1] = value_insert


def _quicksort(array, start, end):
    while (end - start) >= 50:
        p = _partition(array, start, end)
        _quicksort(array, start, p - 1)
        start = p + 1
    _insertion_sort(array, start, end)
    return array
