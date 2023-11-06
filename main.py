#Original code
# age = input("What is your age?: ")

# if int(age) < 18:
#   print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
#   print("Powering On. Enjoy the ride!");
# elif int(age) == 18:
#   print("Congratulations on your first year of driving. Enjoy the ride!")


#Task 1: 
#Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 

def checkDriverAge():
  age = input("What is your age?: ")
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()

#Task 2: 
#Call the function with different ages to test that it works.
checkDriverAge()
checkDriverAge()
checkDriverAge()

#Task 3:
#Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.
#Hint: Remember that you can pass arguments to functions just like you do with variables.

def checkDriverAge(age=0):
  age = input("What is your age?: ")
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()


#If we put the code with 'age = input("What is your age?: ")' outside the function & call as many times as we want, it will repeat its output
age = input("What is your age?: ")

def checkDriverAge():
  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge() #calling 3 times back to back
checkDriverAge()
checkDriverAge()