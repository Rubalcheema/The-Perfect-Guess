from random import randint


print("Welcome to the perfect Guess Game")
print("Guess a number between 1 - 100 ")
Number = randint(1,100)
guess = 0
while True:
 guess +=1
 answer =int(input("what is the number ? ...."))
 if answer < Number:
   print("GO Higher")
 elif answer > Number:
    print("Go Lower")  
 elif answer == Number:
    print ("BULLS EYE ! YOU WON..")
    score = 1000 - guess 
    print(f"your score is {score}")
    leave = input("do you want to play again ?..(yes/no)").lower()
    if leave == "no":
      print(f"your total score is {score}")
      break
    else:
      print("let's play again ")
      Number = randint(1,100)
      guess = 0
 
 
 