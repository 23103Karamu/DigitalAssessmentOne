## Variables
Student_name = None
Student_age = None
Min_age = 5
Max_age = 17
Transport_cost = 80
Camp_number = None
Camp_chosen = None
Meal_number = None
Meal_chosen = None
Shuttle_y_n = None
Shuttle_taken = None
Going_to_camp = None
GTG_y_n = None
Student_details = []
Camp_leader_y_n = None
Camp_leader = ""
Camp_leader_eligibility = False

## The details of the students
while Student_name is None: ## The code to get the student's name is put into a loop so if no name is given the code will repeat
    Student_name = input("What is the student's name? ")
    if Student_name == "":
        print("Please input the student's name. ")
        Student_name = None
    else:
        Student_details.append(Student_name)
        break

while Student_age is None: ## The code is put into a loop so if no age is given or a string is given, the code will repeat
    try:
        Student_age = int(input("What is the student's age? "))
    except ValueError: ## if a number isn't inputted, this code will play which will tell them to input a number
        print("Please input a number. ")
        continue
    if Student_age <= 0 or Student_age >= 100: ## if their age is below 0 or over 100, this code will play which will make them have to input a proper age
        print("Are you sure that is the student's age? ")
        Student_age = None
        continue
    else:
        Student_details.append(Student_age)
        print("\n") ## This is here to split it up into sections
        if Student_age >= 15:
            Camp_leader_eligibility = True
        break

if Student_age < Min_age or Student_age > Max_age: ## This is to test if the student is too young or too old to do the activities
    print("Sorry, but the student is not eligible due to their age. ")
    Student_eligibility = False
    Student_details.append(Student_eligibility)
else: ##if they aren't too old or too young, their eligibility is true
    Student_eligibility = True
    Student_details.append(Student_eligibility)

while Camp_leader_eligibility == True and Student_eligibility == True: ## Camp leader offered
    Camp_leader_y_n = input("Would the student like the chance to be camp leader? (yes/no) ")
    if Camp_leader_y_n == "y" or Camp_leader_y_n == "yes":
        print("The student will have the chance to be camp leader.") ## This prints so they know that the program isn't broken in case they have that fear
        Camp_leader = "The student might be chosen as the camp leader." 
        print("\n")
        Student_details.append(Camp_leader)
        break
    elif Camp_leader_y_n == "n" or Camp_leader_y_n == "no":
        print("The student will not have the chance to be camp leader.")
        Camp_leader = ""
        Student_details.append(Camp_leader)
        print("\n")
        break
    else:
        print("This is a yes or no question")
        continue
## Choosing the camp
Camps = ["Cultural immersion, 5 days, easy, $800","Kayaking and Pancakes, 5 days, moderate, $400","Mountain biking, 4 days, difficult, $900"]

while Student_eligibility == True: ## if the student is eligible, they will see the camps availible
    for i, item in enumerate(Camps, start = 1):
        print(i, item)
    break ## the code will break instead of looping after all the choices are finished printing

while Camp_chosen is None and Student_eligibility == True: ## This code is in place so if the student isn't eligible, the code won't run and therefore won't waste resources and if they haven't chosen a camp, it will run
    try:
        Camp_number = int(input("Choose a camp number you want to go to: "))
    except ValueError: ## If they don't input a number, it will run this code
        print("Please input a number")
        continue
    if Camp_number < 1 or Camp_number > 3: ## If they do a number that isn't there, the code will detect it, set the camp chosen to none, and continue running the loop
        print("Invalid camp choice, please try again")
        continue
    else: ## if the number is valid and isn't an error, this code will run which will set the camp chosen and break
        if Camp_number == 1:
            Cost = 800
            Camp_chosen = Camps[Camp_number-1] ## This sets the Camp chosen to be from the list of camps
            Camp_chosen = Camp_chosen.replace(" $800", "") ## This removes the cost from it so I can add it in later
        elif Camp_number == 2:
            Cost = 400
            Camp_chosen = Camps[Camp_number-1]
            Camp_chosen = Camp_chosen.replace(" $400", "")
        elif Camp_number == 3:
            Cost = 900
            Camp_chosen = Camps[Camp_number-1]
            Camp_chosen = Camp_chosen.replace(" $900", "")
        Student_details.append(Camp_chosen) ## This adds the camp chosen to the student details list
        print("\n") ## This clears it up and splits it off into sections
        break

