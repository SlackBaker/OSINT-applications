import findinstagram
import facebookfind

def nicknamebio():
    nickname = str(input("Nickname: "))
    findinstagram.findbio(nickname)
    facebookfind.bioofuser(nickname)