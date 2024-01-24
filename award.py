"""Create a new Python file in this folder called award.py.
● Design a program that determines the award a person competing in a
triathlon will receive.

● Your program should read in the times (in minutes) for all three events of a
triathlon, namely swimming, cycling, and running, and then calculate and
display the total time taken to complete the triathlon.

● The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes.
Display the award that the participant will receive based on the following
criteria"""

# provincial_colours = 0 - 100 
# Provincial_Half_colours = 101 - 105 
# Provincial_Scroll = 106 - 110 
# No_Award = 111

#get user input for swimming, cycling and running
swimming = int(input("What was your time to complete swimming: "))
cycling = int(input("What was your time to complete cycling: "))
running = int(input("What was your time to complete running: "))

#declare variable to store total time
total_time = swimming + running + cycling

#show total time to user 
print(f"your total time to complete the triathlon was:{total_time} mins")

#check if total time matches award conditions
if total_time <= 100:
    print("Congratulations you are within qualifying time and receive the Provincial Colours")
elif (total_time >= 101) and (total_time <= 105): 
    print("Congratulations you are within 5 mins of the qualifying time and receive the Provincial Half Colours award!") 
elif (total_time >= 106 ) and (total_time <= 110):
    print("Congratulations you are within 10mins of the qualifying time and receive the Provincial Scroll award!")
else:
    print("Sorry you are more than 10 minutes off of the qualifying time you don't receive a reward") 

