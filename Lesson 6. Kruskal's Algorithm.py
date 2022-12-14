"""
Необходим для поиска минимального остова взвешенного неориентированного графа.
Остов — это подграф данного графа, содержащий все его вершины без циклов.
https://www.youtube.com/watch?v=KDKACf8tcnM&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=6
"""

# список рёбер графа вида (длина, вершина 1, вершина 2)
R = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6), (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

Rs = sorted(R, key=lambda x: x[0])  # сортируем список рёбер по длине
U = set()                           # список соединённых вершин
D = {}                              # словарь списка изолированных групп вершин
T = []                              # список рёбер остова

# запускаем первый этап алгоритма
for r in Rs:
    if r[1] not in U or r[2] not in U:  # проверка на изолированность для исключения циклов в остове
        if r[1] not in U and r[2] not in U:  # если обе вершины изолированны
            D[r[1]] = [r[1], r[2]]           # формируем в словаре ключ с номерами вершин
            D[r[2]] = D[r[1]]                # связываем его со второй вершиной
        else:                           # иначе
            if not D.get(r[1]):              # если в словаре нет первой вершины
                D[r[2]].append(r[1])         # добавляем её в список группы вершин
                D[r[1]] = D[r[2]]            # связываем его с ключом первой вершины
            else:                       # иначе
                D[r[1]].append(r[2])         # делаем то же самое, но со второй вершиной
                D[r[2]] = D[r[1]]

        T.append(r)  # добавляем ребро в остов
        U.add(r[1])  # добавляем вершины в список соединённых вершин
        U.add(r[2])

# второй этап алгоритма
for r in Rs:
    if r[2] not in D[r[1]]:  # если вершины не принадлежат одной изолированной группе
        T.append(r)  # добавляем это ребро в остов
        temp = D[r[1]]
        D[r[1]] += D[r[2]]  # обьединяем списки двух групп вершин
        D[r[2]] += temp

print(T)


