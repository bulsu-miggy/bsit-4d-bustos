import time
import random
import os

print("Welcome to the  Quiz Game!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0
qnum = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10]
counter = 1

i = 0
while i < 10:
  i +=1
  
  y = random.choice(qnum) #randomnumber
  print("Question:")

  if (y == 1): #question 1
            print(counter,". If you want to access the string in reverse, you must use a (blank) index\n(a) Table\n(b) Row\n(c) Index\n(d) Line\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "c"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "c", "\n\n")
  elif (y == 2): #question 2
            print(counter,". What symbol should you use to combine two string values?\n(a) .\n(b) ,\n(c)/\n(d) +\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "d"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "d", "\n\n")
  elif (y == 3): #question 3
            print(counter,". Is it true that you can't use a single quote for string?\n(a) True\n(b) False\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "b"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "b", "\n\n")
  elif (y == 4): #question 4
            print(counter,". is a sequence of instructions that is continually repeated until a certain condition is reache\n(a) line\n(b) loop\n(c) table\n(d) Non of the above\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "b"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "b", "\n\n")
  elif (y == 5): #question 5
            print(counter,". What symbol should you use to duplicate string? \n(a) *\n(b) +\n(c) :\n(d) Non of the above\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "a"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "a", "\n\n")
  elif (y == 6): #question 6
            print(counter,". is a collection of items, or data, stored in contiguous memory locations, also known as database system?\n(a) Java Script\n(b) c++\n(c) String\n(d) Array\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "d"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "d", "\n\n")
  elif (y == 7): #question 7
            print(counter,". Is it true that you can also combine the positive and negative indexes.\n(a) True\n(b) False\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "a"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "a", "\n\n")
  elif (y == 8): #question 8
            print(counter,". is traditionally a sequence of characters, either as a literal constant or as some kind of variable. \n(a) Java Script\n(b) c++\n(c) String\n(d) Array\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "c"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "c", "\n\n")
  elif (y == 9): #question 9
            print(counter,". is it true that you can't loop in string?  \n(a) True\n(b) false\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "b"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "b", "\n\n")
  elif (y == 10): #question 10
            print(counter,". What bracket should you use to access substring?  \n(a) Rectangle Bracket\n(b) Square Bracket\n(c) Diamond Bracket\n(d) Non of the above\n\n ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer.lower() == "b"):
                score += 1
                print("Correct! Good Job.\n")
                
            else:
                print("Incorrect!\n")
                print("The correct answer is", "b", "\n\n")
  counter +=1

#print the score
while score >= 4:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing the  Quiz Game!")