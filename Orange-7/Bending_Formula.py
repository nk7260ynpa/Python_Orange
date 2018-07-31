import os
Bending_Data=dict()
Flushed_Data=dict()
Duck_data=dict()
length=[Bending_Data,Flushed_Data,Duck_data]

#First Wall

Main_wall=float(input("Input the First Wall"))
Thickness=float(input("Input the Thickness"))


# Bending calculation
def Ben_cal ():
    b_num = int(input("輸入折邊數"))
    a=0

    for a in range(b_num):
        length[0][a] = float(input("Input the length"))
        print(length[0][a])

#Main menu
print("Bending:1")
print("Flushed:2")
print("Duck:3")

slect = int(input("Input your choice"))
if slect==1:
    Ben_cal()
elif slect==2:
    Flu_cal()
elif slect==3:
    Duck_cal()







