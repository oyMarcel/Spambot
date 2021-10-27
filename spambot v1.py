from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
cnt = 0
author = "oyMarcel"
version = "Build 1"
name = "SpamBot"

print(name + " by " + author + " " + version)
time.sleep(0.5)
print("Use 'spam' to start spamming and use 'about' for more info or type 'exit' to exit")
cmmd = input()

if cmmd == "about":
    print("Made by oyMarcel")
    print("Made to spam!")
    time.sleep(4)
    print("To exit type 'exit'")
    close = input()
    if close == "exit":
        print("Bye!")
        time.sleep(1)
        exit(0)
    

elif cmmd == "spam":
    print("Type the word you desire to spam")
    word = input()
    print("Type 'confirm' to confirm you want to spam or type 'exit' to exit")
    confirm = input()
    if confirm == "confirm":
        print("The word " + word + " will be spammed shortly")
        time.sleep(3)
        while cnt < 100:
            keyboard.type(word)
            time.sleep(0.3)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            cnt = cnt + 1


    if confirm == "exit":
        print("Bye!")
        time.sleep(1)
        exit(0)


elif cmmd == "exit":
    print("Bye!")
    time.sleep(1)
    exit(0)

    
else:
    print("Please use an valid command, restart the program")
    time.sleep(1)
    exit(0)
