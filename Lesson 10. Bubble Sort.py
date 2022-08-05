"""
Алгоритм сортировки пузырьком.
Сложность: O(n*n)
https://www.youtube.com/watch?v=5BuCMzKYagg&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=10
"""

mas = [7, 5, -8, 0, 10, 1]
N = len(mas)

for i in range(0, N-1):
    for j in range(0, N-1-i):  # проход по оставшимся не отсортированным элементам массива
        if mas[j] > mas[j+1]:
            mas[j], mas[j+1] = mas[j+1], mas[j]

print(mas)
