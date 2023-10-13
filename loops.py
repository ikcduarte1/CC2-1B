#NUMBER 1
for i in range(5):
    for j in range(1, i + 2):
        print(j, end = " ")
    print()
    print()

#NUMBER 2
n = int(input("input: "))
sum = 0
for i in range(1, n + 1):
    if i == n:
        print(i, end=" = ")
    else:
        print(i, end=" + ")
    sum += i
print(sum)

#NUMBER 3
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()
    print()


