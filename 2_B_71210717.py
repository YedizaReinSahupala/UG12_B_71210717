counter=0
list_n= []
list_j= []
check= 0
while True:
    n= input("Masukan nama: ")
    if n == 'STOP':
        no ='STOP'
        break
    else:
        j = int(input("Masukan nomor kursi "+ n + ": " ))
        if (len(list_j) ==0):
            list_n.insert(counter, n)
            list_j.insert(counter, j)
            counter+=1
        else:
            for i in range(len(list_j)):
                if list_j[i] == j:
                    check= 0
                    break
                else:
                    check=1
            if check == 1:
                list_n.insert(counter, n)
                list_j.insert(counter, j)
                counter += 1
            else:
                print("Mohon maaf kursi tersebut telah terisi.")
print()

print("List kursi yang telah terisi: ")
for i in range(counter):
    print("Kursi nomor ", list_j[i], "telah diisi oleh ", list_n [i])