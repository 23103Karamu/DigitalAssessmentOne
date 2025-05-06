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
    except ValueError: ## if a number isn't inputted, this code will play which will tell them to input a number
        print("Please input a number. ")
        continue
    if Student_age <= 0 or Student_age >= 100: ## if their age is below 0 or over 100, this code will play which will make them have to input a proper age
        print("Are you sure that is the student's age? ")
        Student_age = None
        continue
    else:
        print("\n") ## This is here to split it up into sections
        break

if Student_age < Min_age or Student_age > Max_age: ## This is to test if the student is too young or too old to do the activities
    print("Sorry, but the student is not eligible due to their age. ")
    Student_eligibility = False
else: ##if they aren't too old or too young, their eligibility is true
    Student_eligibility = True

## Choosing the camp
Camps = ["Cultural immersion, 5 days, easy, $800","Kayaking and Pancakes, 5 days, moderate, $400","Mountain biking, 4 days, difficult, $900"]

while Student_eligibility == True: ## if the student is eligible, they will see the camps availible
    for i, item in enumerate(Camps):
        print(i, item)
    break ## the code will break instead of looping after all the choices are finished printing

while Camp_chosen == None and Student_eligibility == True: ## This code is in place so if the student isn't eligible, the code won't run and therefore won't waste resources and if they haven't chosen a camp, it will run
    try:
        Camp_number = int(input("Choose a camp number do you want to go to "))
    except ValueError: ## If they don't input a number, it will run this code
        print("Please input a number")
        continue
    if Camp_number < 0 or Camp_number > 2: ## If they do a number that isn't there, the code will detect it, set the camp chosen to none, and continue running the loop
        print("Invalid camp choice, please try again")
        continue
    else: ## if the number is valid and isn't an error, this code will run which will set the camp chosen and break
        if Camp_number == 0:
            Cost = 800
        elif Camp_number == 1:
            Cost = 400
        elif Camp_number == 2:
            Cost = 900
        Camp_chosen = Camps[Camp_number]
        print("\n")
        break

## Choosing a meal
Meals = ["Standard", "Vegetarian", "Vegan"] ## This is the meal options which will be printed out
while Student_eligibility == True: ## This code is here so if the student is eligible, they will get to see the meal options
    for i, item in enumerate(Meals):
        print(i, item)
    break ## when it finishes printing the 3 choices, it will break instead of looping

while Meal_chosen == None and Student_eligibility == True: ## This code is here so if they are eligible and haven't chosen a meal, this code will play
    try:
        Meal_number = int(input("Choose a meal number that you want ")) ## When you respond, the meal_number will be set to that number and checked if availible
    except ValueError: ## if a string or non-number entered, it will be reset and asked for a proper number to be inputted
        print("Please input a number") 
        continue
    if Meal_number < 0 or Meal_number > 2: ## If the meal number is not there, it will go back to the int(input)
        print("Invalid meal choice, please try again")
    else: ## if the response is valid, this else statement will play and set the meal_chosen to the meal in Meals
        Meal_chosen = Meals[Meal_number]
        print("\n")
        break

print(Camp_chosen.replace("$800", f"${Cost}")) ## This is code to test the replace feature and so I remember it as well