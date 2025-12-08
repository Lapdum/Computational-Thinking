import os
import csv
from module import Maximum, Minimum, find_max_lengths, length, number_task
from validate_date import validate_Date

class TaskViewer:
    def __init__(self, filename = "Tasks_Copy.csv"):
        self.filename = filename
        self.tasks = self.load_task()
        print(f"Success with {filename}")
        
    def load_task(self):
        tasks = []
        
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    tasks = [row for row in reader]
            except(csv.Error, FileNotFoundError):
                print("Error on load_tasks")
                return []
        return tasks
    
    def save_tasks(self):
    
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['task', 'deadline', 'status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.tasks)
            print("Data successfully saved!")
            
    def add_task(self, task, deadline, status):
        self.tasks = [*self.tasks, {
            'task' : task,
            'deadline' : deadline,
            'status' : status
        }]
        
        print("Successfully added a new task!")
        
    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete!")
            return
        
        print("\nCurrent tasks:")
        print("┌───┬──────────────────────────────────────┐")
        print("│ # │ Task Description                     │")
        print("├───┼──────────────────────────────────────┤")
        for i, task in enumerate(self.tasks, 1):
            mx_len = 33
            if length(task['task']) > mx_len:
                task_display = task['task'][:mx_len] + "..."
            else:
                task_display = task['task']
            print(f"│ {i:<2}│ {task_display:<36} │")
        print("└───┴──────────────────────────────────────┘")
        
        try:
            choice = input("Enter task number to delete (or 'cancel' to abort): ")
            if choice.lower() == 'cancel':
                return "Deletion cancelled."
            
            choice = int(choice)
            if 1 <= choice <= number_task(self.tasks):
                task_to_delete = self.tasks[choice - 1]
                confirm = input(f"Delete '{task_to_delete['task']}'? (y/N): ").lower()
                
                if confirm == 'y':
                    task_to_delete = self.tasks[choice - 1]
                    self.tasks = [n for i, n in enumerate(self.tasks) if i != choice - 1]
                    self.save_tasks()
                    return f"Deleted: {task_to_delete['task']}"
                else:
                    return "Deletion cancelled."
            else:
                return "Invalid task number!"
        except:
            return "Please enter a valid number!"
        
    def edit_task(self):
        if not self.tasks:
            print("No task to edit!")
            return
        
        print("\nCurrent tasks:")
        task_width = 4
        desc_width = 20
        deadline_width = 10
        status_width = 6
        
        for i, task in enumerate(self.tasks, 1):
            desc_width = Maximum(desc_width, length(task['task']))
            deadline_width = Maximum(deadline_width, length(task['deadline']))
            status_width = Maximum(status_width, length(task['status']))
        
        desc_width = Minimum(desc_width, 35) + 2
        status_width = Minimum(status_width, 15) + 2
        task_width = Maximum(task_width, length(str(number_task(self.tasks)))) + 2
        
        desc_width = Maximum(desc_width, length("Task Description"))
        deadline_width += 2
        status_width = Maximum(status_width, length("Status"))
        
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
            choice = input("Enter task number to edit (or 'cancel' to abort): ")
            if choice.lower() == "cancel":
                return "Edit cancelled."
            
            choice = int(choice)
            if 1 <= choice <= number_task(self.tasks):
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
                
                edit_choice = input("Input: ")
                
                if edit_choice == '1':
                    new_task = input("Enter new task name: ")
                    if new_task:
                        task_to_edit['task'] = new_task
                        print("Task name updated!")
                    else:
                        print("Task name cannot be empty!")
                elif edit_choice == '2':
                    is_valid = False
                    while not is_valid:
                        new_deadline = input("Enter new deadline (DD-MM-YYYY): ")
                        is_valid, msg = validate_Date(new_deadline)
                        
                        if is_valid:
                            task_to_edit['deadline'] = new_deadline
                            print("Dealine updated!")
                        else:
                            print(f"{msg}. Please try again!")
                elif edit_choice == '3':
                    new_status = input("Enter new status: ")
                    if new_status:
                        task_to_edit['status'] = new_status
                        print("Status updated!")
                    else:
                        print("Status cannot be empty!")
                elif edit_choice == '4':
                    new_task = input("Enter new task name: ")
                    if new_task:
                        task_to_edit['task'] = new_task
                    
                    is_valid = False
                    while not is_valid:
                        new_deadline = input("Enter new deadline (DD-MM-YYYY): ")
                        is_valid, msg = validate_Date(new_deadline)
                        
                        if is_valid:
                            task_to_edit['deadline'] = new_deadline
                    
                    new_status = input("Enter new status: ")
                    if new_status:
                        task_to_edit['status'] = new_status
                        
                        print("All fields updated!")
                elif edit_choice == '5':
                    print("Edit cancelled.")
                    return
                else:
                    print("Invalid option!")
                    return
                
                self.save_tasks()
                print("Changes saved successfully!")
                return
            
            else:
                print("Invalid task number!")
                return
        except:
            print("Please enter a valid number!")
            return
        
                
        
    def display_tasks(self):
        if not self.tasks:
            print("No tasks available!")
            return
        
        task_width, deadline_width, status_width = find_max_lengths(self.tasks)
        task_width = int(Maximum(task_width, length("Task"))) + 2
        deadline_width = int(Maximum(deadline_width, length("Deadline"))) + 2
        status_width = int(Maximum(status_width, length("Status"))) + 2
        
        top_border = "┌" + "─" * task_width + "┬" + "─" * deadline_width + "┬" + "─" * status_width + "┐"
        print(top_border)
        header = f"│{'Task':^{task_width}}│{'Deadline':^{deadline_width}}│{'Status':^{status_width}}│"
        print(header)
        separator = "├" + "─" * task_width + "┼" + "─" * deadline_width + "┼" + "─" * status_width + "┤"
        print(separator)
        for task in self.tasks:
            row = f"│{task['task']:<{task_width}}│{task['deadline']:^{deadline_width}}│{task['status']:^{status_width}}│"
            print(row)
        bottom_border = "└" + "─" * task_width + "┴" + "─" * deadline_width + "┴" + "─" * status_width + "┘"
        print(bottom_border)