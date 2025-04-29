## The details of the students
Student_name = None
Student_age = None
Student_eligibility = True
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
        break

if Student_age < 5 or Student_age > 17:
    print("Sorry, but the student is not eligible due to their age. ")
    Student_eligibility = False