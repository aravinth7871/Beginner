y=int(input())
if(y>1):
    for i in range(2,y):
        if(y%i) == 0:
            print("no")
            break
            
    else:
            print("yes")
