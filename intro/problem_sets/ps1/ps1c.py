## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_the_house = 800000
down_payment = cost_of_the_house*0.25
epsilon = 100
upper_r = 1
lower_r = 0
r = (upper_r + lower_r)/2
months = 36
amount_saved = initial_deposit * ((1 + (r/12))**months)
steps = 1
max_savings = initial_deposit * ((1 + (upper_r/12))**months)

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if max_savings < down_payment:
    print("Not possible to reach down payment in time.")
    r = None

else:
    while abs(amount_saved - down_payment) >= epsilon:
        steps += 1
        if amount_saved > down_payment:
            upper_r = r
        elif amount_saved < down_payment:
            lower_r = r
        elif amount_saved == down_payment:
            break
        r = (lower_r + upper_r)/2
        amount_saved = initial_deposit * ((1 + (r/12))**months)
        print(amount_saved)

    print(f"Best savings rate: {r}")
    print(f"Steps in bisection search: {steps}")

