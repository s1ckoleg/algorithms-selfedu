"""
Реализация стека типа LIFO (Last-In-First-Out). Пример его использования для проверок записи скобок в строке.
https://www.youtube.com/watch?v=2NM802a6A00&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=14
"""

a = input("Введите пример: ")
stack = []
flVerify = True  # флаг для определения итогов проверки

for lt in a:
    if lt in "([{":
        stack.append(lt)
    elif lt in ")]}":
        if len(stack) == 0:
            flVerify = False
            break

        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        flVerify = False
        break

if flVerify and len(stack) == 0:
    print('Correct')
else:
    print('Incorrect')
