def s1s2(n):
    s1=input('enter the string 1: ')
    s2=input('enter the string 2: ')
    s=s1+s2
    print('base string: ',s)
    sm=s.lower()*100
    sf=list(sm[:n])
    print('substring: ',sf)
    sd={}
    for i in sf:
        if i in sd:
            sd[i]+=1
        else:
            sd[i]=1        
    print(sd)
s1s2(10)    
    

