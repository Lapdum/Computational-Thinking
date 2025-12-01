#Project II : Task tracker (Using JSON)
import os
import json
import sys
import time
import random
from datetime import datetime

def clear_Screen():
    #Windows
    if os.name == 'nt':
        os.system('cls')
    #MacOS/Linux (Replit pakai linux)
    #os.system('clear')


def login(cnt):
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
        clear_Screen()
        return login(cnt)
    else:
        print("Too many failed login attempts!")
        print("Shutting down TaskCommand...")
        time.sleep(3)
        sys.exit()


class TaskViewer:

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
        #print(f"success wiht {filename}")

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)
            #print(f"Data successfully saved at {file}")

    def add_task(self, task, deadline, status="Pending"):
        self.tasks.append({
            "task": task,
            "deadline": deadline,
            "status": status
        })

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete!")
            time.sleep(2)
            clear_Screen()
            return

        print("\nCurrent tasks:")
        print("┌───┬──────────────────────────────────────┐")
        print("│ # │ Task Description                     │")
        print("├───┼──────────────────────────────────────┤")
        for i, task in enumerate(self.tasks, 1):
            task_display = task['task'][:35] + "..." if len(
                task['task']) > 35 else task['task']
            print(f"│ {i:<2}│ {task_display:<36} │")
        print("└───┴──────────────────────────────────────┘")

        try:
            choice = input(
                "Enter task number to delete (or 'cancel' to abort): ").strip(
                )
            if choice.lower() == 'cancel':
                print("Deletion cancelled.")
                return

            choice = int(choice)
            if 1 <= choice <= len(self.tasks):
                task_to_delete = self.tasks[choice - 1]
                confirm = input(f"Delete '{task_to_delete['task']}'? (y/N): "
                                ).strip().lower()
                if confirm == 'y':
                    deleted_task = self.tasks.pop(choice - 1)
                    print(f"✓ Deleted: {deleted_task['task']}")
                    self.save_tasks()
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def edit_task(self):
        if not self.tasks:
            print("No task to edit!")
            time.sleep(2)
            clear_Screen()
            return
        
        print("\nCurrent tasks:")
        task_width = 4
        desc_width = 20
        deadline_width = 10
        status_width = 6
        
        for i, task in enumerate(self.tasks, 1):
            desc_width = max(desc_width, len(task['task']))
            status_width = max(status_width, len(task['status']))
            
        desc_width = min(desc_width, 35) + 2
        status_width = min(status_width, 15) + 2
        task_width = max(task_width, len(str(len(self.tasks)))) + 2
        
        desc_width = max(desc_width, len("Task Description"))
        status_width = max(status_width, len("Status"))
        
        total_width = task_width + desc_width + deadline_width + status_width + 6
        
        print("┌" + "─" * task_width + "┬" + "─" * desc_width + "┬" + "─" * deadline_width + "┬" + "─" * status_width + "┐")
        print(f"│ {'#':^{task_width-2}} │ {'Task Description':^{desc_width-2}} │ {'Deadline':^{deadline_width-2}} │ {'Status':^{status_width-2}} │")
        print("├" + "─" * task_width + "┼" + "─" * desc_width + "┼" + "─" * deadline_width + "┼" + "─" * status_width + "┤")
        
        for i, task in enumerate(self.tasks, 1):
            task_desc = task['task'][:desc_width-3] + "..." if len(task['task']) > desc_width-2 else task['task']
            deadline = task['deadline'][:deadline_width-2]
            status = task['status'][:status_width-3] + "..." if len(task['status']) > status_width-2 else task['status']
        
        print(f"│ {i:^{task_width-2}} │ {task_desc:<{desc_width-2}} │ {deadline:^{deadline_width-2}} │ {status:^{status_width-2}} │")
    
        print("└" + "─" * task_width + "┴" + "─" * desc_width + "┴" + "─" * deadline_width + "┴" + "─" * status_width + "┘")
        
        try:
            choice = input("Enter task number to edit (or 'cancel' to abort): ").strip()
            if choice.lower() == 'cancel':
                print("Edit cancelled.")
                return
            
            choice = int(choice)
            if 1 <= choice <= len(self.tasks):
                task_to_edit = self.tasks[choice - 1]
                print(f"\nEditing Task: {task_to_edit['task']}")
                print(f"Current Deadline: {task_to_edit['deadline']}")
                print(f"Current Status: {task_to_edit['status']}")
                print("\nWhat would you like to edit?")
                print("1. Task name")
                print("2. Deadline")
                print("3. Status")
                print("4. All fields")
                print("5. Cancel")

                edit_choice = input("Choose option (1-5): ").strip()

                if edit_choice == '1':
                    new_task = input("Enter new task name: ").strip()
                    if new_task:
                        task_to_edit['task'] = new_task
                        print("✓ Task name updated!")
                    else:
                        print("Task name cannot be empty!")

                elif edit_choice == '2':
                    is_valid = False
                    while not is_valid:
                        new_deadline = input("Enter new deadline (DD-MM-YYYY): ").strip()
                        is_valid, message = validate_date(new_deadline)
                        if is_valid:
                            task_to_edit['deadline'] = new_deadline
                            print("✓ Deadline updated!")
                        else:
                            print(f"{message}. Please try again!")

                elif edit_choice == '3':
                    new_status = input("Enter new status: ").strip()
                    if new_status:
                        task_to_edit['status'] = new_status
                        print("✓ Status updated!")
                    else:
                        print("Status cannot be empty!")

                elif edit_choice == '4':
                    # Edit all fields
                    new_task = input("Enter new task name: ").strip()
                    if new_task:
                        task_to_edit['task'] = new_task
                    
                    is_valid = False
                    while not is_valid:
                        new_deadline = input("Enter new deadline (DD-MM-YYYY): ").strip()
                        is_valid, message = validate_date(new_deadline)
                        if is_valid:
                            task_to_edit['deadline'] = new_deadline
                        else:
                            print(f"{message}. Please try again!")
                    
                    new_status = input("Enter new status: ").strip()
                    if new_status:
                        task_to_edit['status'] = new_status
                    
                    print("✓ All fields updated!")

                elif edit_choice == '5':
                    print("Edit cancelled.")
                    return
                else:
                    print("Invalid option!")
                    return

                self.save_tasks()
                print("Changes saved successfully!")

            else:
                print("Invalid task number!")
                
        except ValueError:
            print("Please enter a valid number!")
        
    def create_table(self):
        if not self.tasks:
            return "No tasks available!"

        task_width = max(len(task["task"]) for task in self.tasks)
        deadline_width = max(len(task["deadline"]) for task in self.tasks)
        status_width = max(len(task["status"]) for task in self.tasks)

        task_width = max(task_width, len("Task")) + 2
        deadline_width = max(deadline_width, len("Deadline")) + 2
        status_width = max(status_width, len("Status")) + 2

        table = []

        top_border = "┌" + "─" * task_width + "┬" + "─" * deadline_width + "┬" + "─" * status_width + "┐"
        table.append(top_border)

        header = f"│{'Task':^{task_width}}│{'Deadline':^{deadline_width}}│{'Status':^{status_width}}│"
        table.append(header)

        separator = "├" + "─" * task_width + "┼" + "─" * deadline_width + "┼" + "─" * status_width + "┤"
        table.append(separator)

        for task in self.tasks:
            row = f"│{task['task']:<{task_width}}│{task['deadline']:^{deadline_width}}│{task['status']:^{status_width}}│"
            table.append(row)

        bottom_border = "└" + "─" * task_width + "┴" + "─" * deadline_width + "┴" + "─" * status_width + "┘"
        table.append(bottom_border)

        return "\n".join(table)

    def display_tasks(self):
        print(self.create_table())
        
