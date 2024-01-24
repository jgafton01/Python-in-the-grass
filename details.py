"""
Create a program that uses input() to get the below information from the user

Name
Age
House Number 
Street Name 

then print the information in a sentence 

"""
# Acquire users details using input()
users_name = input("Enter your name: ")
users_age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")

# Print user details in a sentence using f string to embed variables  

print(f"This is {users_name}. They are {users_age} years old and live at {house_number} {street_name}.")