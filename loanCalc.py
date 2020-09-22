# Get the basic info fo the loan
def get_loan_info():
    #create a empty dict to represent a loan
    loan = {}
    # get user input for loan
    loan['principal'] = float(input("Enter the loan amount: "))
    loan['rate'] = float(input("Enter the interest rate: "))/100
    loan['monthly payment']=float(input("Enter the desired monthly payment amount: "))
    loan['money paid']=0

    return loan 


#current loan status
def show_loan_info(loan, number):
    print(f"\n---Loan information after {str(number)} months---")
    for key, value in loan.items():
        print(f"{key.title()} : {str(value)}")

#update loan for interest
def collect_interest(loan):
    # divide by 12 for monthly interest
    loan['principal'] = loan['principal'] + loan['principal']*loan['rate']/12


#making monthyly payment
def make_monthly_payment(loan):
    loan['principal']= loan['principal']-loan['monthly payment']
    #you are required to make a full payment this month, you have not yet paid off your loan
    if loan['principal'] > 0:
        loan['money paid'] += loan['monthly payment']
    else:
        # loan principal will be negative
        loan['money paid'] += loan['monthly payment'] + loan['principal']
        loan['principal'] = 0


# display the result
def summarize_loan(loan, number, initial_principal):
    print(f"\nCongrats! You paid of your loan in {str(number)} months!")
    print(f"Your initial loan was ${str(initial_principal)} at a rate of {str(100*loan['rate'])}")
    print(f"Your monthly payment was ${str(loan['monthly payment'])}.")
    print(f"Your spent ${str(round(loan['money paid'],2))} in total.")

    interest = round(loan['money paid'] - initial_principal, 2)
    print(f"You spent ${str(interest)} on interest!")

# create graph
# def create_graph(data, loan):
#     x_values = []   #month numbers
#     y_values = []   #principal values

#     #loop through dataset
#     # point[0] represent month number
#     # point[1] represent a principal value
#     for point in data:
#         x_values.append(point[0])
#         x_values.append(point[1])

#     #create a plot
#     pyplot.plot(x_values, y_values)
#     pyplot.title(str(100 * loan['rate']) + "% interest with $" + str(loan['monthly payment'])+ " monthly payment!")
#     pyplot.xlabel("Month Number")
#     pyplot.ylabel("Principal")
#     pyplot.show()



print("Welcome to the Loan calculator App ")

month_number = 0
my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []
show_loan_info(my_loan, month_number)
input("Press 'Enter' to begin paying off the loan.")

while my_loan['principal'] > 0:
    #can never pay off loan 
    if my_loan['principal'] > starting_principal:
        break 
    
    #possible to payof loan
    #increment month number, collect interest, make a payment, 
    month_number += 1
    collect_interest(my_loan)
    make_monthly_payment(my_loan)
    data_to_plot.append((month_number, my_loan['principal']))
    show_loan_info(my_loan, month_number)


# loan is paid off in full
if my_loan['principal'] <= 0:
    summarize_loan(my_loan, month_number, starting_principal)
else:
    print("\n You will never pay off the loan")
    print("you can not get ahead og interest payment.")



