rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

image= [rock, paper, scissors]
names = ["rock", "paper", "scissors"]

while(True):
    computer= random.randint(0,2)
    user = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    score= [0,0]

    if user >= 3 or user <= 0 :
        print("You typed an invalid number, you lose!")
        score[0] += 0
        score[1] += 1

    else:
        print(f"You chose {names[user]}")
        print(image[user])
        print(f"Computer chose {names[computer]}")
        print(image[computer])
        
    if int(computer) == int(user) :
        print("It's a draw.")
        score[0] += 0
        score[1] += 0


    elif computer == 1 and user == 2 or (computer == 3 and user == 1) or ( computer == 2 and user == 3):
        print("You win!")
        score[0] += 1
        score[1] += 0


    elif (computer == 1 and user == 3) or (computer == 3 and user == 2) or (computer == 2 and user == 1):
        print("You loose!")
        score[0] += 0
        score[1] += 1
    
    print(f"You final score\n You- {score[0]} \n Computer - {score[1]}")

