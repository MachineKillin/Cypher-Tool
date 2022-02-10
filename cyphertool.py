import os, time, ctypes, hashlib, os.path, tkinter, os.path, requests
from tracemalloc import reset_peak
from flask import session
from colorama import Fore, init
import os
import time
root = tkinter.Tk()
root.withdraw()
proxylist = []
self = []
session = requests.Session()
session.trust_env = False
init()
blue, red, white, green, cyan, lightblue, reset = Fore.BLUE, Fore.RED, Fore.WHITE, Fore.GREEN, Fore.CYAN, Fore.LIGHTBLUE_EX, Fore.RESET

def github(line):
    global taken
    global available
    global total
    try:
        url = f"https://github.com/{line}"
        r = requests.get(url)
        if r.status_code == 200:
            print("{}The username {} is taken!{}".format(red, line, reset))
            time.sleep(4)
            name_check()
        else:
            print("{}The username {} is avalible!{}".format(green, line, reset))
            time.sleep(5)
            name_check()
    except Exception:
        print("{}Failed!{}".format(red, reset))
        time.sleep(3)
        name_check()

def tiktok(line):
    os.system('cls')
    global taken
    global available
    global total
    try:
        url = f"https://www.tiktok.com/@{line}?"
        r = requests.get(url)

        if r.status_code == 200:
            print("{}The username {} is taken!{}".format(red, line, reset))
            time.sleep(4)
            name_check()
        else:
            print("{}The username {} is avalible!{}".format(green, line, reset))
            time.sleep(5)
            name_check()
    except Exception:
        print("{}Failed!{}".format(red, reset))
        time.sleep(3)
        name_check()
    
def instagram(line):
    os.system('cls')
    global taken
    global available
    global total
    try:
        url = f"https://www.instagram.com/{line}/"
        r = requests.get(url)

        if r.status_code == 200:
            print("{}The username {} is taken!{}".format(red, line, reset))
            time.sleep(4)
            name_check()
        else:
            print("{}The username {} is avalible!{}".format(green, line, reset))
            time.sleep(5)
            name_check()
    except Exception:
        print("{}Failed!{}".format(red, reset))
        time.sleep(3)
        name_check()

def linktree(line):
    os.system('cls')    
    global taken
    global available
    global total
    try:
        url = f"https://linktr.ee/{line}"
        r = requests.get(url)

        if r.status_code == 200:
            print("{}The username {} is taken!{}".format(red, line, reset))
            time.sleep(4)
            name_check()
        else:
            print("{}The username {} is avalible!{}".format(green, line, reset))
            time.sleep(5)
            name_check()
    except Exception:
        print("{}Failed!{}".format(red, reset))
        time.sleep(3)
        name_check()


def cracked(line):
    os.system('cls')
    global taken
    global available
    global total
    try:
        url = f"https://cracked.io/{line}"
        r = requests.get(url)

        if r.status_code == 200:
            print("{}The username {} is taken!{}".format(red, line, reset))
            time.sleep(4)
            name_check()
        else:
            print("{}The username {} is avalible!{}".format(green, line, reset))
            time.sleep(5)
            name_check()
    except Exception:
        print("{}Failed!{}".format(red, reset))
        time.sleep(3)
        name_check()

def minecraft(line):
    os.system('cls')
    global taken
    global available
    global total
    try:
        url = f"https://api.mojang.com/users/profiles/minecraft/{line}"
        r = requests.get(url)

        if r.status_code == 200:
            print("{}The username {} is taken!{}".format(red, line, reset))
            time.sleep(4)
            name_check()
        else:
            print("{}The username {} is avalible!{}".format(green, line, reset))
            time.sleep(5)
            name_check()
    except Exception:
        print("{}Failed!{}".format(red, reset))
        time.sleep(3)
        name_check()

