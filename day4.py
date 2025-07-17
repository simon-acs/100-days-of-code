import random
value = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user =int(value)


#computer game play
ai = [0,1,2]
num = random.choice(ai)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
scissors
'''
#user
print("Player Chooses :")
if user == 0 :
    print(rock)
elif user == 1:
    print(paper)
elif user == 2 :
    print(scissors)
else:
    print("Wrong Value")
    exit()

    #ai
print("Computer Chooses :")
if num == 0 :
    print(rock)
elif num == 1:
    print(paper)
else:
    print(scissors)



if user == num :
    print ("Draw")
elif user == 0 and num == 2 :
    print("You Win")
elif user == 0 and num == 1 :
    print("You Lose")
elif user == 1 and num == 0 :
    print("You Win")
elif user == 1 and num == 2 :
    print("You Lose")
elif user == 2 and num == 0 :
    print("You Lose")
elif user == 2 and num == 1 :
    print("You Win")




