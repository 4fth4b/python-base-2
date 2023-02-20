n=int(input('Enter the number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        a=j*i
        print(a,end=" ")     
    print()