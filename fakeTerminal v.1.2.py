try:

    print("Importing modules... [os,time,random,sys,pip,colorama]")
    
    import os, time, random, sys, pip, colorama
    from stat import * # ST_SIZE etc
    from colorama import Fore, Style, init
    init()

    print("Imported modules")
    time.sleep(3)
    os.system("cls")
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

        fileSize()
    elif command == "help":
        help()
    elif command == "cls" or command == "clear":
        clear()
    elif command == "exit":
        print()
    elif command == "ver":
        ver()
    else:
        print(command, "is an unknown internal/external command, program, or script.")
        commands()

def clear():

    os.system("cls")
    commands()
    
def help():
    print()
    print("Here is a list of acceptable commands:")
    print()
    print("DIR      Lists files or folders in the current directory.")
    print("CLS      Clears the screen.")
    print("EXIT     Exits the terminal.")
    print("VER      Displays the terminal version.")
    print()
    commands()
    
def ver():

    print()
    print("fakeTerminal v1.2. Created by Jose Marquez in Python 3.6.1.")
    print("New in this version: Updated code for calculating file size, folder sizes still broken...")
    print("I encourage you to edit this program.")
    print()
    commands()

def fileSize():

    print()
    print(Fore.RED + '----------------------------------------------------------------')
    print(Fore.RED + 'CALCULATING SIZES OF FOLDERS IS BROKEN UNTILL I IMPROVE THE CODE')
    print(Fore.RED + '----------------------------------------------------------------')
    print(Style.RESET_ALL)
    print("Directory of", directory)
    print()
    print("DOW = Day of Week    MON = Month    DY = Day    HR = Hour    SC = Second    MS = Millisecond    BT = Bytes")
    print()

    print("SIZE | DOW MON DY HR:SC:MS YEAR |  DIR  | FILE / DIR NAME")
    print()
    
    for i in os.listdir('.'):
        try:
            st = os.stat(i)
        except IOError:
            print("Failed to get information about", file)
        else:
            num = int(st[ST_SIZE])
            size = 0
            
            while num > 1024.0:
            
                num = num % 1024.0
                size = size + 1
                
            if num == 0:
                num = "ERROR"
                
            sizes = ["BT", "KB", "MB", "GB", "TB"]
    
            if os.path.isdir(i):
                print(num, sizes[size], "|", time.asctime(time.localtime(st[ST_MTIME])), "| <DIR> |", i)
            else:
                print(num, sizes[size], "|", time.asctime(time.localtime(st[ST_MTIME])), "|       |", i) 
                
    print()
    print(Fore.RED + '----------------------------------------------------------------')
    print(Fore.RED + 'CALCULATING SIZES OF FOLDERS IS BROKEN UNTILL I IMPROVE THE CODE')
    print(Fore.RED + '----------------------------------------------------------------')
    print(Style.RESET_ALL)

    commands()
    
def denied():

    print("ACCESS DENIED!")
    
main()