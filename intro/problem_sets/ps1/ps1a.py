## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
months = 0
monthly_salary = yearly_salary/12
amount_saved = 0
r = 0.05

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < (cost_of_dream_home*portion_down_payment):
    months += 1
    monthly_return = (portion_saved*monthly_salary) + (amount_saved * (r/12))
    amount_saved += monthly_return

print(f"Number of months: {months}")
