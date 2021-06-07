import os
import time
peaceful = "47616d654d6f6465010000000776616c75655f5f00080200000005"
normal = "47616d654d6f6465010000000776616c75655f5f00080200000000"
hard = "47616d654d6f6465010000000776616c75655f5f00080200000001"
easy = "47616d654d6f6465010000000776616c75655f5f00080200000003"
creative = "47616d654d6f6465010000000776616c75655f5f00080200000002"
gamemode = ""
gamemode2 = ""
changegamemode = ""
changegamemode2 = ""
content = ""
def checkgamemodeandselectgamemod():
    os.system("copy " + '"' + file + '"' + " " + '"' + file + ".bak" + '"' + " /y" + ">nul")
    with open(file, 'rb') as f:
        content = f.read().hex()
        f.close()
    if normal in content:
        gamemode = "normal"
        gamemode2 = normal
    elif hard in content:
        gamemode = "hard"
        gamemode2 = hard       
    elif easy in content:
        gamemode = "easy"
        gamemode2 = easy
    elif peaceful in content:
        gamemode = "peaceful"
        gamemode2 = peaceful
    elif creative in content:
        gamemode = "creative"
        gamemode2 = creative
    else:
        print("an error has occured\n exiting....")
        exit()
    print("your current gamemode is " + gamemode)
    print("type 1 for peaceful")
    print("type 2 for normal")
    print("type 3 for hard")
    print("type 4 for easy")
    print("type 5 for creative")
    theinput = input("what gamemode would you like to change to?: ")
    if int(theinput) == 1:
        changegamemode = "peaceful"
        changegamemode2 = peaceful
    elif int(theinput) == 2:
        changegamemode = "normal"
        changegamemode2 = normal
    elif int(theinput) == 3:
        changegamemode = "hard"
        changegamemode2 = hard
    elif int(theinput) == 4:
        changegamemode = "easy"
        changegamemode2 = easy
    elif int(theinput) == 5:
        changegamemode = "creative"
        changegamemode2 = creative
    else:
        print("error that is not an option")
        print("please try again")
        checkgamemodeandselectgamemod()
    return content, gamemode, gamemode2, changegamemode, changegamemode2
def change(content, gamemode, gamemode2, changegamemode, changegamemode2):
    print("changing gamemode " + gamemode + " to gamemode " + changegamemode)
    yesorno = input("are you sure you want to continue? y or n: ")
    if yesorno == "n":
        print("exiting....")
        exit()
    if yesorno == "y":
        content = content.replace(gamemode2, changegamemode2)
        with open(file, 'wb') as d:
            d.write(bytes.fromhex(content))  
            d.close()
        print("success")
        print("now exiting....")
        exit()
    else:
        print("that is not a correct choice please try again...")
        change(content, gamemode, gamemode2, changegamemode, changegamemode2)
if __name__ == '__main__':
    try:
        import pyfiglet
    except:
        os.system("pip3 install pyfiglet>nul")
        os.system("pip install pyfiglet>nul")
    try:
        import pyfiglet
    except:
        print('please install the python module "pyfiglet"')
        print('exiting....')
        exit()
    try:
        import easygui
    except:
        os.system("pip3 install easygui>nul")
        os.system("pip install easygui>nul")
    try:
        import easygui
    except:
        print('please install the python module "easygui"')
        print('exiting....')
        exit()
    try:
        print(pyfiglet.figlet_format("Raft gamemode changer by moom825"))
        time.sleep(2)
        print("To find where your world save file is located, go to this link...")
        print("https://steamcommunity.com/app/648800/discussions/0/1694922980049829923/")
        print("press enter to continue...")
        input()
        while True:
            file = easygui.fileopenbox(msg="select your raft world file", title="Raft gamemode changer by moom825", default='*', filetypes ="*.*", multiple=False)
            if file[-3:] == "rgd":
                break
            else:
                print("This is not the correct file or file does not have to correct extension")
        content, gamemode, gamemode2, changegamemode, changegamemode2 = checkgamemodeandselectgamemod()
        change(content, gamemode, gamemode2, changegamemode, changegamemode2)
    except Exception as e:
        print("an error has occured: ")
        print(e)
