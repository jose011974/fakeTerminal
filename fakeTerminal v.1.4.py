try:

    print("Importing modules... [os,re,time,sys,stat,colorama]")

    import os, re, time, sys, colorama
    from stat import ST_SIZE, ST_MTIME
    from colorama import Fore, Back, Style, init
    init()

    print("Imported modules")
    time.sleep(3)

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print()

except ImportError:

    Continue = False

    print("An error occured while inporting a module. Please make sure the modules: os, re, time, random, sys, stat, pip, and colorama are installed.")
    print("If not, use the provided *.whl files and use 'python -m pip install name.whl' from a Windows Command Prompt or Linux Terminal.")
    print("Continued use may result in a crash. Type 'OK' to continue.")
    print()

    while Continue == False:
        userInput = input(">>")

        if userInput != "OK":
            print("Please type OK and press enter to continue!")
        else:
            Continue = True

# python -m pip install colorama - install using a wheel file
# pip3.6 install --user colorama - install online

def cd(path):

    try:
        os.chdir(path)
    except OSError:
        print()
        print(Fore.RED + 'PATH', Style.RESET_ALL + path, Fore.RED + 'NOT FOUND. PLEASE TRY AGAIN')
        print(Style.RESET_ALL)

def clear():

    os.system("clear")

def commands():

    print()
    print("Type a command. Type 'help' for help.")
    print()

    directory = os.getcwd()
    command = input(directory + ">>")
    
    command = command.lower()

    dir_ectory = str.strip(re.sub('cd', '', command))
    changeDir = str.strip(re.sub(dir_ectory, '', command))

    if command == "dir":
        dir(directory)
    elif command == "cls" or command == "clear":
        clear()
    elif command == "exit":
        sys.exit()
    elif command == "help":
        help()
    elif command == "game" or command == "games":
        game()
    elif command == "ver":
        ver()
    elif changeDir == "cd" or changeDir == "" or changeDir == "." or changeDir == "cd/" or changeDir == "/":
        cd(dir_ectory)
    else:
        print(command, "is an unknown internal/external command, program, or script.")

def dir(DIR):

    print("Directory of", DIR)
    print()
    print("DOW = Day of Week    MON = Month    DY = Day    HR = Hour    SC = Second    MS = Millisecond")
    print()
    print("BT = Bytes    KB = Kilobytes    MB = Mebagytes    GB = Gigabytes    TB = Terabytes")
    print()
    print("      SIZE | DOW MON DY HR:SC:MS YEAR |  DIR  | FILE / DIR NAME")
    print()

    listDir()

def exception_handler(exception_type, exception, traceback):

    if exception_type.__name__ == "KeyboardInterrupt":
        print()
        print()
        print(Fore.RED + 'Error: The user has manually interrupted the program')
    else:
        print("%s: %s" % (exception_type.__name__, exception))


def fileLength(fileName, fileSize, fileType, fileSizeType):

    st = os.stat(fileName)
    sizes = ["BT", "KB", "MB", "GB", "TB"]
    length = len(str(abs(fileSize)))

    if length < 7:

        if length == 6:
            space = 0
        elif length == 5:
            space = 1
        elif length == 4:
            space = 2
        elif length == 3:
            space = 3

    try:

        if fileType == 0 & length < 7:
            print(" " * space, fileSize, sizes[fileSizeType], "|", time.asctime(time.localtime(st[ST_MTIME])), "| <DIR> |", fileName)
        elif fileType == 1 & length < 7:
            print(" " * space, fileSize, sizes[fileSizeType], "|", time.asctime(time.localtime(st[ST_MTIME])), "|       |", fileName)
        elif fileType == 0 & length > 6:
            print(fileSize, sizes[fileSizeType], "|", time.asctime(time.localtime(st[ST_MTIME])), "| <DIR> |", fileName)
        elif fileType == 1 & length > 6:
            print(fileSize, sizes[fileSizeType], "|", time.asctime(time.localtime(st[ST_MTIME])), "|       |", fileName)

    except FileNotFoundError:

        print("Unable to get information on", fileName)

def help():

    print()
    print("Here is a list of acceptable commands:")
    print()
    print("CD 'PATH'    Change directory to the specified PATH.")
    print("CLS          Clears the screen.")
    print("DIR          Lists files or folders in the current directory.")
    print("EXIT         Exits the terminal.")
    print("GAME         Lists the avaliable games.")
    print("VER          Displays the terminal version.")
    print()

def listDir():

    for filename in os.listdir('.'):
        try:
            st = os.stat(filename)
        except IOError:
            print("Failed to get information about", filename)
        else:

            num = int(st[ST_SIZE])
            size = 0
            kind = 0

            if os.path.isdir(filename):
                for (path, dirs, files) in os.walk(filename):
                    for file in files:

                        nameDir = filename
                        filename = os.path.join(path, file)
                        num += os.path.getsize(filename)
                        kind = 0
                        filename = nameDir

            else:
                kind = 1

            while num > 1024.0:

                num = num / 1024.0
                size = size + 1

            if type(num) != float:
                num = num + .0

            num = round(num, 1)

            fileLength(filename, num, kind, size)
            
def game():

    print("Games comming soon!")

def ver():

    print()
    print("fakeTerminal v1.4. Created by Jose Marquez in Python 3.6.1 at RHS. (3.6.5 or the latest version, if I'm coding at home)")
    print("New in this version:")
    print()
    print(Fore.WHITE + Back.BLUE + '1. Reworked my code using tips from my CompSci class')
    print('2. CD command is still somewhat broken')
    print('3. Removed the login feature since I do not want to go through hell in figuring out how to save "user profiles" in python. It was pointless anyway, since the idea of people logging into a terminal seemed cool when I started to make this.')
    print('4. Fixed a bug that printed the name of a subdirectory in the directory listing')
    print('5. Added some placeholder code for upcoming games (Not sure what kind however.)')
    print(Style.RESET_ALL)
    print("I encourage you to edit/improve this program.")
    print("Don't sell it though. I mean there's not much so why would anyone buy it.")

def main():

    sys.excepthook = exception_handler

    while __name__ == "__main__":
        commands()

if __name__ == "__main__":
    main()