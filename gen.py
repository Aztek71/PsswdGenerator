import random
import time

print ("""

  ___                                            _      ___                                   _               
 | _ \  __ _   ___  ___ __ __ __  ___   _ _   __| |    / __|  ___   _ _    ___   _ _   __ _  | |_   ___   _ _ 
 |  _/ / _` | (_-< (_-< \ V  V / / _ \ | '_| / _` |   | (_ | / -_) | ' \  / -_) | '_| / _` | |  _| / _ \ | '_|
 |_|   \__,_| /__/ /__/  \_/\_/  \___/ |_|   \__,_|    \___| \___| |_||_| \___| |_|   \__,_|  \__| \___/ |_|  

""")

time.sleep(1)
lenght = input(("Enter the lenght of the password : "))
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbol = "!@#$%^&*()_+"

all = upperCase + lowerCase + number + symbol

if(lenght.isdigit()):
    lenght = int(lenght)
    if(lenght > 0):
        password = ""
        for i in range(lenght):
            password += random.choice(all)
        print("Your password is : " + password)
    else:
        print("The lenght of the password must be greater than 0")
        exit()
