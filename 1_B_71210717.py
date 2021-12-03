n= int(input("Masukan banyak bilangan: "))

sum= 1
print('Total= ',end=' ')
for i in range(1,n+1):
   if i % 7 == 0:
      sum+= 0
      print ("+ 0", end=' ')
   elif i % 3 == 0:
      sum+=(i*-1)
      print('-',str(i), end=" ")
   elif i==1:
      print(str(i),  end=' ')
   else:
      sum+= i
      print('+',str(i), end=' ')

print("\nHasil perhitugan diatas ialah ",sum)



