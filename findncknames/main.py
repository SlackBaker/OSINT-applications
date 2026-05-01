import whereisnickname
import findnciknameinnet.nicknamebio as nicknamebio
from colorama import Fore, init

init()

if __name__ == "__main__":
    while True:
        userinput = input(Fore.GREEN + "> ")
        match userinput:
            case "quit":
                break
            case "wherenickname":
                whereisnickname.checknickname()
            case "nicknamebio":
                nicknamebio.nicknamebio()