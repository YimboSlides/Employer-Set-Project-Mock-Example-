#Importing pandas to read the CSV file
#Importing time to add delays to output messages
import pandas as pd
import time

#Start menu where options are selected, including to quit, see trends or convert a currency
def start():
    print("""###############MENU###################
OPTION 1...........CONVERT CURRENCY
OPTION 2...........VIEW TRENDS
OPTION 3...........QUIT
###############MENU###################""")

#Function that calls the existing code
def converter():
    import Task4a_currency_conversion


#Function for trends, which based on selection takes takes values for the table and calculates it
def trends():
    #same naming convention as in the implemented program
    df = pd.read_csv("Task4a_data.csv")
    
    #repeat is used to repeat the trend sub-menu if an input is wrong
    repeat = True
    
    while repeat == True:
        print("1........GBP - USD")
        print("2........USD - GBP")
        trend = input("Please Enter a Trend to view(1-2): ")

        conversions = {
            '1': 'GBP - USD',
            '2': 'USD - GBP'}

        conversion = conversions.get(trend)
        #Rows set as 86 for total num in the CSV file
        rows = 86

        
        if trend == '1':
            #Displays averages for each individual month in the file, the whole 4 months, and the last week
            
            total = 0
            print("Average conversion for",conversion,"For: ")
            for i in range(rows):
                total = total + df[conversion].iloc[-i]
                                   
            average = total/86
            print("- Last 4 months: ",round(average,2))

            #for each average it calculates it on one line
            average = sum(df[conversion].iloc[1:13])/13
            print("- December: ",round(average,2))

            average = sum(df[conversion].iloc[14:44])/31
            print("- January: ",round(average,2))

            average = sum(df[conversion].iloc[45:72])/28
            print("- February: ",round(average,2))   

            average = sum(df[conversion].iloc[72:88])/13
            print("- March(current month): ",round(average,2))

            average = sum(df[conversion].iloc[79:88])/7
            print("- Last 7 Days: ",round(average,2))

            #input to allow users to continue when ready
            input("Press ENTER to Continue")

            #While loop that allows users to return to trend sub-menu rather than to the main menu
            t_repeat = True
            while t_repeat == True:
                view_trends = input("Would you like to see another trend?(Y/N): ")
                if view_trends.upper() == "Y":
                    repeat = True
                    t_repeat = False

                elif view_trends.upper() == "N":
                    repeat = False
                    t_repeat = False

                else:
                    print("That is not a valid option")
                    time.sleep(1)
             
        elif trend == '2':
            #Displays same averages as trend option 1
            
            total = 0
            print("Average conversion for",conversion,"For: ")
            for i in range(rows):
                total = total + df[conversion].iloc[-i]
                                   
            average = total/86
            print("- Last 4 months: ",round(average,2))

            average = sum(df[conversion].iloc[1:14])/13
            print("- December: ",round(average,2))

            average = sum(df[conversion].iloc[15:46])/31
            print("- January: ",round(average,2))

            average = sum(df[conversion].iloc[47:74])/28
            print("- February: ",round(average,2))   

            average = sum(df[conversion].iloc[74:88])/13
            print("- March(current month): ",round(average,2))

            average = sum(df[conversion].iloc[79:88])/7
            print("- Last 7 Days: ",round(average,2))

            input("Press ENTER to Continue")

            #same loop as trend 1
            t_repeat = True
            while t_repeat == True:
                view_trends = input("Would you like to see another trend?(y/n): ")
                if view_trends.upper() == "Y":
                    repeat = True
                    t_repeat = False

                elif view_trends.upper() == "N":
                    repeat = False
                    t_repeat = False

                else:
                    print("That is not a valid option")
                    time.sleep(1)
            
            
        else:
            print("That is not a valid option")
            time.sleep(1)

#While loop that repeats the menu whenever the chosen selection has finished, such as after viewing trends
#or converting currency
    
choice = ""
while choice != '3':
    start()
    choice = input("Please Enter one of the available options(1-3): ")
    if choice == '1':
        #imports existing code for conversions
        converter()
    
    elif choice == '2':
        #Calls trend function
        trends()

    elif choice == '3':
        #Quit function, simply prints info to let user know it has quit
        print("Quitting....")
        time.sleep(1)
        print("Quit Successful")

    else:
        #Adds delay to incorrect option to make sure prompt is seen
        print("That is not a valid option")
        time.sleep(1)

    
