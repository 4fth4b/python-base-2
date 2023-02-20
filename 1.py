def q1():
    list1=[19,19,5,5,5,5,5]
    icount=0
    jcount=0
    for i in list1:
        if i==19:
            icount+=1
    for j in list1:
        if j==5:
            jcount+=1    
    if icount==2 and jcount>=3:
        print(True)
    else:
        print(False)            
q1()