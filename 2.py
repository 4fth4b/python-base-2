def q2():
    a=list(input('Enter the numbers: ').split())
    d=[]
    for i in a:
        d.append(int(i))    
    b=len(d)
    c=d[4]
    count=0
    print('The length of the string: ',b)
    print('The fifth element: ',c)
    for i in d:
        if i==c:
            count+=1
    print('no of 5th element in the list: ',count)
    if b==8 and count==3:
        print(True)
q2()
            