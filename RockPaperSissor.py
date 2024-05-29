import random

def choose(rpc):
    if rpc == 0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
    elif rpc == 1:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
    else:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

me = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
choose(me)
computer = random.randint(0,2)
print("Computer chose : ")
choose(computer)
if(me == computer):
    print("Its a draw")
elif(me == 0 and computer == 2 or me == 1 and computer == 0 or me == 2 and computer == 1):
    print("You WON")
else:
    print("You LOOSE")