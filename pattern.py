"""Write code to output the star pattern shown below, using an if-else
statement in combination with a single for loop (it’s really easy with two,
but using only one takes a little more thought!):
*
**
***
****
*****
****
***
**
*
"""
#declare variable
rows = 5

# Loop to iterate over the range of values from 1 to (rows * 2)
for i in range(1, rows * 2):
    # Check if the current value of i is less than or equal to row
    if i <= rows:
         # If the current value of i is greater than rows
        print('*' * i)
         # Print '*' repeated times
    else:
        print('*' * (rows * 2 - i))