def MarkTim(num):
    n=str(num)
    prime=[2,3,5,7]
    l=len(n)
    print(n)

    
    for i in range(0,l):
        if i%2==0 and n[i]%2==0:
            if i%2!=0 and n[i] in prime:
                print(True)
            else:
                print(False)
        else:
            print(False)            
MarkTim(2342)
