"""
Алгоритм быстрой сортировки Хоара
Сложность: O(N*log(N))
https://www.youtube.com/watch?v=HjVE1ei28_I&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=13
"""

import random


def quick_sort(a):
    if len(a) > 1:
        x = a[random.randint(0, len(a) - 1)]  # случайное пороговое значения для разделения на малые и большие

        low = [u for u in a if u < x]   # список значений, которые меньше случайного порогового
        eq = [u for u in a if u == x]   # список значений, которые равны случайному пороговому
        high = [u for u in a if u > x]  # список значений, которые больше случайного порогового
        a = quick_sort(low) + eq + quick_sort(high)

    return a


a = [9, 5, -3, 4, 7, 8, -8]
sorted_a = quick_sort(a)

print(sorted_a)


