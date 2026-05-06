from colorama import Fore, init

import whereisnickname
import nicknamebio as nicknamebio

init()

def main():
    while True:
        userinput = input(Fore.GREEN + "> ").strip()

        match userinput.lower():
            case "quit" | "exit" | "x":
                break

            case "whereisnickname":
                whereisnickname.checknickname()

            case "nicknamebio":
                nicknamebio.nicknamebio()

            case _:
                print(Fore.YELLOW + "Unknown command")

if __name__ == "__main__":
    main()