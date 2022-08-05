"""
Быстрый алгоритм сортировки методом слияния. Подходит для сортировки больших массивов (десятки тысяч и миллионы
элементов).
Сложность: O(N*log(N))
https://www.youtube.com/watch?v=SnzZ61aCVxc&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=12
"""


def merge_lists(a, b):  # функция слияния двух отсортированных списков из Lesson 11
    result = []

    n = len(a)
    m = len(b)

    i = 0
    j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result += a[i:] + b[j:]

    return result


def split_and_merge_lists(a):  # функция деления списка и слияния списков в общий отсортированный список
    n = len(a) // 2  # делим массив на две (примерно) равные части
    a1 = a[:n]  # элементы до половины
    a2 = a[n:]  # элементы после половины

    if len(a1) > 1:  # если длина первого списка больше 1, то делим его ещё раз
        a1 = split_and_merge_lists(a1)
    if len(a2) > 1:   # если длина второго списка больше 1, то делим его ещё раз
        a2 = split_and_merge_lists(a2)

    return merge_lists(a1, a2)  # слияние двух отсортированных списков в один


a = [9, 5, -3, 4, 7, 8, -8]
sorted_a = split_and_merge_lists(a)

print(sorted_a)
