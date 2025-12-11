from JournalTracker import JournalTracker
from clear_Screen import Clear_Screen

def Journal():
    tracker = JournalTracker()
    operation = ''

    while (operation != 5):
        Clear_Screen()
        print("Welcome to Journal!")
        tracker.display_journals()
        print("What would you like to do today?")
        print("Task Commands: ")
        print("1. Write a new journal")
        print("2. Read your old journal")
        print("3. Delete your old journal")
        print("4. Edit your old journal")
        print("5. Back to menu")
        operation = int(input("Input : "))

        if operation == 1:
            Clear_Screen()

            print("Please enter the journal details!")
            title = input("Journal title : ")                
            entry = input("New entry : ")

            tracker.add_journal(title, entry)
            tracker.save_journals()
            Clear_Screen()
        elif operation == 2:
            Clear_Screen()

            journal_count = tracker.count()

            if (journal_count <= 0):
                input("There are no journal available!")
                Journal()

            success = False
            
            while not success:
                index = int(input("Journal number : "))
                if (index > 0) and (index <= journal_count):
                    success = True
                else:
                    print(f"Please pick a number between 1 and {journal_count}!")

            Clear_Screen()
            tracker.read_journal(index - 1)
        elif operation == 3:
            Clear_Screen()

            journal_count = tracker.count()

            if (journal_count <= 0):
                input("There are no journal available!")
                Journal()

            success = False
            
            while not success:
                index = int(input("Journal number : "))
                if (index > 0) and (index <= journal_count):
                    success = True
                else:
                    print(f"Please pick a number between 1 and {journal_count}!")

            Clear_Screen()
            tracker.delete_journal(index - 1)
        elif operation == 4:
            Clear_Screen()

            journal_count = tracker.count()

            if (journal_count <= 0):
                input("There are no journal available!")
                Journal()

            success = False
            
            while not success:
                index = int(input("Journal number : "))
                if (index > 0) and (index <= journal_count):
                    success = True
                else:
                    print(f"Please pick a number between 1 and {journal_count}!")

            Clear_Screen()
            tracker.edit_journal(index - 1)

    from menu import Menu
    Menu()
    return