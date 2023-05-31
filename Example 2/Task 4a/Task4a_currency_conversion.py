import pandas as pd
#Imported time so a delay can be introduced throughout this program so users
#have time to read error/validation messages
import time

#The menu() function generates the UI the accepts and validates user choice
def menu():

    flag = True

    while flag:
        print("######################################################")
        print("Which conversion would you like to make today?")
        print("1. Pound Sterling (GBP) to Euros (EUR)")
        print("2. Euros (EUR) to Pound Sterling(GBP)")
        print("3. Pound Sterling (GBP) to Austrailan Dollars (AUD)")
        print("4. Austrailan Dollars (AUD) to Pound Sterling (GBP)")
        print("5. Pound Sterling (GBP) to Japanese Yen (JPY)")
        print("6. Japanese Yen (JPY) to Pound Sterling (GBP)")
        #added options for USD - GBP and GBP - USD
        print("7. Pound Sterling (GBP) to United States Dollar (USD)")
        print("8. United States Dollar (USD) to Pound Sterling (GBP)")
        print("######################################################")

        
        menu_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            time.sleep(1)
            flag = True
        else:
            if int(menu_choice) < 1 or int(menu_choice) > 8:
                print("Sorry, you did not neter a valid choice")
                time.sleep(1)
                flag = True
            else:
                return menu_choice  


#Gets the short version of the conversion information based on user menu choice
def get_currency ():
    currencies = {
       '1': 'GBP - EUR',
       '2': 'EUR - GBP', 
       '3': 'GBP - AUD',
       '4': 'AUD - GBP',
       #spelling corrected
       '5': 'GBP - JPY',
       '6': 'JPY - GBP',
       #new currencies
       '7': 'GBP - USD',
       '8': 'USD - GBP'}
   
    currency = currencies.get(menu_choice)
    
    return currency


menu_choice = menu()
currency = get_currency()


#The get_conversion_rate function uses pandas to get the latest conversion rate
#Imports a csv file in to a data frame
#Uses 'iloc' to get the last/most recent value in the selected column
def get_conversion_rate():
    df = pd.read_csv("Task4a_data.csv")
    
    conversion_rate = round(df[currency].iloc[-1],2)


    return conversion_rate

conversion_rate = get_conversion_rate()


#Accepts and validates user input for teh amount they want to convert
def get_amount_to_convert():
    print("You are converting: ",currency)
    
    flag = True
    
    while flag:
        conversion_amount = input("please enter the ammount you wish to convert: ")
    
        try:
            float(conversion_amount)
        except:
            print("Sorry, you must enter a numerical value")
            time.sleep(1)
            flag = True
        else:
            if float(conversion_amount) < 0:
                print("The amount to be converted cannot be a negative number")
                time.sleep(1)
                flag = True
            else:
                return conversion_amount  

conversion_amount = float(get_amount_to_convert())

#Performs the converison and outputs the final values
def perfom_conversion():
    amount_recieved = round(conversion_amount * conversion_rate, 2)

    print("##################################")
    print('You are converting {} in {}'.format(conversion_amount, currency[0:3]) )
    print('You will recieve {} in {}'.format(amount_recieved, currency[6:9]))
    input("Press ENTER to Continue")
    
perfom_conversion()
