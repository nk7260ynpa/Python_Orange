fp=open("zop.txt","r")
zops=fp.readlines()
fp.close()
i=1
print("Zen of Python")
for zen in zops:
    print("Zen {}:{}".format(i,zen),end="")
    i+=1