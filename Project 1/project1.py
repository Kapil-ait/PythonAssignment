import random
print("WELCOME TO MY GAME PAGE")
print("Player vs Computer")

num=int(input("How many rounds you want to play:"))
userscore=0
computerscore=0
drawscore=0
start=1

while start<=num:
 print("\nRound",start)
 n=input("Enter player choice (Rock,Paper,Scissor):")
 com=random.choice(["Rock","Paper","Scissor"])
 print("Computer:",com)

 match(n,com):
  case("Rock","Rock"):
   print("Draw")
   drawscore+=1
   start+=1
  case("Paper","Paper"):
   print("Draw")
   drawscore+=1
   start+=1
  case("Scissor","Scissor"):
   print("Draw")
   drawscore+=1
   start+=1
  case("Rock","Paper"):
   print("Computer wins")
   computerscore+=1
   start+=1
  case("Rock","Scissor"):
   print("User wins")
   userscore+=1
   start+=1
  case("Paper","Rock"):
   print("User wins")
   userscore+=1
   start+=1
  case("Paper","Scissor"):
   print("Computer wins")
   computerscore+=1
   start+=1
  case("Scissor","Rock"):
   print("Computer wins")
   computerscore+=1
   start+=1
  case("Scissor","Paper"):
   print("User wins")
   userscore+=1
   start+=1
  case _:
   print("Invalid choice")

print("=====Dashboard=====")
print("User wins:",userscore)
print("Computer wins:",computerscore)
print("Draw scores:",drawscore)

if userscore>computerscore:
 print("🏆 Overall Winner: User")
elif computerscore>userscore:
 print("🏆 Overall Winner: Computer")
else:
 print("🤝 Overall Match Draw")

print("Game Over")