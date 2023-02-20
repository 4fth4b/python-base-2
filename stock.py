def Arraychallenge(l):
    list1=[]
    for i in l:
        list1.append(i)  
    a=[]
    f=[]
    g=[]
    x=len(list1)
    for i in range(0,x):
        for j in range(i,x):
            b=list1[i]-list1[j]
            a.append(b)  
            if(list1[i]-list1[j]==min(a)):
                f.append(list1[i])
                g.append(list1[j])
    print(f[-1],g[-1])
    c=min(a)

    print('The max profit is: ',-c)    
l=[44,30,24,32,35,30,40,38,15]
Arraychallenge(l)

