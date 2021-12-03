n=input("Input: ")
m=len(n)
print('Output:')
for i in range(m):
    for j in range(m-i-1):
        print(' ',end='')
    for j in range(i+1):
       print(n[j],end='')
    print()
for i in range(1,m):
    for k in range(i):
        print(' ', end='')
    for k in range(m-i):
        print(n[k], end='')
    print()