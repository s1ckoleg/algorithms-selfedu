"""
Алгоритм слияния двух упорядоченных списков, так, чтобы результирующий список тоже был упорядоченным.
https://www.youtube.com/watch?v=GqieI_1yh40&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=11
"""

a = [1, 4, 10, 11]
b = [2, 3, 3, 4, 8]
result = []

N = len(a)
M = len(b)

i = 0
j = 0

while i < N and j < M:
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result += a[i:] + b[j:]  # добавляем элементы, которые остались в каком-то из списков

print(result)
