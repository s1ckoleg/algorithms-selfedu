"""
Реализация очереди.
"""

import collections

q = collections.deque()  # при помощи этого объекта можно создавать эффективные стэки, дэки, очереди и прочие структуры
                         # со сложностью O(1) при добавлении или извлечении элементов
q.append(5)
q.append(3)
q.append(1)

print(q)
print(q.popleft())
print(q)
