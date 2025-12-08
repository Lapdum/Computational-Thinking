#Project II
from login import Login
from clear_Screen import Clear_Screen
from menu import Menu

def main():
    print("Hello! Welcome to TaskCommand!\n")

    if Login(1):
        Clear_Screen()
        Menu()

#Run Code
main()