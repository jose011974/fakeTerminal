import os, time, random, sys, pip
from stat import * # ST_SIZE etc

try:
    import colorama
    from colorama import Fore, Style, init
    init()

    print("Colorama was imported.")
    print()
    time.sleep(1)

except ImportError:
    print("Would you like to install colorama? (y/n)")
    install = input(">>")
    if install == "y":
        pip.main(['install', 'colorama'])

# python -m pip install colorama
# pip3.6 install --user colorama

directory = os.getcwd()

def main():

    username = input("Enter your username: ")
    password = eval(input("Enter your password: "))

    if username == "Patrick":
        if password == 24:
            print()
            print("Welcome: ", username)
            print("The secret code is:", random.randint(0, 100))
            commands()
        else:
            denied()
    elif username == "dev" or username == "Dev":
        commands()
    else:
        denied()

def commands():

    print("Type a command. Type 'help' for help.")

    print()

    command = input(directory + ">>")

    if command == "dir":

        print()
        print(Fore.RED + '-----------------------------------------------------')
        print(Fore.RED + 'CALCULATING SIZES IS BROKEN UNTILL I IMPROVE THE CODE')
        print(Fore.RED + '-----------------------------------------------------')
        print(Style.RESET_ALL)
        print("Directory of", directory)
        print()
        print("DOW = Day of Week    MON = Month    DY = Day    HR = Hour    SC = Second    MS = Millisecond")
        print()

        print("SIZE | DOW MON DY HR:SC:MS YEAR |  DIR  | FILE / DIR NAME")
        print()

        fileSize()

        print()

        print(Fore.RED + '-----------------------------------------------------')
        print(Fore.RED + 'CALCULATING SIZES IS BROKEN UNTILL I IMPROVE THE CODE')
        print(Fore.RED + '-----------------------------------------------------')
        print(Style.RESET_ALL)

        commands()
    elif command == "help":
        print()
        print("Here is a list of acceptable commands:")
        print()
        print("DIR      Lists files or folders in the current directory.")
        print("CLS      Clears the screen.")
        print("EXIT     Exits the terminal.")
        print("VER      Displays the terminal version.")
        print()
        commands()
    elif command == "cls" or command == "clear":
        clear()
    elif command == "exit":
        print()
    elif command == "ver":
        print()
        print("fakeTerminal v1.1. Created by Jose Marquez in Python 3.6.1.")
        print("I encourage you to edit this program.")
        print()
        commands()
    else:
        print(command, "is an unknown internal/external command, program, or script.")
        commands()

def clear():

    os.system("cls")
    commands()

def denied():

    print("ACCESS DENIED!")

def fileSize():
    
    for i in os.listdir('.'):
    
        if os.path.isdir(i):
            print(file_size(i), "|", time.asctime(time.localtime(st[ST_MTIME])), "| <DIR> |", i)
        else:
            print(file_size(i), "|", time.asctime(time.localtime(st[ST_MTIME])), "|       |", i) 
  
def convert_bytes(num):

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):

    if os.path.isfile(file_path):
    
        try:
            st = os.stat(i)
        except IOError:
            print("Failed to get information about", file)
        else:
            return convert_bytes(file_info.st_size) 
            
main()