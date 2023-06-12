"""Дз №1"""

list_1 = range(50)
print(min(list_1), max(list_1))
print("\n")
for a in list_1:
    if a % 3 == 0:
        if a % 5 != 0:
             print(a)

print("\n")

"""ДЗ № 2"""

list_2 = [1, 2, 1, 2, 3, 4, 5, 4, 5]
for b in list_2:
    count = list_2.count(b)
    if count < 2:
        print(b)

