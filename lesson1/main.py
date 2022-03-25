# 1 задача
a = int(input())
b = int(input())

if a > b:
    print(f"Наименьшее число: {b}")
elif a < b:
    print(f"Наименьшее число: {a}")
elif a == b:
    print("Числа равны")


# 2 задача
a = int(input())
b = int(input())
c = int(input())

if a > b and c > b:
    print(f"Наименьшее число: {b}")
elif a < b and a < c:
    print(f"Наименьшее число: {a}")
elif c < b and a > c:
    print(f"Наименьшее число: {c}")
elif a == b == c:
    print("Числа равны")


# 3 задача
a = input()
b = input()
c = input()

if a == b == c:
    print("3")
elif a == b or a == c or b == c:
    print("2")
elif c < b and a > c:
    print(f"Наименьшее число: {c}")
else:
    print("0")


# 4 задача
a = int(input())
b = int(input())

i = 0
for _ in range(a, b):
    i += _

print(i)