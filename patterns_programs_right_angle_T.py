# right-angled triangle
for i in range(1, 9):
    for j in range(1, i + 1):
        print(' * ', end='')
    print()

print()

for i in range(1, 9):
    for j in range(1, 9 - i + 1):
        print(' * ', end='')
    print()


print()
k = 0
for i in range(1, 5):
    for j in range(1, 5 - i + 1):
        print(k, ' ', end='')
        k = k+1
    print()
