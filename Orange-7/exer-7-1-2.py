import random
a=int(input("Enter a number"))
b=float(a)
c=[0,0,0,0,0,0]
for i in range(0,a,1):
    x=random.randint(1,6)
    print(" ",x,end="")
    if x==1:
        c[0]+=1
    elif x==2:
        c[1]+=1
    elif x==3:
        c[2]+=1
    elif x==4:
        c[3]+=1
    elif x==5:
        c[4]+=1
    else:
        c[5]+=1
print("")
print(float(c[0]/b))
print(float(c[1]/b))
print(float(c[2]/b))
print(float(c[3]/b))
print(float(c[4]/b))
print(float(c[5]/b))



