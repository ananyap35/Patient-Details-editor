
print("Welcome to your patient portal! Here you can create a profile to be used for our hospital records")
ready = input("Are you ready to proceed? ")
#the variable "ready" takes in user input, and is later used in the parameter "decision" for the procedure "enterdata"

def enterdata(decision):
  dataname = ["First Name", "Last Name", "Gender","Age" ,"Weight in Pounds (lb)", "Height in Inches (in)", "blood type"]
#This is the list that will serve as a name for each of the details that user will input
#The below selection statements determine the control flow of the code depending on the user input for the variable "ready" that passes through parameter "decision"
  if decision == "Yes" or decision == "yes":
    phpp = []
    for i in range(len(dataname)):
      detail = input("Please Input Your " + dataname[i] + ". ") 
      phpp.insert(i, detail)
#this is a new list "phpp" stores the user input
#for statement is used to iterate through "dataname" list which stores the names of each input.
#The indices of dataname corresponds with the list "phpp", which stores the inputs of the user.
    print("\nYour Patient Portal : \n")
    
    for a in range(len(phpp)):
      print(dataname[a] + ": " + phpp[a])  
#This for statement creates the structure for the patient portal, matching each index of dataname's input's name from list "dataname" with the corresponding input from list "phpp"

#bmi is calculated based on the user input
#Selection statement determines the value of "status" or the interpreration of the bmi in relation to weight and health
    
    bmi = (((float(phpp[4]))*703)/((float(phpp[5]))**2))
    if bmi > 18.5 and bmi < 24.9:
      status = "HEALTHY"
    elif bmi < 18.5:
      status = "UNDERWEIGHT"
    elif bmi > 24.9 and bmi < 30.0:
      status = "OVERWEIGHT"
    elif bmi > 30.0:
      status = "OBESE"
    else:
      print("Please re-evaluate your inputs \n re-enter data if necessary")

    print("Body Mass Index" + ": " + str(round(bmi,2)) + " " + status)

#Calculates basic metabolic rate "bmr" and ideal body weight "ibw" based on user's stored input in list "phpp"
#Selection statement determines the control flow for the appropriate method of calculating the bmr and ibw based on gender
    
    if phpp[2] == "Male" or phpp[3] == "male" or phpp == "m" or phpp == "M":
      bmr = ((4.536 * float(phpp[4])) + (15.88 * float((phpp[5]))) - (5 * float(phpp[3])) + 5)
      ibw = (110.23 + (5.1*((float(phpp[5]))-60)))
    elif phpp[2] == "Female" or phpp[2] == "female" or phpp[2] == "F" or phpp[2] == "f":
      bmr = ((4.536 * float(phpp[4])) + (15.88 * float((phpp[5]))) - ((5 * float(phpp[3])) -161))
      ibw = (100.3 + (5.1 * ((float(phpp[5]))-60)))
    else:
      print("Error, please re-enter data and reconfirm inputs \n refresh the page if necessary")
    print("Basic Metabolic Rate" + ": " + str(round(bmr,2)) + " \n" + "Ideal Body Weight" + ": " + str(round(ibw,2)))

#Based on the value of ibw, the code outputs a statement if the user has an ibw that is in an undesirable range
    if float(phpp[4]) < (ibw-23.3) or float(phpp[4]) > (ibw + 23.3):
      print("Please re-evaluate weight and nutrition plan")

    
  else:
#The control flow where the user input's "No" at the start of the program for variable "ready". 
#Selection statements re-confirm whether the user wants to input details or not
    
    xcheck = input("Are you sure? ")
    if xcheck != ready:
      print("Please exit the site")
    else:
      print("Please refresh the code to start again")


      


      

      
#if statement used to check if the user enters passable values for the procedure
#Control flow determines is the procedure is called or not


#if statement used to check if the user enters passable values for the procedure
#Control flow determines is the procedure is called or not

if ready == "Yes" or  ready == "yes" or ready == "No" or ready == "no":
  enterdata(ready)
else:
  while ready != "Yes" or ready != "yes" or ready != "No" or ready != "no":
    ready = input("Please input either yes or no ")
    if ready == "Yes" or  ready == "yes" or ready == "No" or ready == "no":
      break
  enterdata(ready)