def name_check():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Username Checker")
    print("""  {}Pick a Choice:      [0 to leave]{}
        ╔══════════════════╦══════════════════╗
        ║ {}1. Minecraft{}     ║ {}2. Cracked.io{}    ║
        ║                  ║                  ║
        ║ {}3. linktree      {}║ {}4. Instagram {}    ║
        ║                  ║                  ║
        ║ {}5. Tiktok {}       ║ {}6. Github    {}    ║
        ╚══════════════════╩══════════════════╝{}""".format(lightblue, cyan, lightblue, cyan, lightblue, cyan, lightblue, cyan, lightblue, cyan, lightblue, cyan, lightblue, cyan, lightblue, cyan))
    try:
        question = int(input(""))
    except Exception:
        print("{}Invalid input{}".format(red, red))
        time.sleep(2)
        main()
    if  question == 0:
        main()
    if question == 1:
        os.system('cls')
        print("    {}[1] Minecraft{}".format(lightblue, reset))
        print("{}What name do you want to check?{}".format(cyan, reset))
        line = input("")
        minecraft(line)
    elif question == 2:
        os.system('cls')
        print("    {}[2] Cracked.to{}".format(lightblue, reset))
        print("{}What name do you want to check?{}".format(cyan, reset))
        line = input("")
        cracked(line)
    elif question == 3:
        os.system('cls')
        print("    {}[3] Linktree{}".format(lightblue, reset))
        print("{}What name do you want to check?{}".format(cyan, reset))
        line = input("")
        linktree(line)
    elif question == 4:
        os.system('cls')
        print("    {}[4] Instagram{}".format(lightblue, reset))
        print("{}What name do you want to check?{}".format(cyan, reset))
        line = input("")
        instagram(line)
    elif question == 5:
        os.system('cls')
        print("    {}[5] TTikTok{}".format(lightblue, reset))
        print("{}What name do you want to check?{}".format(cyan, reset))
        line = input("")
        tiktok(line)
    elif question == 6:
        os.system('cls')
        print("    {}[6] GitHub{}".format(lightblue, reset))
        print("{}What name do you want to check?{}".format(cyan, reset))
        line = input("")
        github(line)
def single_check():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Single Combo Checker")
    print("{}   Coded by KillinMachine#0001{}". format(cyan, reset))
    print("     Please Paste Your Combo: ")
    combo = (input(""))
    username = combo.split(":")[0]
    password = combo.split(":")[1]
    time.sleep(2)
    try:
        json = {"agent":{"name": "Minecraft", "version": 1},'clientToken':"fff","password": password,"requestUser": "true", "username": username}
        check = session.get("https://authserver.mojang.com/authenticate", json = json, headers = {"User-Agent": "MinecraftLauncher/1.0"})
        if "clientToken" in check.text:
            print("{}The account {}:{} is Valid!{}".format(green, username, password, reset))
            time.sleep(10)
            main()
        elif "legacy\":true" in check.text:
            print("{}The account {}:{} is Valid!{}".format(green, username, password, reset))
            time.sleep(10)
            main()
        else: 
            print("{}The account {}:{} is not Valid!{}".format(red, username, password, reset))
            time.sleep(3)
            main()
    except Exception:
        print("   {}Checking Failed!{}".format(red, reset))
        time.sleep(3)
        main()

def main():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("CypherTool")
    print("     {}░█████╗░██╗░░░██╗██████╗░██╗░░██╗███████╗██████╗░{}".format(cyan, reset))
    print("     {}██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗{}".format(cyan, reset))
    print("     {}██║░░╚═╝░╚████╔╝░██████╔╝███████║█████╗░░██████╔╝{}".format(cyan, reset))
    print("     {}██║░░██╗░░╚██╔╝░░██╔═══╝░██╔══██║██╔══╝░░██╔══██╗{}".format(cyan, reset))
    print("     {}╚█████╔╝░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║{}".format(cyan, reset))
    print("     {}░╚════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝{}".format(cyan, reset))
    print("")
    print("\n  [1] Single combo check\n  [2] Username Check\n  [3] Credits".format(blue, reset))
    try:
        question = int(input(""))
    except Exception:
        print("{}Invalid input{}".format(red, red))
        time.sleep(2)
        main()
    if question == 1:
        single_check()
    elif question == 2:
        name_check()
    elif question == 3:
        os.system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Cypher Tool")
        print('''Credits:
  - Project made by MachineKillin''')
        print()
        input("Press ENTER to get on menu..")
        main()
main()