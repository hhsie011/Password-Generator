from random import seed
from random import randint
from datetime import datetime

#Global variable(s)
symbols = "~`!@#$%^&*()_-+={[}]|\\:;\"\'<,>.?/"

if __name__ == "__main__":

    #Ask user for password requirements
    min_ch = int(input("At least how many characters? "))
    max_ch = int(input("At most how many characters? "))
    upper = input("One uppercase letter required? [y/n] ")
    special_ch = input("One special character required? [y/n] ")

    seed(datetime.now())

    #Figure out how many characters
    num_ch = randint(min_ch, max_ch)

    #Figure out location of uppercase character if 
    upper_loc = -1
    if upper == "y":
        upper_loc = randint(0, num_ch)

    #Figure out location of special character if required
    special_loc = -1
    if special_ch == "y":
        while True:
            special_loc = randint(0, num_ch)
            if special_loc != upper_loc:
                break
    
    #Generate password
    passwd = ""
    for i in range(num_ch):
        if i == upper_loc:
            passwd += chr(ord('a') + randint(0, 25)).upper()
            continue
        if i == special_loc:
            passwd += symbols[randint(0, len(symbols) - 1)]
            continue
        if randint(0, 1) == 0:
            passwd += chr(ord('a') + randint(0, 25))
            continue
        passwd += str(randint(0, 9))

    #Output generated password
    print(passwd)
