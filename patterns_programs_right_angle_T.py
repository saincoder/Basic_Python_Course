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
