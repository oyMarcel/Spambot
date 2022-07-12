from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

author = "oyMarcel"
version = "Build 1.2"
name = "SpamBot"



def simpleMain():
    cmd = input("> ")

    if cmd == "about":
        print("Made by oyMarcel")
        print("Made to spam!")
        simpleMain()
    

    elif cmd == "spam":
        print("Type the word you desire to spam")
        word = input()
        print("Type 'confirm' to confirm you want to spam or type 'exit' to exit")
        confirm = input()
        if confirm == "confirm":
            print("The word " + word + " will be spammed shortly")
            time.sleep(3)
            cnt = 0
            while cnt < 100:
                keyboard.type(word)
                time.sleep(0.3)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                cnt = cnt + 1
            print("The current assigment was finished sucsessfully")
            simpleMain()

        if confirm == "exit":
            quitProgram()
        


    elif cmd == "exit":
        quitProgram()

    elif cmd == "help":
        print("'spam' - spams your desired word")
        print("'exit' - quits the program")
        print("'about' - see details about this program")
        print("'help' - displays this screen")
        simpleMain()
        
        
    else:
        print("'" + cmd + "'" + " is not recognized as an valid commamd ")
        simpleMain()

def quitProgram():
    print("Bye!")
    time.sleep(1)
    exit(0)


print(name + " by " + author + " " + version)
time.sleep(0.5)
simpleMain()



