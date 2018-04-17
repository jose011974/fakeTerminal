import os, time, random
from stat import * # ST_SIZE etc

directory = os.getcwd()

def main():

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "Patrick":
        if password == "24":
            print()
            print("Welcome: ", username)
            print("The secret code is:", random.randint(1, 100))
            commands()
        else:
            denied()
            
    else:
        denied()

def commands():

    print("Type a command. Type 'help' for help.")
    
    print()
    
    command = input(directory + ">>")
    
    if command == "dir":
    
        print()
        print("Directory of", directory)
    
        print()
        for i in os.listdir('.'):
        
            try:
                st = os.stat(i)
            except IOError:
                print("Failed to get information about", file)
            else:
                print(int(st[ST_SIZE] / 1024, ), "KB |", time.asctime(time.localtime(st[ST_MTIME])), "|", i)
                
        print()
        commands()
    elif command == "help":
        print()
        print("Here is a list of acceptable commands:")
        print()
        print("DIR          Lists files or folders in the current directory.")
        print("CLS          Clears the screen.")
        print("EXIT         Exit.")
        print()
        commands()
    elif command == "cls" or command == "clear":
        print("23")
        clear()
    elif command == "exit":
        exit()
    else:
        print(command, "is an unknown internal/external command, program, or script.")
        commands()
        
def clear():
    os.system("cls")
    commands()
    
def exit():
    os.exit()
    
def denied():
    print("ACCESS DENIED!")
    
main()