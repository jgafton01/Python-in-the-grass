"""
Create program using if statements to output responses using the following conditions:

less than 13 output "You qualify for the kiddie discount"x
13-21 + 21-40 "Age is but a number."
21 "Congrats on your 21st!" x
40 or over "you're over the hill"x
65-100 "Enjoy your retirement!"
100 = "sorry you're dead" x

the order of the statements matters as it checks the user input against the condition i.e if age is 100 and 2nd statement is >= than 40 than it will print this condition

"""
#Declare the age as a variable and get input from user to build if statement 
age = int(input("What is your age? "))

#if statements control structure that prints out the appropriate response based on age  
if age > 100:
    print("Sorry you're dead")
elif age >= 65: 
    print("Enjoy your retirement")
elif age >= 40: 
    print("you're over the hill")
elif age < 13:
    print("You qualify for the kiddie discount") 
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number")



