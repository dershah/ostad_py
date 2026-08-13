import sys

import requests
import datetime
import os
import json

last_data=None
current_time= datetime.datetime.now()
# - - - - - - - Current Weather - - - - - - - - -
def weather():
    
    city = input("Enter the City Name: ").strip().lower()
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data=response.json()
        city = city.upper()
        temperature = f"{data['current_condition'][0]['temp_C']}°C"
        humidity = f"{data['current_condition'][0]['humidity']}%"
        wind_speed = f"{data['current_condition'][0]['windspeedKmph']} km/h"
        condition= f"{data['current_condition'][0]['weatherDesc'][0]['value']}"

        print("\n========================================")
        print("======= ➡️ 🌪️ Weather Report ☀️ ⬅️ ======")
        print("========================================\n")
        print(f"City: {city}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Wind Speed: {wind_speed}")
        print(f"Condition: {condition}")
        print(f"Fetched At: {current_time}")

        weather_report={
            "Type":"Weather",
            "City": city,
            "Temperature":temperature,
            "Humidity":humidity,
            "Wind Speed":wind_speed,
            "Condition":condition,
            "Fetched At": f"{current_time}"
        }
        globals()['last_data']=weather_report
    else:
        print("💥Failed to retrieve data:", response.status_code)



# - - - - - - - Currency Exchange Rate - - - - - - - - -

def currency():
    base_currency= input("Enter the Base Currency: ").strip().upper()
    target_currency= input("Enter the Target Currency: ").strip().upper()
    url = f"https://open.er-api.com/v6/latest/{base_currency.lower()}"

    response = requests.get(url)

    # is the request was successful?
    if response.status_code == 200:
        data= response.json()
        rate = round(data['rates'][target_currency], 2)
        print("\n========================================")
        print("======= ➡️ 🤑 Currency Report 💸 ⬅️ =======")
        print("========================================\n")
        print(f"1 {base_currency} = {rate} {target_currency}")
        print(f"Fetched At: {datetime.datetime.now()}")
        currency_report={
            "Type":"Currency",
            "Base": base_currency,
            "Target":target_currency,
            "Rate":rate,
            "Fetched At": f"{current_time}"
        }
        globals()['last_data']=currency_report
    else:
        print("\n💥Failed to retrieve data:", response.status_code) 

def save_json():
    file_path= "./module_4/data.json"
    json_string = json.dumps(globals()['last_data'], indent=4)
    with open(file_path, 'w') as file:
        file.write(json_string)
    print("\nLast data has been saved successfully ✅\n")
    

def view_json():
    print("\n========================================")
    print("============ ➡️ Saved Data ⬅️ ============")
    print("========================================\n")
    file_path= "./module_4/data.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            if not data:
                print("❌ File exists but JSON content is empty ❌")
            else:
                for key, value in data.items():
                    print(key,": ", value)

    else:
        print("❌ File does not exist or is empty ❌")
    
    

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
                save_json()
            elif choice==4:
                view_json()
            elif choice==5:
                print("\n########## - The App ended by the choice of user ✅ - ##########\n")
                sys.exit(0)
            else:
                raise ValueError("Invalid Menu Option")

        except Exception as error:
            print(f"\n########## - 💥{error}💥 - ##########\n")

if __name__ == "__main__":
    main()