def validate_date(deadline, date_format=("%d-%m-%Y")):
    try:
        datetime.strptime(deadline, date_format)
        return True,""
    except ValueError as e:
        return False, f"Invalid date format: {e}"
    


def task():
    clear_Screen()
    tracker = TaskViewer()
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
            clear_Screen()
            is_valid = False
            print("Please enter the task details!")
            task = input("Task name : ")
            while is_valid != True:
                deadline = input("Task deadline (DD-MM-YYYY): ")
                is_valid, message = validate_date(deadline)
                if is_valid != True:
                    print(f"{message}. Please input it correctly!")
            status = input("Current status : ")

            tracker.add_task(task, deadline, status)
            tracker.save_tasks()
            clear_Screen()
        elif operation == 2:
            clear_Screen()
            tracker.delete_task()
            time.sleep(2)
            clear_Screen()
        elif operation == 3:
            clear_Screen()
            tracker.edit_task()
            time.sleep(2)
            clear_Screen()

    menu()
    return


class Timer:

    def __init__(self, time_in_sec):
        self.time_in_sec = time_in_sec

    @staticmethod
    def displayTimer(time_in_sec):
        minute, second = divmod(time_in_sec, 60)
        timer = '{:02d}:{:02d}'.format(minute, second)
        print("┌" + "─" * (len(timer) + 2) + "┐")
        print(f"│ {timer} │")
        print("└" + "─" * (len(timer) + 2) + "┘")

    def countdown(self, message, mode):
        message_cnt = 0
        current_message = random.randint(0, len(message) - 1)
        chosen_message = message[current_message]

        while self.time_in_sec:
            try:
                clear_Screen()
                print(mode)
                Timer.displayTimer(self.time_in_sec)
                print(chosen_message)

                time.sleep(1)
                self.time_in_sec -= 1

                message_cnt += 1
                if message_cnt == 10:
                    current_message = random.randint(0, len(message) - 1)
                    chosen_message = message[current_message]
                    message_cnt = 0
            except KeyboardInterrupt:
                while True:
                    clear_Screen()
                    print("Timer paused")
                    print("What would you like to do?")
                    print("1. Continue timer")
                    print("2. Stop timer")
                    operation = str(input("Input: "))
                    if(operation == "1"):
                        print("Timer will continue!")
                        time.sleep(1)
                        break
                    else:
                        timer()

    def focusMode(self, message, increment, mode):
        mode = f"[FOCUS MODE]: Session {increment + 1}"
        self.countdown(message, mode)
        clear_Screen()
        print(mode)
        Timer.displayTimer(0)
        time.sleep(1)
        print("You did it! Take a proper break!")
        time.sleep(3)

    def breakMode(self, message, increment, session, mode):
        mode = f"[BREAK MODE]: Session {increment + 1}"
        self.countdown(message, mode)
        clear_Screen()
        print(mode)
        Timer.displayTimer(0)
        time.sleep(1)
        if (increment != session - 1):
            print("Go back to your work!")
        else:
            print("Congratulations! Now, take a long rest!")
        time.sleep(3)


