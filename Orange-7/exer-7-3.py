import os
class_101=dict() #record the number and name of students
chi_score=dict() #record the score of Chinese subject
eng_score=dict() #record the score of English subject
mat_score=dict() #record the score of math subject
subjects=["Chinese","English","Math"]
scores=[chi_score,eng_score,mat_score]

def disp_menu():
    os.system("clear")
    print("Class 101 score management")
    print("----------------------------")
    print("1.input name")
    print("2.input Chinese score")
    print("3.input English score")
    print("4.input math score")
    print("5.display the transcript")
    print("0.exit the program")
    print("----------------------------")

def enter_std_data():
    while True:
        no= int(input("number(0==>Stop):"))
        if no<=0 or no>100: break
        name=input("name")
        class_101[no]=name
        print(class_101)

def enter_score(subject_no):
    for no,name in class_101.items():
        scores[subject_no][no]=int(input("{},{},{}score:".format(no,name,subjects[subject_no])))
        print(scores[subject_no])
        x=input("Press Enter to main menu")

def disp_score_table():
    for no in class_101.keys():
        print("{:<5}:".format(class_101[no]),end="")
        sum=0
        for subject_no in range(0,3):
            sum=sum+scores[subject_no][no]
            print("{}:{:>}".format(subjects[subject_no],\
                                scores[subject_no][no]),end="")
        print("Sum:{:>3},Average:{:.2f}".format(sum,float(sum)/len(scores)))
    x=input("Press Enter to main menu")


#main program start here

while True:
    disp_menu()
    user_choice=int(input("Please Enter your Selection"))
    if user_choice==1:
        enter_std_data()
    elif user_choice>=2 and user_choice<=4:
        enter_score(user_choice-2)
    elif user_choice==5:
        disp_score_table()
    else:
        break
print("Thanks for your use")
