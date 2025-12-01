#Project II : Task tracker
#Test
import os
import csv
import sys
import time
import random


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
        login(cnt)
    else:
        print("Too many failed login attempts!")
        print("Shutting down TaskCommand...")
        time.sleep(3)
        sys.exit()


class TaskViewer:

    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = self.load_tasks()
        #print(f"success wiht {filename}")

    def load_tasks(self):
        tasks = []
        
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        tasks.append(row)
            except (csv.Error, FileNotFoundError):
                return []
        return tasks

    def save_tasks(self):
        
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['task', 'deadline', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.tasks)
                #print(f"Data successfully saved at {file}")
        

    def add_task(self, task, deadline, status="Pending"):
        self.tasks.append({
            "task": task,
            "deadline": deadline,
            "status": status
        })
        self.save_tasks()

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
                
                time.sleep(2)
                clear_Screen()
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

                    time.sleep(2)
                    clear_Screen()
                else:
                    print("Deletion cancelled.")
                    
                    time.sleep(2)
                    clear_Screen()
            else:
                print("Invalid task number!")

                time.sleep(2)
                clear_Screen()
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
            print("Please enter the task details!")
            task = input("Task name : ")
            deadline = input("Task deadline : ")
            status = input("Current status : ")

            tracker.add_task(task, deadline, status)
            tracker.save_tasks()
            clear_Screen()
        elif operation == 2:
            clear_Screen()
            tracker.delete_task()

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
        "Don't give up!", "Tip: Press Ctrl + C for pause"
    ]
    message_break = ["Rest your mind!", "Tip: Press Ctrl + C for pause"]
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
            print("Tip: Press Ctrl + C to pause the timer")

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
            print("Tip: Press Ctrl + C to pause the timer")
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
            Timer.displayTimer(time_in_sec)
            time_focus_string = str(input("Insert focus time (minute:second): "))
            time_focus_array = time_focus_string.split(":")
            # time_focus_array will create [minute, second] array
            time_focus = int(time_focus_array[0]) * 60 + int(time_focus_array[1])

            time_break_string = str(input("Insert break time (minute:second): "))
            time_break_array = time_break_string.split(":")
            time_break = int(time_break_array[0]) * 60 + int(time_break_array[1])
            
            session = int(input("Insert session: "))

            clear_Screen()
            print("[FOCUS MODE]")
            Timer.displayTimer(time_focus)
            operation = str(input("Would you like to start? (y/n): "))
            print("Tip: Press Ctrl + C to pause the timer")
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
