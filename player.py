import random
def roll_dice():
        
        r=random.randint(1,6)
        return r

from art import dices
class Target:
    def __init__(self,name) :
       self.fromposition = [8,19,21,28,36,43,50,54,61,62,66,98,93,83,69,68,64,59,52,48,46]
       self.toposition  =  [26,38,82,53,57,77,91,88,99,96,87,13,37,22,33,2,24,18,11,9,15]
       self.position = 0
       self.score = 0
       self.ongame = True
       self.initial =1
       self.final = 100
       self.name=name


    def promotion(self):
        if self.position in self.fromposition:
            locate=self.fromposition.index(self.position) 
            self.position = self.toposition[locate]
            if self.toposition[locate] > self.fromposition[locate]:
                print("You climbed")
            else:
                print("snake bite")
            print(f"So {self.name} is now @ position={self.position}")   

   
    
    
    def updater (self):
        dice = roll_dice()
        print(dices[dice-1])
        if self.position == 0:
            if dice == 6:
                self.position = self.initial
        else:
            f =self.final - self.position
            # print(f"dice={dice}")
            if  f >= dice:    
              
                self.position += dice
        print(f"{self.name} got dice {dice} so now @ position={self.position}")


    def won(self):
        if self.position >= self.final :
            self.ongame = False
            print(f"{self.name} won the match ")

        
    

        

