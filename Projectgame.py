"""
s for snake
w for water
g for gun
"""
import random
computer = random.choice([1,2,3])
you = input("Enter your choice: ")
youdict = {"s":1,"w":2,"g":3}
revdict = {1:"Snake",2:"Water",3:"Gun"}
num =youdict.get(you)

print(f"You entered {revdict.get(num)}\nComputer entered {revdict.get(computer)}")
if(computer==you):
    print("Game drwan")
else:
    if(computer==1 and num == 2):
        print("You Loose!")
    elif(computer==1 and num ==3):
        print("You Win!")
    elif(computer==2 and num == 1):
        print("You Win!")
    elif(computer==2 and num == 3):
        print("You Loose!")
    elif(computer==3 and num ==1):
        print("You Loose!")
    elif(computer==3 and num == 2):
        print("You Win!")
    else:
        print("Something went wrong!!!!!!")