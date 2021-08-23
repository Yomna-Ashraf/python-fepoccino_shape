x=[]
for i in range(0,10):
    if i <=1:
        x.append(i)
    else:
        a=x[-1]
        y=x[-2]
        x.append(a+y)
    print(x)    
