def sweet():
    n=int(input('Enter the number of sweet packets: '))
    a=[]
    print('Enter the no of sweets respectively')
    for i in range(0,n):
        b=input('')
        a.append(b)
    print(a)
    m=[]
    k=[]
    for i in range(0,n):
        for j in range(i,n):
            if a[i] > a[j]:
                m.append(i+1)
                k.append(j+1)
                c=a[i]
                a[i]=a[j]
                a[j]=c
    s=m+k
    print(s)
    print(a)       
sweet()