## Choosing a meal
Meals = ["Standard", "Vegetarian", "Vegan", "Gluten free"] ## This is the meal options which will be printed out
while Student_eligibility == True: ## This code is here so if the student is eligible, they will get to see the meal options
    for i, item in enumerate(Meals, start = 1):
        print(i, item)
    break ## when it finishes printing the 3 choices, it will break instead of looping

while Meal_chosen is None and Student_eligibility == True: ## This code is here so if they are eligible and haven't chosen a meal, this code will play
    try:
        Meal_number = int(input("Choose a meal number that you want: ")) ## When you respond, the meal_number will be set to that number and checked if availible
    except ValueError: ## if a string or non-number entered, it will be reset and asked for a proper number to be inputted
        print("Please input a number") 
        continue
    if Meal_number < 1 or Meal_number > 4: ## If the meal number is not there, it will go back to the int(input)
        print("Invalid meal choice, please try again")
    else: ## if the response is valid, this else statement will play and set the meal_chosen to the meal in Meals
        Meal_chosen = Meals[Meal_number-1]
        print("\n")
        Student_details.append(Meal_chosen)
        break

## If taking the shuttle bus
while Shuttle_taken is None and Student_eligibility == True: ## If they are eligible and haven't chosen if they want to take the shuttle bus yet, this will run
    Shuttle_y_n = input("Do you want to take the shuttle bus? it is an extra $80: ").lower() ## This has a .lower() as if you do it at the input, instead of question, you don't need to run it at the question which saves time
    if Shuttle_y_n == "y" or Shuttle_y_n == "yes":
        Cost = Cost + Transport_cost ## This chanegs the cost to be the previous cost plus 80
        Shuttle_taken = "shuttle bus will be taken" ## This lets them know that the shuttle bus definitely will be taken
        Student_details.append(Cost) ## This adds the cost to student details
        Student_details.append(Shuttle_taken) ## This adds if they will be taking the bus to student details
        print("\n")
        break
    elif Shuttle_y_n == "n" or Shuttle_y_n == "no":
        Shuttle_taken = "shuttle bus will not be taken"
        Student_details.append(Cost)
        Student_details.append(Shuttle_taken)
        print("\n")
        break
    else:
        print("This is a yes or no question") ## If they don't do n, no, y, yes this will play
        continue

## If they will be going
if Student_eligibility == True: ## if they student is eligible and after answering every question, this will play telling them what has been chosen
    print(f"{Student_name}, {Student_age}, {Camp_chosen} the student's meal is {Meal_chosen}, the {Shuttle_taken}, the cost will be ${Cost}. {Camp_leader}") ## This is done as a print statement so when they are asked if the student will be going, this won't repeat, only the question

while Going_to_camp is None and Student_eligibility == True:
    GTG_y_n = input("Will the student be going (yes or no)? ").lower() ## As I said before, this is the question which will repeat if they don't answer with y, yes, n, or no
    if GTG_y_n == "y" or GTG_y_n == "yes":
        print("The student will be attending the camp.") ## This prints so they know that the program isn't broken in case they have that fear
        Going_to_camp = True
        Student_details.append(Going_to_camp)
    elif GTG_y_n == "n" or GTG_y_n == "no":
        print("The student will not be attending the camp.")
        Going_to_camp = False
        Student_details.append(Going_to_camp)
    else:
        print("This is a yes or no question")