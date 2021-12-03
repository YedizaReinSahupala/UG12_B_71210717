n= int(input('Input: '))
print('Output:')
for i in range(n):
    for j in range(n-i-1):
        print(' ',end='  ')
    for j in range(n):
        if j == 0 or i == (n-1) or i == j:
            print('*', end= '  ')
        else:
            print(end='   ')
    print()
