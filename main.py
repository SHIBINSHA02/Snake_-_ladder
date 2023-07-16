
from player import *

name = input("Enter your name:")
Player1 = Target(name)

# while Player1.ongame :
for _ in range (100):
    Player1.updater()
    Player1.promotion()
    Player1.won()
    print("/////////////")
    
