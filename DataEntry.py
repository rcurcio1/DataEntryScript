import pandas as pd
import numpy as np
from datetime import date
import csv

data = []

while True:
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

    if payments_remaining <= 12:
        term = 12
    elif payments_remaining <=24:
        term = 24
    elif payments_remaining <= 36:
        term = 36
    elif payments_remaining <= 48:
        term = 48
    else:
        term = 60

    deal_array = []
    deal_array.append("ACH")
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

    today = date.today()

    # dd/mm/YY
    day = int(today.strftime("%d"))
    month = int(today.strftime("%m"))
    year = int(today.strftime("%Y"))

    if day <= 15:
        deal_array.append(month + 1)
        deal_array.append(1)
        deal_array.append(year)
        deal_array.append(month)
        deal_array.append(15)
        deal_array.append(year)
    else:
        deal_array.append(month + 2)
        deal_array.append(1)
        deal_array.append(year)
        deal_array.append(month + 1)
        deal_array.append(15)
        deal_array.append(year)

    deal_array.append(term - payments_remaining)
    deal_array.append(payments_remaining)
    for i in range(2):
        deal_array.append("")
    deal_array.append("EFA")
    data.append(deal_array)

    quit = input("Enter Q to quit: ")
    if quit == "Q" or quit == "q":
        break
    
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for row in data:
        spamwriter.writerow(row)
    
