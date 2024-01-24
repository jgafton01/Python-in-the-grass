"""
Create a program with the following requirements:

save the sentence "The!quick!brown!fox!jumps!over!the!lazy!dog."

using replace functino to replace() function to replace every ! exclamation mark with a blank space. 

then reprint the sentence as "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG" using the upper() function

then reprint the sentence in reverse

"""
#declare the string as a variable
string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#declare a 2nd variable to store string and replace "!" with " "
modified_string = string.replace("!"," ")

#use the modified string and convert to upper case using upper()
modified_string = modified_string.upper()

#print the uppercase variable 
print(modified_string)

#print the uppercase variable in reverse using slicing [::-1]
#-1 prints the string from the end and moves backwards with a step of -1
print(modified_string [::-1])

