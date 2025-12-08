import os

def Clear_Screen():
    #Windows
    if os.name == 'nt':
        os.system('cls')
    #MacOS/Linux (Replit pakai linux)
    #os.system('clear')