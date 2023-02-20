def fabinocci(a):
    f1=0
    f2=1
    print('the fabinocci series is:')
    for i in range(0,a):
        print(f1)
        c=f1+f2
        f1=f2
        f2=c
fabinocci(4)    
# a=int(input('Enter the number'))


    


