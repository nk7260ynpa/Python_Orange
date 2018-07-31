import random
for i in range(0,10,1):
    x=random.randint(1,6)
    if x == 1 or x==6:
        continue
    print(x)

