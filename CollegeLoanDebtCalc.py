
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: colinbehr
"""

studType = [] #Dependent or Independent
loan = [] #tuition amount
subRate = [] #subsidized loan interest rate
unsubRate = [] #Unsubsidized rate

#start counter for years 
years = 0
#While still in college
attend = True
while (attend):
    while True:
        status = input('Enter D for Dependent or I for Independent: ')
        if (status == 'I' or status == 'D'):
            break
        else:
            print('Enter Correct Status!')
            
### Tuition Loan Amount ###

    while True:
        try:
            amt = int(input('How much is your loan this year?: '))
            
            #YEAR 1
            if (years == 0 and status == 'D' and amt <= 5500):
                break
            elif (years == 0 and status == 'I' and amt <=9500):
                break
            
            #YEAR 2
            elif(years == 1 and status == 'D' and amt <= 6500):
                break
            elif(years == 1 and status == 'I' and amt <= 10500):
                break
            
            #YEAR 3 & BEYOND
            elif(years >= 2 and status == 'D' and amt <= 7500):
                break
            elif(years >= 2 and status == 'I' and amt <= 12500):
                break
                      
            else: 
                print('Enter correct amount!')
                continue
    
        except:
            print('Amount should be a whole number!')
            continue

    loan.append(amt)

### Subsidized Interest Rate ###
    
    while (True):
        try:
           subr = float(input('Insert the subsidized loan interest rate: '))
           break
       
        except:
           print('Enter the rate as a percent number (like 4.8): ')
           continue 
    
    subRate.append(subr)

### Unsubsidized Interest Rate ###

    while(True):
        try:
            unsubr = float(input('Insert the unsubsidized loan interest rate: '))
            break
        except:
            print('Enter the rate as a percent number (like 4.8): ')

    unsubRate.append(unsubr)

### Next Year Attendance ###
    next_year = input('Are you attending another year of undegrad -- Y or N?: ')
    if next_year == 'Y':
        years+=1
    
    elif next_year == 'N':
        attend = False
        years += 1
    
    else:
        print('Enter either Y or N')
        
#typeStud = ["D","D","I","I"]
#loan = [5000, 6000, 9000, 12000]
#subRate = [5,6,6,7]
#unsubRate = [7,8,8,9]
#years = 4
subLoanLimit = [3500, 4500, 5500]
totalOwed = 0
loansList, rateList = [], []

for ac_year in range(years):
   
    #temp index
    if ac_year < 2:
        ind = ac_year
    else:
        ind = min(2,ac_year)
       
    #calculate the unsubsidised loan amt
    unsubAmt = loan[ac_year] - subLoanLimit[ind]
   
    #charge interest on ''unsubAmt"
    annual_unsubRate = unsubRate[ac_year]
    monthly_unsubRate = annual_unsubRate/12/100
   
    #month count
    month_count = (years - ac_year) * 12 + 3
   
    for m in range(month_count):
        unsubAmt *= (1 + monthly_unsubRate)
       
    totalOwed = totalOwed + unsubAmt + subLoanLimit[ind]
   
    #append to lists
    loansList.append(unsubAmt)
    loansList.append(subLoanLimit[ind])
   
    rateList.append(unsubRate[ac_year])
    rateList.append(subRate[ac_year])
   
    if ac_year >= 3:
        yearleft = max(2, ac_year)
        
        
        print('\nTotal owed 6 months after leaving college:','${:0,.2f}'.format(totalOwed))
        
        
debtDict = {0:10,
            7500: 12,
            10000: 15,
            20000: 20,
            40000: 25,
            60000: 30}

### Term (how long it'll take to pay back 100%) Calcs ###
for i in debtDict:
    if totalOwed < i:
        break
    term = debtDict[i]
    
debtTotal = totalOwed
InterestTotal = 0

for loan, rate in zip(loansList, rateList):
    InterestTotal += loan * (rate/100)
    
newRate = InterestTotal / debtTotal 



import numpy_financial as np
payment = np.pmt(newRate/12, term*12, totalOwed) * -1


totaleverything = (payment * term * 12)
TotalInt = (totaleverything - totalOwed)



print('\nConsolidated Interest Rate: ', '{:0,.2f}'.format(newRate*100), '%')
print("\nMonthly payment after consolidation: $", '{:0,.2f}'.format(payment))
print('\nLoan payments continue for this many years: ',(term))
print('\nTotal interest paid on school loans: $', '{:0,.2f}'.format(TotalInt))
print('\nTotal paid loans plus interest: $','{:0,.2f}'.format( totaleverything))


