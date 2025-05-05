## Variables
Student_name = None
Student_age = None
Min_age = 5
Max_age = 17
Transport_cost = 80
Camp_number = None
Camp_chosen = None

## The details of the students
while Student_name is None: ## The code to get the student's name is put into a loop so if no name is given the code will repeat
    Student_name = input("What is the student's name? ")
    if Student_name == "":
        print("Please input the student's name. ")
        Student_name = None
    else:
        break

while Student_age is None: ## The code is put into a loop so if no age is given or a string is given, the code will repeat
    try:
        Student_age = int(input("What is the student's age? "))
    except ValueError:
        print("Please input a number. ")
        continue
    if Student_age <= 0 or Student_age >= 100:
        print("Are you sure that is the student's age? ")
        Student_age = None
        continue
    else:
        print("\n") ## This is here to split it up into sections
        break

if Student_age < Min_age or Student_age > Max_age: ## This is to test if the student is too young or too old to do the activities
    print("Sorry, but the student is not eligible due to their age. ")
    Student_eligibility = False
else:
    Student_eligibility = True

## Choosing the camp
Camps = ["Cultural immersion, 5 days, easy, $800","Kayaking and Pancakes, 5 days, moderate, $400","Mountain biking, 4 days, difficult, $900"]

while Student_eligibility == True:
    for i, item in enumerate(Camps):
        print(i, item)
    break

while Camp_number == None and Student_eligibility = True:
    try:
        Camp_number = int(input("Which number camp do you want to go to? "))
    except ValueError:
        print("Please input a number")
        continue
    if Camp_number < 0 or Camp_number > 3:
        print("Invalid camp choice, please try again")
        Camp_chosen = None
        continue
    else:
        Camp_chosen = Camps[Camp_number]
        print("\n")
        break
print(Camp_chosen)