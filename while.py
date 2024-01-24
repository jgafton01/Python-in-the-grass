"""
write a program using a while loop that continually asks the user to enter a number

when a user enters "-1" the program should stop requesting the user t enter a number

The program must then calculate the average of the numbers entered excluding the 1 

"""
#declare a variable to store the total and count 
total = 0 
count = 0

#get user input and cast into integer 
user_input = int(input("please enter a number(-1 to exit: )"))

#create loop where input is not equal to -1 
while user_input != -1: 
    #Increment the count and add the user input to the total 
    count += 1
    #the total store the total  
    total += user_input
    #if condition is met we ask for input again
    user_input = int(input("please enter a number(-1 to exit: )"))
    #print the total once user exits


#print the total and count once the user exits
print(f"\nTotal:{total}")
print(f"Count:{count}")

# Check if there are valid numbers entered before calculating the average
if count > 0:
    # Calculate and display the average
    average = total / count
    print(f"Average: {average}")
else:
    print("No valid numbers entered.")

