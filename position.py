fromposition = [8,19,21,28,36,43,50,54,61,62,66,98,93,83,69,68,64,59,52,48,46]
toposition  =  [26,38,82,53,57,77,91,88,99,96,87,13,37,22,33,2,24,18,11,9,15]
i=input("enter the value of i")
position=fromposition.index(int(i)) 

if int(i) in fromposition:
    i= toposition[fromposition.index(int(i))]
 
print(i)

if toposition[position] > fromposition[position]:
    print("You climbed")
else:
    print("snake bite")