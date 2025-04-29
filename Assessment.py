## The details of the students
Student_name = None
Student_age = None
while Student_name == None: ## The code to get the student's name is put into a loop so if no name is given the code will repeat
    Student_name = input("What is the student's name? ")
    if Student_name == "":
        print("Please input the student's name. ")
        Student_name = None
    else:
        break
while Student_age == None: ## The code is put into a loop so if no age is given or a string is given, the code will repeat
    try:
        int(input("What is the student's age? "))
    except ValueError:
        print("Please input a number. ")
        Student_age = None
    else:
        break