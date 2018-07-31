import sys

print("參數長度={}".format(len(sys.argv)-1))
i=0
for arg in sys.argv:
    if i!=0:
        print("第{}個參數是：{}".format(i,arg))
    i+=1