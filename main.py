from player import Target

Player=[]
num= int(input("Enter the number of Players"))

for i in range (num):
    name = input("Enter your name:")
    Player.append(Target(name))

while any (player.ongame for player in Player):
    for player in Player:
        player.updater()
        player.promotion()
        player.won()
    
    print("/////////////")
    
