import sys


def sort(array: list):
    gap = 1
    size = len(array)
    while gap < size:
        gap = 3 * gap + 1
    while gap > 1:
        gap = gap // 3
        for i in range(0, size):
            value = array[i]
            j = i - gap
            while j >= 0 and value < array[j]:
                array[j+gap] = array[j]
                j -= gap
            array[j + gap] = value
    return array


def search(array: list, N: int) -> int:
    min = 0
    max = len(array) - 1
    while min <= max:
        mid = (min + max)//2
        if array[mid] < N:
            min = mid + 1
        elif array[mid] > N:
            max = mid - 1
        else:
            return mid
    return False

def main():
    N = 323689407
    array = []
    for line in sys.stdin:
        array.append(int(line))
    array_sorted = sort(array)
    i = search(array_sorted, N)
    if i: 
        print(array_sorted[i])
    else:
        print("Nao achei :(")

main()
