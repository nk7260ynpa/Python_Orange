import random
a=int(input("Enter a number"))
b=float(a)
no1=float(0)
no2=float(0)
no3=float(0)
no4=float(0)
no5=float(0)
no6=float(0)
for i in range(0,a,1):
    x=random.randint(1,6)
    print(" ",x,end="")
    if x==1:
        no1=no1+1
    elif x==2:
        no2=no2+1
    elif x==3:
        no3=no3+1
    elif x==4:
        no4=no4+1
    elif x==5:
        no5=no5+1
    else:
        no6=no6+1
print("")
print(no1/b)
print(no2/b)
print(no3/b)
print(no4/b)
print(no5/b)
print(no6/b)

print("","\n",no1,"\n",no2,"\n",no3)

