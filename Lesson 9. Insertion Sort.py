"""
Алгоритм сортировки вставками.
Сложность: O(n*n)
https://www.youtube.com/watch?v=jMWvNTp_wFA&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=9
"""

mas = [-3, 5, 0, -8, 1, 10]
N = len(mas)

for i in range(1, N):
    for j in range(i, 0, -1):
        if mas[j] < mas[j-1]:
            mas[j], mas[j-1] = mas[j-1], mas[j]
        else:
            break

print(mas)
