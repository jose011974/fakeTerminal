import os, time, random, sys
from stat import * # ST_SIZE etc

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
        print("SIZE OF DIRECTORIES IS BROKEN UNTILL I FIND A SOLUTION")
        print("Directory of", directory)
        print()
        print("DOW = Day of Week    MON = Month    DY = Day    HR = Hour    SC = Second    MS = Millisecond")
        print()
        
        print("SIZE | DOW MON DY HR:SC:MS YEAR |  DIR  | FILE / DIR NAME")
        print()
        
        fileSize()
        
        print("SIZE OF DIRECTORIES IS BROKEN UNTILL I FIND A SOLUTION")
        print()
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
        print("fakeTerminal v1.0. Created by Jose Marquez in Python 3.6.1.")
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
            
        try:
            st = os.stat(i)
        except IOError:
            print("Failed to get information about", file)
        else:
            size = int(st[ST_SIZE])
            
            while size > 1024:
            
                size = size / 1024
                size = round(size, 2)
                
            if os.path.isdir(i):
                print(size, "KB |", time.asctime(time.localtime(st[ST_MTIME])), "| <DIR> |", i)
            else:
                print(size, "KB |", time.asctime(time.localtime(st[ST_MTIME])), "|       |", i)
    
main()