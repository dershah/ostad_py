import sys

import requests

# - - - - - - - Current Weather - - - - - - - - -
def weather():
    url = "https://wttr.in/Dhaka?format=j1"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        print(response.json())
    else:
        print("Failed to retrieve data:", response.status_code) 



# - - - - - - - Currency Exchange Rate - - - - - - - - -

def currency():
    url = "https://open.er-api.com/v6/latest/USD"
    alt_url = "https://api.exchangerate-api.com/v4/latest/USD"

    response = requests.get(url)
    alt_response = requests.get(alt_url)

    # Check if the request was successful
    if response.status_code == 200:
        print(response.json())
    elif alt_response.status_code == 200:
            print("Alt:- - - - - - - -")
            print(response.json())
    else:
        print("Failed to retrieve data:", response.status_code) 

def display_menu():
    print("\n===================================================================")
    print("========== ➡️ Real-Time Weather & Currency Data Fetcher ⬅️ ==========")
    print("===================================================================\n")
    print("# 1. Current Weather")
    print("# 2. Currency Exchange Rate")
    print("# 3. Save Result to JSON File")
    print("# 4. View Previous Saved Data")
    print("# 5. Exit")

def main():
    while True:
        try:
            display_menu()
            choice= int(input("Enter An Option: "))
            if choice==1:
                weather()
            elif choice==2:
                currency()                
            elif choice==3:
                pass
            elif choice==4:
                pass
            elif choice==5:
                print("\n########## - The App ended by the choice of user ✅ - ##########\n")
                sys.exit(0)
            else:
                raise ValueError("Invalid Menu Option")

        except Exception as error:
            print(f"\n########## - 💥{error}💥 - ##########\n")

if __name__ == "__main__":
    main()