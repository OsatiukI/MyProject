player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:


       print("Твой выбор: Камень Ножницы Бумага")
       answer = input()
       if answer == "Камень":
         answer = 3
       elif answer == "Ножницы":
         answer = 2
       else:
         answer = 4
       import random
       options = ["Камень", "Ножницы", "Бумага"]
       conputer = random.choice(options)
       computer_text = conputer
       print("Компьютер выбрал:", computer_text)
       if  conputer == "Камень":
         conputer = 3
       elif conputer == "Ножницы":
         conputer = 2
       else:
          conputer = 4

       if answer == 3 and conputer == 2:
         print("you win")
         player_score +=1

       elif answer == 3 and conputer == 4:
        print("you loss")
        computer_score +=1

       elif answer == 3 and conputer == 3:
         print("nicha")

       elif answer == 2 and conputer == 3:
         print("you loss")
         computer_score +=1

       elif answer == 2 and conputer == 4:
         print("you win")
         player_score += 1

       elif answer == 2 and conputer == 2:
         print("nicha")

       elif answer == 4 and conputer == 3:
         print("you win")
         player_score += 1

       elif answer == 4 and conputer == 2:
         print("you loss")
         computer_score += 1

       else:
         print("you nicha")
       print("Счет: ", computer_score, ":", player_score)

if player_score == 3:
   print("Win : you")
if computer_score == 3:
   print("Win comp")







