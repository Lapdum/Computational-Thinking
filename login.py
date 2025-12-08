import sys
import time
from clear_Screen import Clear_Screen

def Login(cnt):
    #Username Default : Student123
    #Password Default : 12345

    print("Please enter your username and password!")
    username = input("Username : ")
    password = input("Password : ")

    if username == "Student123" and password == "12345":
        return True
    elif cnt < 3:
        print("Incorrect username or password!")
        cnt += 1
        Clear_Screen()
        return Login(cnt)
    else:
        print("Too many failed login attempts!")
        print("Shutting down TaskCommand...")
        time.sleep(3)
        sys.exit()