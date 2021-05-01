import os
from time import *
from pygame import mixer


mixer.init()

with open("user_file.txt") as f:
    users = {}
    for line in f:
        x = line.split("-")
        a = x[0]
        b = x[1]
        c = len(b) - 1
        b = b[0:c]
        users[a] = b

def menu(user_input):
    if user_input == "l":
        olduser_login()
    elif user_input == "r":
        newuser_register()
    elif user_input == 'q':
        return exit()
def olduser_login():
    while 1:
        global username
        username = input("Username :")
        if username.isalnum() == False:
            print("Invalid Username. (Do not give spaces)\n")
            continue
        global password
        password = input("Password :")
        if confirm_input() == "n":
            continue
        if username in users and users[username] == password:
            print("\nLogin Successfull.")
            print("Welcome " + username.upper())
            break
        else:
            print("\nUser don't exist or wrong password.")
            break
def newuser_register():
    while 1:
        global username
        username = input("Username :")
        if username.isalnum() == False:
            print("Invalid Username. (Do not give spaces)\n")
            continue
        global password
        password = input("Password :")
        if confirm_input() == "n":
            continue
        if username in users:
            print("\nUsername already taken. Try again.\n")
            continue
        users[username] = password
        with open("user_file.txt", "a") as f:
            f.write(username + "-" + password + "\n")
        print("Successfully Registered.\nHello " + username.upper() + ". \n" +
              "I am Elena, your Daily Health Assitant\n" +
              "If you are living a sedentary lifestyle, then in such case i might can help you." +
              "\nTell me your working hrs schedule and i'll be assisting you in such a way that your health doesn't get compromised." +
              "\nI'll be monitoring your - 'Water Drinking','Eyes Resting' & 'Physical Exe'" +
              " Activities during the day.")
        break
def confirm_input():
    confirm = input("Confirm? (y/n) : ")
    if confirm == "y":
        return 0
    elif confirm == "n":
        return "n"
    else:
        print("Wrong Input.")
        return confirm_input()


From = "0800PM" #default work starting time
To = "0900PM"   #default work ending time
tfrom = strptime(From, "%I%M%p")
tto = strptime(To, "%I%M%p")
def custom_fromto():
    while 1:
        global From, To, tfrom, tto
        print("(write in this format = hhmmam/pm\nFrom : ", end=" ")
        From = input()
        print("To : ", end=" ")
        To = input()
        if confirm_input() == "n":
            continue
        tfrom = strptime(From, "%I%M%p")
        tto = strptime(To, "%I%M%p")
        break
def isofficetime(current_time):
    if current_time > strftime("%H%M%S", tfrom) and current_time < strftime("%H%M%S", tto):
        return True
    else:
        print(f"Wokring Time over {username.upper()}.\nGoodluck for rest of the day.\nMeet you soon.")
        return False

total_water = 3500  # total water(mL) to drink per day
water_afterevery = 1200  # in-seconds(20mins)
eyes_afterevery = 1800  # in-seconds(30mins)
exe_afterevery = 2700  # in-seconds(45mins)

current_time = strftime("%H%M%S")
water_takenat = time()
eyes_restat = time()
phy_exeat = time()

def water():
    mixer.music.load("water.mp3")
    mixer.music.set_volume(1)
    mixer.music.play(loops=-1)
    print(f"Water Amount to consume - 175mL/reminder,({total_water}mL left for a day)")
    while 1:
        revert = input("Type:\n'Drank' when done.\n'p' to Pause.\n>>>")
        if revert == "Drank":
            mixer.music.stop()
            break
        elif revert == 'p':
            mixer.music.pause()
            continue
        else:
            print("Type Error! Try Again...")
            continue
    file = username + "waterlog.txt"
    if os.path.exists(file):
        with open(file, "a") as f:
            f.writelines(strftime("%a %dth %b %Y, %I:%M:%S %p", localtime()))
            f.writelines("\t")
            f.writelines("WATER CHECK\n")
    else:
        with open(file, "w") as f:
            f.writelines(username.upper() + "'s Water Log\n")
            f.writelines("TIME\tSTATUS\n")
            f.writelines(strftime("%a %dth %b %Y, %I:%M:%S %p", localtime()))
            f.writelines("\t")
            f.writelines("WATER CHECK\n")
def eyes():
    mixer.music.load("eyes.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(loops=-1)
    while 1:
        revert = input("Type:\n'EyDone' when done.\n'p' to Pause.\n>>>")
        if revert == "EyDone":
            mixer.music.stop()
            break
        elif revert == 'p':
            mixer.music.pause()
            continue
        else:
            print("Type Error! Try Again...")
            continue
    file = username + "eyeslog.txt"
    if os.path.exists(file):
        with open(file, "a") as f:
            f.writelines(strftime("%a %dth %b %Y, %I:%M:%S %p", localtime()))
            f.writelines("\t")
            f.writelines("EYES CHECK\n")
    else:
        with open(file, "w") as f:
            f.writelines(username.upper() + "'s Eyes Log\n")
            f.writelines("TIME\tSTATUS\n")
            f.writelines(strftime("%a %dth %b %Y, %I:%M:%S %p", localtime()))
            f.writelines("\t")
            f.writelines("EYES CHECK\n")
def exe():
    mixer.music.load("exe.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play(loops=-1)
    while 1:
        revert = input("Type:\n'ExDone' when done.\n'p' to Pause.\n>>>")
        if revert == "ExDone":
            mixer.music.stop()
            break
        elif revert == 'p':
            mixer.music.pause()
            continue
        else:
            print("Type Error! Try Again...")
            continue
    file = username + "exelog.txt"
    if os.path.exists(file):
        with open(file, "a") as f:
            f.writelines(strftime("%a %dth %b %Y, %I:%M:%S %p", localtime()))
            f.writelines("\t")
            f.writelines("EXE CHECK\n")
    else:
        with open(file, "w") as f:
            f.writelines(username.upper() + "'s Exe Log\n")
            f.writelines("TIME\tSTATUS\n")
            f.writelines(strftime("%a %dth %b %Y, %I:%M:%S %p", localtime()))
            f.writelines("\t")
            f.writelines("EXE CHECK\n")


if __name__ == '__main__':
    print("----------HEALTHY PROGRAMMER-----------")
    username = ""
    password = ""
    while 1:
        user_input = input("\t\t\tl : Login\n\t\t\tr : Register\n\t\t\t(q-quit)\n>>> ")
        if user_input == 'l' or user_input == 'r' or user_input == 'q':
            menu(user_input)
            print("Your working time is scheduled for - " + strftime("%I:%M:%S %p", tfrom) + " to " + strftime(
                "%I:%M:%S %p",
                tto))
            print("Are you ok with timing?")
            while confirm_input() == 'n':
                custom_fromto()
                print(
                    "Your new working time is scheduled for - " + strftime("%I:%M:%S %p", tfrom) + " to " + strftime(
                        "%I:%M:%S %p",
                        tto))
            while (isofficetime(current_time)):
                if (time() - water_takenat) > water_afterevery:
                    water()
                    water_takenat = time()
                    total_water -= 175
                if (time() - eyes_restat) > exe_afterevery:
                    eyes()
                    eyes_restat = time()
                if (time() - phy_exeat) > exe_afterevery:
                    exe()
                    phy_exeat = time()

            isofficetime(current_time)
            break
        else:
            print("Error! Wrong Input. Try Again")
            continue













