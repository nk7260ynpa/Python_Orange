import os, sys
try:
    os.remove("hello.txt")
except Exception as e:
    print(e)

    e_type,e_value,e_tb=sys.exc_info()
    print("種類：{}\n訊息：{}\n資訊：{}".format(e_type,e_value,e_tb))
