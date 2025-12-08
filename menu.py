import sys
from clear_Screen import Clear_Screen
from task import Task
from Timer import timer
from journal import Journal

def Menu():
    Clear_Screen()
    print("What would you like to do today?")
    print("1. Tasks")
    print("2. Pomodoro Timer")
    print("3. Journal")
    print("4. Quit")

    operation = int(input("Input : "))

    if operation == 1:
        Task()
    elif operation == 2:
        timer()
    elif operation == 3:
        Journal()
    elif operation == 4:
        sys.exit()