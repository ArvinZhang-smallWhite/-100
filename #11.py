for i in reversed(range(1,6)):
    if(i==5 or i==1):
        print("* "*i)
    else:
        print("*"+" "*pow(2,i-2)+"*")
