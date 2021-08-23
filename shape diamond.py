
def shape(y,h):
    v=" "
    xx=20
    ss=20
    for b in range(20):
        a = b * y + h
        di =  xx * v + h + b * y+a 
        print(di)
        xx = xx-1
    for z in range(21):
        aa = ss * y + h
        di2 = z * v + h + ss * y + aa
        print(di2)
        ss=ss-1
    return "Thanks"    
x = input("inter any shape you want: ") 
y=  input("inter any shape you want: ")     
print(shape(x,y))