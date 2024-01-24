import math


#Get user input for bond/investment 

user_input = (input("Please type whether you would like investment or bond: "))

#casting user input to uppercase 
user_input = user_input.upper()

#declare interest variable
interest_amount = 0

#Check if user input is investment
if (user_input == "INVESTMENT"):

    #Get user input for deposit
    deposit = float(input("How much money are you depositing: ")) 

    #Get user input for interest rate
    interest_rate = float(input("What is the interest rate: "))

    #Get user input for  years investing
    years_investing = float(input("How many years will you invest for:"))

    #Get user input for interest
    interest = input("Would you like compound or simple interest?: ")
    
    #cast variable into uppercase 
    interest = interest.upper()
    
    #Check user input is investment
    if (user_input == "INVESTMENT"):
        #check if interest is simple
        if (interest == "SIMPLE"):
             #formula for calculating interest
             total_amount = deposit *(1 + interest_rate/100*years_investing)
             #print total amount result to user 
             print(f"your total amount is: {total_amount}")
             #check if interest is compound
        elif (interest == "COMPOUND"):
             #formula for calculating interest
             interest_amount = deposit *(math.pow((1+interest_rate/100),years_investing))
             print(interest_amount)
#Check if user input is bond
elif (user_input == "BOND"):
        
        #Get user input for house value, interest rate, repay months
        house_value = float(input("What is the present value of the house: "))
        interest_rate = float(input("What is the interest rate: "))
        repay_months = float(input("How many months do you plan to take to repay the bond: "))
        interest_rate = (interest_rate / 100) / 12

        #formula for calculating interest rate 
        repayment = (interest_rate * house_value)/(1 - (1 + interest_rate)**(-repay_months))
        print(f"You will have to repay: {repayment}")

#prompt user to enter correct value 
else:
    print("Enter either 'investment' or 'bond' from the menu above to proceed: ")

