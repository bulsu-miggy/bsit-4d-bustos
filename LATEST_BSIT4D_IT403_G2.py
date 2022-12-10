import os #for terminal clear
import random # for randoming questions
import sys #for exiting
import time

counter = 1 #for numbering
points = 0 #for points
QuestionNum = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10] #for questions 
appreciation = ["Wow!", "Brilliant!", "Amazing!", "Yahoo!", "Good-for-you!"]

os.system('cls||clear') 
print(".........................................")
print("Welcome to Python-Collection Random Quiz!") #Start_welcome
print(".........................................", "\n\n")
print("Are you ready? [Yes] or [No]")

x = input()
os.system('cls||clear') #clearing the terminal


if x == "yes" or x == "Yes" or x == "YES":
    print("..............................................")
    print("GET READY! The QUIZ will start after 5 seconds")
    print("..............................................", "\n\n")
    time.sleep(5) #countdown
    os.system('cls||clear')
    
    i = 0
    while i < 10: #10 loops for 10 questions
        i +=1
        

        y = random.choice(QuestionNum) #randomnumber
        appreciate = random.choice(appreciation) #for appreciation
        
        print("Question:")
        
        if (y == 1): #question 1
            print(counter,". It has a shorthand that requires it to be in a list. \n [While Loop] [Nested Loop] [Short Loop] [For Loop]", sep='') #separator for spacing
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            
            if (answer == "For Loop" or answer == "for loop"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
                
            else:
                print("Sorry, incorrect answer.","\n")
                
                
        elif (y == 2): #question 2
            print(counter,". A collection type that is ordered, indexed and just like the arrays declared in other languages. \n [List] [Tuples] [Dictionaries] [Set]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "list" or answer == "Lists" or answer == "list" or answer == "List"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")
                
                
        elif (y == 3): #question 3
            print(counter,". A collection type just like lists but it is immutable. \n [List] [Tuples] [Dictionaries] [Set]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "Tuples" or answer == "tuples" or answer == "tuple" or answer == "Tuple"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")
                
                
        elif (y == 4): #question 4
            print(counter,". A collection type that are unordered, changeable, and indexed. \n [List] [Tuples] [Dictionaries] [Set]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "Dictionaries" or answer == "dictionaries" or answer == "dictionary" or answer == "Dictionary"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")       
        
        elif (y == 5): #question 5
            print(counter,". An unordered collection, does not record element position or order of insertion, and could be heterogeneous. \n [List] [Tuples] [Dictionaries] [Set]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "Set" or answer == "set"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n") 
                
        elif (y == 6): #question 6
            print(counter,". Special characters used in set to enclose its contents. \n [Brackets] [Asteries] [Braces] [Parentheses]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "braces" or answer == "Braces"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")
                
        elif (y == 7): #question 7
            print(counter,". Special characters used in dictionaries to enclose its contents. \n [Brackets] [Asteries] [Braces] [Parentheses]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "braces" or answer == "Braces"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")
                
        elif (y == 8): #question 8
            print(counter,". Special characters used in tuples to enclose its contents. \n [Brackets] [Asteries] [Braces] [Parentheses]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "Parentheses" or answer == "parentheses"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")
        
        elif (y == 9): #question 9
            print(counter,". Special characters used in lists to enclose its contents. \n [Brackets] [Asteries] [Braces] [Parentheses]", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "brackets" or answer == "Brackets"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")
                
        elif (y == 10): #question 10
            print(counter,". These four (list, tuples, string, dictionaries) are types of python collections except.", sep='')
            QuestionNum.remove(y)
            print("\n","Answer:")
            answer = input()
            os.system('cls||clear')
            
            if (answer == "String" or answer == "string"):
                points += 10
                print(appreciate, "You've got 10 points.","\n")
            else:
                print("Sorry, incorrect answer.","\n")
                
        counter +=1
            
elif(x == "no" or x == "NO" or x == "No"):
    print("Thank you! Please don't forget to answer your quizzes.", "\n\n\n\n\n\n")
    sys.exit()
else:
    print("Invalid answer! Please try again later.", "\n\n\n\n\n\n")
    sys.exit()
    
print("Your Quiz is finished. Do you want to see the result? [Y] or [N]")#done_score
c = input()
if (c == 'y' or c == 'Y'):
    os.system('cls||clear')
    print(".........................................")
    print("CONGRATULATIONS! Your Total Score is ", points, "/100.", sep='')
    print(".........................................", "\n\n\n\n\n")
elif(c == 'n' or c =='N'):
    os.system('cls||clear')
    
    print("Thank you for answering our Random Quiz!", "\n\n\n\n\n\n")
else:
    os.system('cls||clear')
    print("Invalid answer! Please comeback later.", "\n\n\n\n\n\n")
    