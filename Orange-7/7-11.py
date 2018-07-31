while True:
    try:
        age=int(input("What's your age?"))
        break
    except:
        print("Please enter a number.")
if age<15:
    print("You are too young.")
else:
    print("Don't forget go to vote.")
