import time
import random
from clear_Screen import Clear_Screen


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
                Clear_Screen()
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
                looper = True
                while looper:
                    Clear_Screen()
                    print("Timer paused")
                    print("What would you like to do?")
                    print("1. Continue timer")
                    print("2. Stop timer")
                    operation = str(input("Input: "))
                    if(operation == "1"):
                        print("Timer will continue!")
                        time.sleep(1)
                        looper = False
                    else:
                        timer()

    def focusMode(self, message, increment, mode):
        mode = f"[FOCUS MODE]: Session {increment + 1}"
        self.countdown(message, mode)
        Clear_Screen()
        print(mode)
        Timer.displayTimer(0)
        time.sleep(1)
        print("You did it! Take a proper break!")
        time.sleep(3)

    def breakMode(self, message, increment, session, mode):
        mode = f"[BREAK MODE]: Session {increment + 1}"
        self.countdown(message, mode)
        Clear_Screen()
        print(mode)
        Timer.displayTimer(0)
        time.sleep(1)
        if (increment != session - 1):
            print("Go back to your work!")
        else:
            print("Congratulations! Now, take a long rest!")
        time.sleep(3)


def timer():
    Clear_Screen()
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
            Clear_Screen()
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
                Clear_Screen()
                timer()
            else:
                timer()
        elif (operation == 2):
            time_in_sec = 50 * 60
            Clear_Screen()
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
                Clear_Screen()
                timer()
            else:
                timer()
        elif (operation == 3):
            Clear_Screen()
            print("[FOCUS MODE]")
            time_focus_string = str(input("Insert focus time (minute:second): "))
            time_focus_array = time_focus_string.split(":")
            time_focus = int(time_focus_array[0]) * 60 + int(time_focus_array[1])

            time_break_string = str(input("Insert break time (minute:second): "))
            time_break_array = time_break_string.split(":")
            time_break = int(time_break_array[0]) * 60 + int(time_break_array[1])

            session = int(input("Insert session: "))

            Clear_Screen()
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
                Clear_Screen()
                timer()
            else:
                timer()
    from menu import Menu
    Menu()
    return