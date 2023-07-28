'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница...'''

x, y = int(input()), int(input())
print(sorted([(i, k if x == i + k and y == i * k else -1) for i in range(1, y + 1) for k in range(1, x + 1)],key= lambda x: x[-1] != -1)[-1])#в одну не получилось, ток в две:)

'''обычное решение'''

x, y = int(input()), int(input())
for i in range(x):
    if len(a := [(i, k) for k in range(y) if x == i + k and y == i * k]) != 0:
        print(*a)
        break