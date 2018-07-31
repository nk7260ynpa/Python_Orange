stock={"book":10,"pen":3,"eraser":6,"ruler":2}

for key,value in stock.items():
    if value<5:
        print("({},{})".format(key,value))