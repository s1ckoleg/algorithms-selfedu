"""
Необходим для определения кратчайших путей к каждой вершине графа. Отличается от алгоритма Дейкстры тем, что работает
с отрицательными значениями дуг и сразу находит кратчайшее расстояния между всеми парами вершин.
https://www.youtube.com/watch?v=ipWZ-d1l00s&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=4
"""

import math


def get_path(P, end, start):  # поиск кратчайшего пути
    path = [end]
    while end != start:
        end = P[end][start]
        path.append(end)

    return path


V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],  # матрица смежности графа
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0]]

N = len(V)  # число вершин в графе
P = [[v for v in range(N)] for u in range(N)]  # начальный список предыдущих вершин для поиска кратчайших маршрутов

for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]  # расстояние через дополнительную вершину
            if V[i][j] > d:
                V[i][j] = d
                P[i][j] = k

start = 0
end = 7
print(get_path(P, end, start)[::-1])
