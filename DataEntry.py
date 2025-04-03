import pandas as pd
import numpy as np
from datetime import date
import math
import csv

# Array of arrays to hold each deal entered
portfolio_master = []
deposit_log = []

while True:
    # Retrieve information for one deal from command line
    paynet = input("Enter PayNet score: ")
    softpull = input("Enter CBR: ")
    time_in_business = input("Enter the number of years in business: ")
    
    titled = input("Is the equipment titled? (Y/N): ")
    customer = input("Enter the customer company name: ")
    agreement_number = input("Enter the lease agreement number: ")
    equipment = input("Enter the name of the equipment: ")
    state = input("Enter the state abbreviation for the location of the customer: ")

    amount_financed = input("Enter the total amount financed: ")
    monthly = input("Enter the monthly payment amount: ")
    advance = input("Enter the advance payment amount: ")
    doc_fee = input("Enter the doc fee amount: ")
    payments_remaining = int(input("Enter the number of payments that have been collected: "))

    insurance = input("Enter the monthly insurance amount: ")

    # Determine length of full term from the payments remaining
    term = math.ceil(payments_remaining / 12) * 12

    # Initialize deal array
    deal_array = []
    deal_array.append("ACH")

    # Only add insurance statement if they are paying insurance
    if int(insurance) == 0:
        deal_array.append("")
    else:
        deal_array.append("$" + insurance + "/Star Monthly GA")
    
    deal_array.append(titled)
    deal_array.append("")
    deal_array.append(customer)
    deal_array.append(agreement_number)
    deal_array.append(paynet)
    deal_array.append(softpull)
    deal_array.append(time_in_business)

    deal_array.append(equipment)
    deal_array.append(amount_financed)
    deal_array.append("")
    deal_array.append(monthly)
    deal_array.append(monthly+insurance)
    deal_array.append(advance)
    deal_array.append(doc_fee)
    deal_array.append("EFA")
    for i in range(5):
        deal_array.append("$0.00")
    deal_array.append("")
    deal_array.append(state)
    deal_array.append(term)
    for i in range(3):
        deal_array.append("")
    
    # Get today's date
    today = date.today()
    day = int(today.strftime("%d"))
    month = int(today.strftime("%m"))
    year = int(today.strftime("%Y"))

    # Determine next invoice date and next payment date from whether the current date is before the 15th
    if day <= 15:
        offset = 0
    else:
        offset = 1
    
    deal_array.append(month + 1 + offset)
    deal_array.append(1)
    deal_array.append(year)
    deal_array.append(month + offset)
    deal_array.append(15)
    deal_array.append(year)
    
    deal_array.append(term - payments_remaining)
    deal_array.append(payments_remaining)
    for i in range(2):
        deal_array.append("")
    deal_array.append("EFA")
    portfolio_master.append(deal_array)

    deposit_log_array = []
    deposit_log_array.append(advance + doc_fee)
    deposit_log_array.append(agreement_number)
    deposit_log_array.append(customer)
    deposit_log_array.append("Adv & Doc Fee")

    deposit_log.append(deposit_log_array)
    
    if not insurance == 0:
        insurance_array = []
        insurance_array.append(insurance)
        insurance_array.append(agreement_number)
        insurance_array.append(customer)
        insurance_array.append("GA Ins")
        deposit_log.append(insurance_array)

    # Ask the user if they would like to enter another deal, exit loop if not
    another = input("Would you like to enter another deal? (Y/N) ")
    if another == "N" or another == "n":
        break
# Open csv file and write the information from the deals
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for row in portfolio_master:
        spamwriter.writerow(row)
    for row in deposit_log:
        spamwriter.writerow(row)
    
