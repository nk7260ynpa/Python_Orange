age=int(input("age="))

if age>=20:
    print("請記得今年要去投票")
else:
    diff=20-age
    print("你還差{}歲才能投票".format(diff))