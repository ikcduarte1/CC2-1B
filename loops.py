for i in range(5):
    for j in range(1, i + 2):
        print(j, end = " ")
    print()


for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()


number = int(input("input: "))
sum = 0
for i in range(number + 1):
    sum += i
print(sum)
