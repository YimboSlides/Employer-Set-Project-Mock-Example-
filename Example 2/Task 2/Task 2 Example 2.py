#code for investmant calculator
#T-Level Sample Assessmnet Material (Task 2)
#Non working code


    
def opening ():
    print('#####################################')
    print('Welcome to the investment quote system')
    print('')
    print('Please enter your name')
    opening.name = input()
    
    print('Please enter your Address')
    opening.address = input()
    
    print ('Please eneter your telephone number')
    opening.phone = input()
    while len(opening.phone) != 11:
        print('Phone number is not the correct length, Please enter telephone number: ')
        opening.phone = input()
    
    print ('How much would you like to invest per month (£)?')
    opening.investSum = int(input())
    
def options ():
    print('#####################################')
    print('There are two types of investment available:')
    print('Option 1 - Savings plan')
    print('Option 2 - Managed stock investment')
    print('Please select an option (press 1 or 2 followed by enter)')
    print('#####################################')
    
    option = input()
          
      
    while option != '1' and option != '2':
        print('Please select an option (press 1 or 2 followed by enter)')
        
        option = input()
        
    if option == '1':
        savingsMain()
    else:
        stocksMain()
        

def savingsMain():
    savingsMain.monthlyInvest = opening.investSum
    savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
    
    while savingsMain.yearlyInvest > 20000:
        print('The the initial monthly amount is too high for this type of plan' )
        print ('How much would you like to invest per month (£)?')
        savingsMain.monthlyInvest = float(input())
        savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12

    while savingsMain.yearlyInvest <= 0:
        print('The the initial monthly amount cannot be zero' )
        print ('How much would you like to invest per month (£)?')
        savingsMain.monthlyInvest = float(input())
        savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
    
    savingsPrint()
    
    

def savingsMin():
    predictReturns = 0.012
    yearlyFees = 0.0025 * 12
    savingsMin.total = savingsMain.yearlyInvest
    print('#####################################')   
    print('Forecasted perfromance of this plan at the lowest rate of return:')
    
    for i in range(10):
        savingsMin.total = (savingsMin.total + (savingsMin.total * predictReturns)) - yearlyFees
        
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£{:.2f}'.format(savingsMin.total))
            print('')
            print('Total fees paid in this period: £{:.2f}'.format(yearlyFees * (i+1)))
            print('')
            print('Total profit in this period: £{:.2f}'.format(savingsMin.total - (yearlyFees * (i+1))))
            print('')
    print('#####################################')
    print('')

def savingsMax():
    predictReturns = 0.024
    yearlyFees = 0.0025 * 12
    savingsMax.total = savingsMain.yearlyInvest
    print('#####################################')
    print('Forecasted perfromance of this plan at the highest rate of return::')
    
    for i in range(10):
        savingsMax.total = (savingsMax.total + (savingsMax.total * predictReturns)) - yearlyFees
        
         
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£{:.2f}'.format(savingsMax.total,2))
            print('')
            print('Total fees paid in this period: £{:.2f}'.format(yearlyFees * (i+1)))
            print('')
            print('Total profit in this period: £{:.2f}'.format(savingsMax.total - (yearlyFees * (i+1))))
            print('')
    print('#####################################')  
    print('')

     
def stocksMain():
    stocksMain.monthlyInvest = opening.investSum
    stocksMain.yearlyInvest = stocksMain.monthlyInvest * 12
    
    while stocksMain.yearlyInvest <= 0:
        print('The the initial monthly amount cannot be zero' )
        print ('How much would you like to invest per month (£)?')
        savingsMain.monthlyInvest = float(input())
        savingsMain.yearlyInvest = savingsMain.monthlyInvest * 12
    
    stocksPrint()
    
def stocksMin():
    predictReturns = 0.04
    yearlyFees = 0.13 * 12
    stocksMin.total = stocksMain.yearlyInvest
    print('#####################################')   
    print('Forecasted perfromance of this plan at the lowest rate of return:')
    
    for i in range(10):
        stocksMin.total = (stocksMin.total + (stocksMin.total * predictReturns)) - yearlyFees
        
        if stocksMin.total >= 40000:
            taxRate = 0.2
        elif stocksMin.total >= 12000:
            taxRate = 0.1
        else:
            taxRate = 0
        
        taxPayable = stocksMin.total * taxRate
        postTax = stocksMin.total - taxPayable
        
              
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£{:.2f}'.format(postTax))
            print('')
            print('Total fees paid in this period: £{:.2f}'.format(yearlyFees * (i+1) ))
            print('')
            print('Total profit in this period: £{:.2f}'.format(postTax - (yearlyFees * (i+1))))
            print('')
            print('Total tax due in this period: £{:.2f}'.format(taxPayable))
            print('')
    print('#####################################')
    print('') 

def stocksMax():
    predictReturns = 0.23
    yearlyFees = 0.13 * 12
    stocksMax.total = stocksMain.yearlyInvest
    print('#####################################')   
    print('Forecasted perfromance of this plan at the higher rate of return:')
    
    for i in range(10):
        stocksMax.total = (stocksMax.total + (stocksMax.total * predictReturns)) - yearlyFees
        
        if stocksMax.total >= 40000:
            taxRate = 0.2
        elif stocksMax.total >= 12000:
            taxRate = 0.1
        else:
            taxRate = 0
        
        taxPayable = stocksMax.total * taxRate
        postTax = stocksMax.total - taxPayable
        
              
        if i == 0 or i == 4 or i == 9:
            print('At the end of year', str(i+1))
            print('Your investment will be worth:')
            print('£{:.2f}'.format(postTax))
            print('')
            print('Total fees paid in this period: £{:.2f}'.format(yearlyFees * (i+1)))
            print('')
            print('Total profit in this period: £{:.2f}'.format(postTax - (yearlyFees * (i+1))))
            print('')
            print('Total tax due in this period: £{:.2f}'.format(taxPayable))
            print('')
    print('#####################################')
    print('') 


def savingsPrint ():
    print('--------------------------------------------------------')
    print('Personal Investment Quote for:')
    print('Name: ', opening.name)
    print('')
    print('Telephone Number: ', opening.phone)
    print('--------------------------------------------------------')
    print('')
    print('You selected a savings plan')
    savingsMin()
    savingsMax()

def stocksPrint ():
    print('--------------------------------------------------------')
    print('Personal Investment Quote for:')
    print('Name: ', opening.name)
    print('')
    print('Telephone Number: ', opening.phone)
    print('--------------------------------------------------------')
    print('')
    print('You chose a Managed Stock Investment plan')
    stocksMin()
    stocksMax()


opening()
options()
