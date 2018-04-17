try:

    print("Importing modules... [os,re,time,random,sys,pip,colorama]")

    import os, re, time, random, sys, pip, colorama
    from stat import * # ST_SIZE etc
    from colorama import Fore, Style, init
    init()

    print("Imported modules")
    time.sleep(3)
    os.system("cls")
    print()

except ImportError:
    print("An error occured while inporting a module. Ensure that the colorama module is installed, otherwise install the provided .whl file with the following command from a CMD Prompt:")
    print("python -m pipinstall colorama - install using a wheel file")
    print("Would you like to install colorama from the internet? (y/n)")

    install = input(">>")
    if install == "y":
        pip.main(['install', 'colorama'])

# python -m pip install colorama - install using a wheel file
# pip3.6 install --user colorama - install online

def main():

    username = input("Enter your username: ")
    password = eval(input("Enter your password: "))

    if username == "Patrick" and password == 24:
            print()
            print("Welcome: ", username)
            print("The secret code is:", random.randint(0, 100))
            commands()
    else:
        denied()

def commands():

    print("Type a command. Type 'help' for help.")

    print()

    directory = os.getcwd()
    command = input(directory + ">>")

    dir_ectory = str.strip(re.sub('cd', '', command))
    changeDir = str.strip(re.sub(dir_ectory, '', command))

    if command == "dir":
        dir(directory)
    elif command == "cls" or command == "clear":
        clear()
    elif command == "exit":
        print()
    elif command == "help":
        help()
    elif command == "ver":
        ver()
    elif changeDir == "cd" or changeDir == "" or changeDir == "." or changeDir == "cd/" or changeDir == "/":
        cd(dir_ectory)
    else:
        print(command, "is an unknown internal/external command, program, or script.")
        commands()

def cd(path):

    try:
        os.chdir(path)
    except OSError:
        print()
        print(Fore.RED + 'PATH', Style.RESET_ALL + path, Fore.RED + 'NOT FOUND. PLEASE TRY AGAIN')
        print(Style.RESET_ALL)

    commands()

def clear():

    os.system("cls")
    commands()

def dir(DIR):

    sizes = ["BT", "KB", "MB", "GB", "TB"]

    print("Directory of", DIR)
    print()
    print("DOW = Day of Week    MON = Month    DY = Day    HR = Hour    SC = Second    MS = Millisecond    BT = Bytes")
    print()

    print("SIZE | DOW MON DY HR:SC:MS YEAR |  DIR  | FILE / DIR NAME")
    print()

    for i in os.listdir('.'):
        try:
            st = os.stat(i)
        except IOError:
            print("Failed to get information about", i)
        else:

            num = int(st[ST_SIZE])

            size = 0
            space = 0
            kind = 0

            if os.path.isdir(i):
                for (path, dirs, files) in os.walk(i):
                    for file in files:

                        filename = os.path.join(path, file)
                        num += os.path.getsize(filename)
                        kind = 0
            else:
                kind = 1

            while num > 1024.0:

                num = num / 1024.0
                size = size + 1

            if type(num) != float:
                num = num + .0

            num = round(num, 1)
            length = len(str(abs(num)))

            if length < 7:

                if length == 6:
                    space = 0
                elif length == 5:
                    space = 1
                elif length == 4:
                    space = 2
                elif length == 3:
                    space = 3

            if kind == 0 & length < 7:
                print(" " * space, num, sizes[size], "|", time.asctime(time.localtime(st[ST_MTIME])), "| <DIR> |", i)
            elif kind == 1 & length < 7:
                print(" " * space, num, sizes[size], "|", time.asctime(time.localtime(st[ST_MTIME])), "|       |", i)
            elif kind == 0 & length > 6:
                print(num, sizes[size], "|", time.asctime(time.localtime(st[ST_MTIME])), "| <DIR> |", i)
            elif kind == 1 & length > 6:
                print(num, sizes[size], "|", time.asctime(time.localtime(st[ST_MTIME])), "|       |", i)

    commands()

def help():

    print()
    print("Here is a list of acceptable commands:")
    print()
    print("CD 'PATH'    Change directory to the specified PATH.")
    print("CLS          Clears the screen.")
    print("DIR          Lists files or folders in the current directory.")
    print("EXIT         Exits the terminal.")
    print("VER          Displays the terminal version.")
    print()
    commands()

def ver():

    print()
    print("fakeTerminal v1.3. Created by Jose Marquez in Python 3.6.1 at RHS. (3.6.5 or the latest version, if I'm coding at home)")
    print("New in this version:")
    print()
    print("1. Added code to calculate folder sizes via recursion.")
    print("2. Moved some bits of code")
    print(Fore.WHITE + '3. Added a cd function - Includes "cd .. and cd /"' + Fore.RED + ' SWITCHING TO FOLDERS IS BROKEN FOR SOME REASON BUT GOING BACK A FOLDER WORKS')
    print(Style.RESET_ALL)
    print()
    print("I encourage you to edit/improve this program.")
    print("Don't sell it though. I mean there's not much so why would anyone buy it.")
    print()
    commands()

def denied():

    print("ACCESS DENIED!")

if __name__ == "__main__":
    main()