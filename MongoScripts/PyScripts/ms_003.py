
## experimenting with a python menu sytem

def main_menu():
    os.system('clear')

    print("Please select which source to pull data from.")
    print("Your options are:")
    print("(1) Alpha Vantage, (2) Google Finance, (3) Yahoo Finance.")

    num = input()
    if num > 3 || num < 1:
        print("Invalid option, please try again")
        menu_source()
    elif num == 1:
        source = "Alpha Vantage"
    elif num == 2:
        source = "Google Finance"
    elif num == 3:
        source = "Yahoo Finance"


    print("Please select which field to pull data from.")
    print("Your options are:")
    print("(1) Stock Time, (2)Foreign Exchange, (3)Digital Crypto, (4)Technical Indicators, (5)Sector Performance.")

     num = input()
         if num > 5 || num < 1:
             print("Invalid option, please try again")
             menu_source()
         elif num == 1:
             field = "Stock Time"
         elif num == 2:
             field = "Foreign Exchange"
         elif num == 3:
             field = "Digital Crypto"
         elif num == 4:
             field = "Technical Indicator"
         elif num == 5:
             field = "Sector Performance"

    print("Please select which field to pull data from.")
    print("Your options are:")
    
