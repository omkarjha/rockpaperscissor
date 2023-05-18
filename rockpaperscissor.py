from random import randint

t = ["Rock","Paper","Scissor"]

computer = t[randint(0,2)]

player = False

while player == False:
    
     player = input("Rock,Paper,Scissors?\n")
     if player == computer:
          print("Tie!")
     elif player == "Rock":
          if computer == "Paper":
               print("The computer wins as it COVERS it's opponent")
          else:
               print("The player wins as it SMASH it's opponent")

     elif player == "Paper":
          if computer == "Scissor":
               print("The computer wins as it CUTS it's opponent")
          else :
               print("The player wins as it COVERS it's opponent")
          
     elif player == "Scissor":
          if computer == "Rock":
               print("The computer wins as it SMASH it's opponent")
          else :
               print("The player wins as it CUTS it's opponent")
     else :
          print("That's not a valid play....Recheck your spelling!!!")
          
player = False
computer = t[randint(0,2)]
          