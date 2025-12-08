import time
from clear_Screen import Clear_Screen
from TaskViewer import taskViewer
from validate_date import validate_Date

def Task():
    Clear_Screen()
    tracker = taskViewer()
    operation = ''
    while operation != 4:
        print("Welcome to Tasks!")
        tracker.display_tasks()
        print("Task Commands: ")
        print("1. Add new task")
        print("2. Delete new task")
        print("3. Edit task")
        print("4. Back to menu")
        operation = int(input("Input: "))

        if operation == 1:
            Clear_Screen()
            is_valid = False
            print("Please enter the task details!")
            task = input("Task name : ")
            while is_valid != True:
                deadline = input("Task deadline (DD-MM-YYYY): ")
                is_valid, message = validate_Date(deadline)
                if is_valid != True:
                    print(f"{message}. Please input it correctly!")
            status = input("Current status : ")

            tracker.add_task(task, deadline, status)
            tracker.save_tasks()
            Clear_Screen()
        elif operation == 2:
            Clear_Screen()
            tracker.delete_task()
            time.sleep(2)
            Clear_Screen()
        elif operation == 3:
            Clear_Screen()
            tracker.edit_task()
            time.sleep(2)
            Clear_Screen()
    from menu import Menu
    
    Menu()
    return