"""
Алгоритм сортировки выбором.
Сложность: О(n*n)
https://www.youtube.com/watch?v=eI1ZuXVOmng&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=8
"""

mas = [-3, 5, 0, -8, 1, -10]
N = len(mas)

for i in range(N-1):
    m = mas[i]  # хранит минимальное значение
    p = i       # хранит индекс минимального значения

    for j in range(i+1, N):  # поиск минимального среди оставшихся элементов
        if m > mas[j]:
            m = mas[j]
            p = j

    if p != i:  # обмен позициями, если было найдено минимальное значение
        t = mas[i]
        mas[i] = mas[p]
        mas[p] = t

print(mas)


