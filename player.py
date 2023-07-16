
def roll_dice():
        import random
        r=random.randint(1,6)
        return r


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
        locate = -1
        temp = self.position
        if self.position in self.fromposition:
            locate=self.fromposition.index(self.position) 
            self.position = self.toposition[locate]
            if temp != self.position:
                if self.toposition[locate] > self.fromposition[locate]:
                    print("You climbed")
                else:
                    print("snake bite")

   
    
    
    def updater (self):
        dice = roll_dice()
        if self.position == 0:
            if dice == 6:
                self.position = self.initial
        else:
            f =self.final % self.position
            if self.position != 0 and f <= dice:    
                print(f"dice={dice}")
                self.position += dice
        print(f"self.position={self.position}")


    def won(self):
        if self.position == self.final :
            self.ongame = False

        

