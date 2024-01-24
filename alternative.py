
#read in string 
main_string = "Hello World it is me"

#store updated string
store_string = ""

#for loop to change change alternate letters to upper/ lower 
for i in range(len(main_string)):
    if i % 2 == 0:
        store_string += main_string[i].upper()
    else:
        store_string += main_string[i].lower()
#print result
print (store_string)

store_string = ""
split_string = main_string.split()

#check if i is even 
for i in range(len(split_string)):
    #add lowercase/uppercased version of split_string to store_string 
    #add a space to store string 
    store_string += (split_string[i].lower() if i % 2 == 0 else split_string[i].upper()) + " "
#remove trailing space from store_string
output_string = store_string.rstrip()
#output result 
print(output_string)