def timer():
    clear_Screen()
    time_in_sec = 0
    operation = ''
    message_focus = [
        "Keep going!", "You'll get there!", "Focus!", "Chase your dreams!",
        "Don't give up!", "Tip: Press Ctrl + C for pause!"
    ]
    message_break = ["Rest your mind!", "Tip: Press Ctrl + C for pause!"]
    mode = ""
    while operation != 4:
        print("Welcome to Pomodoro Timer!")
        Timer.displayTimer(time_in_sec)
        print("How long do you want to be focus?")
        print("Select preset: ")
        print("1. 4 x 25 minutes focus, 5 minutes break")
        print("2. 2 x 50 minutes focus, 10 minutes break")
        print("3. Custom time")
        print("4. Back to menu")
        operation = int(input("Input: "))

        if (operation == 1):
            time_in_sec = 25 * 60
            clear_Screen()
            print("[FOCUS MODE]")
            Timer.displayTimer(time_in_sec)
            operation = str(input("Would you like to start? (y/n): "))
            print("Tip: Press Ctrl + C for pause!")

            if (operation == "y"):
                session = 4
                for i in range(session):
                    time_in_sec = 25 * 60
                    focus_timer = Timer(time_in_sec)
                    focus_timer.focusMode(message_focus, i, mode)

                    time_in_sec = 5 * 60
                    break_timer = Timer(time_in_sec)
                    break_timer.breakMode(message_break, i, session, mode)
                clear_Screen()
                timer()
            else:
                timer()
        elif (operation == 2):
            time_in_sec = 50 * 60
            clear_Screen()
            print("[FOCUS MODE]")
            Timer.displayTimer(time_in_sec)
            operation = str(input("Would you like to start? (y/n): "))
            print("Tip: Press Ctrl + C for pause!")
            if (operation == "y"):
                session = 2
                for i in range(session):
                    time_in_sec = 50 * 60
                    focus_timer = Timer(time_in_sec)
                    focus_timer.focusMode(message_focus, i, mode)

                    time_in_sec = 10 * 60
                    break_timer = Timer(time_in_sec)
                    break_timer.breakMode(message_break, i, session, mode)
                clear_Screen()
                timer()
            else:
                timer()
        elif (operation == 3):
            clear_Screen()
            print("[FOCUS MODE]")
            time_focus_string = str(input("Insert focus time (minute:second): "))
            time_focus_array = time_focus_string.split(":")
            time_focus = int(time_focus_array[0]) * 60 + int(time_focus_array[1])

            time_break_string = str(input("Insert break time (minute:second): "))
            time_break_array = time_break_string.split(":")
            time_break = int(time_break_array[0]) * 60 + int(time_break_array[1])

            session = int(input("Insert session: "))

            clear_Screen()
            print("[FOCUS MODE]")
            Timer.displayTimer(time_focus)
            operation = str(input("Would you like to start? (y/n): "))
            print("Tip: Press Ctrl + C to pause the timer!")
            if (operation == "y"):
                for i in range(session):
                    time_in_sec = time_focus
                    focus_timer = Timer(time_in_sec)
                    focus_timer.focusMode(message_focus, i, mode)

                    time_in_sec = time_break
                    break_timer = Timer(time_in_sec)
                    break_timer.breakMode(message_break, i, session, mode)
                clear_Screen()
                timer()
            else:
                timer()
    menu()
    return


class JournalTracker:
    pass


def journal():
    clear_Screen()
    print("Welcome to Journal!")
    print("What would you like to do today?")
    print("1. Write a new journal")
    print("2. Read your old journal")
    print("3. Edit your old journal")
    print("4. Back to menu")
    operation = int(input("Input : "))

    if operation == 1:
        pass
    elif operation == 2:
        pass
    elif operation == 3:
        pass
    elif operation == 4:
        menu()


def menu():
    clear_Screen()
    print("What would you like to do today?")
    print("1. Tasks")
    print("2. Pomodoro Timer")
    print("3. Journal")
    print("4. Quit")

    operation = int(input("Input : "))

    if operation == 1:
        task()
    elif operation == 2:
        timer()
    elif operation == 3:
        journal()
    elif operation == 4:
        sys.exit()


def main():
    print("Hello! Welcome to TaskCommand!\n")

    if login(1):
        clear_Screen()
        menu()

#Run Code
main()
