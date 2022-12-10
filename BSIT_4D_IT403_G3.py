import os
import random

counter = 1
points = 0
qnum = [1, 2, 3, 4 ,5 ,6 ,7, 8, 9, 10]

os.system('cls||clear')
print("--------------------------------------")
print("Welcome to our Python Random Quiz!")
print("--------------------------------------", "\n")
print("We are the Group 3 and our topic is Loops.\nMembers: ") 
print("Elgene Victoria\nEmmalyn Catiis\nJefferson San Jose\nKyla Valenzuela\n") 
name = input("What is your name?: ")
print("Hello " +name, "Are you ready to take this quiz? [Y] or [N]")

x = input()
os.system('cls||clear')

if x == "y" or x == "Y":

    i = 0
    while i < 10:
        i +=1
        

        y = random.choice(qnum)
        print("Question No.", i)
        
        if (y == 1):
            print(counter,". This statement in python terminates the current loop and resumes execution at the next statement. ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            
            if (answer == "Break" or answer == "break"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
                
            else:
                print("Sorry! Your answer is wrong.","\n")
                  
        elif (y == 2): 
            print(counter,". This statement in python returns the control to the beginning of the while loop. ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
          
            if (answer == "Continue" or answer == "continue"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
                
        elif (y == 3): 
            print(counter,". It is a null operation; nothing happens when it executes ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
                  
            if (answer == "Pass" or answer == "pass"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
                       
        elif (y == 4): 
            print(counter,". It can execute a set of statements as long as a condition is true", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
           
            if (answer == "While Loop" or answer == "While loop" or answer == "while loop" or answer == "while Loop"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")     
        
        elif (y == 5): 
            print(counter,". Can execute a set of statements, once for each item in a list, tuple, set, etc.", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            
            if (answer == "For loop" or answer == "For Loop" or answer == "for loop"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
                
        elif (y == 6): 
            print(counter,". Rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            
            if (answer == "Continue" or answer == "continue"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
                
        elif (y == 7): 
            print(counter,". It is used when a statement is required syntactically but you do not want any command or code to execute. ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
            
            if (answer == "Pass" or answer == "pass"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
                
        elif (y == 8): 
            print(counter,". It is a sequence of instructions that is continually repeated until a certain condition is reached. ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
           
            if (answer == "Loop" or answer == "loop"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
        
        elif (y == 9): 
            print(counter,". It is when some external condition is triggered requiring a hasty exit from a loop. ", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
          
            if (answer == "Break" or answer == "break"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
                
        elif (y == 10): 
            print(counter,". It is also useful in places where your code will eventually go, but has not been written yet", sep='')
            qnum.remove(y)
            print("\n","Answer:")
            answer = input()
          
            if (answer == "Pass" or answer == "pass"):
                points += 1
                print("Your answer is correct! You've got 1 point.","\n")
            else:
                print("Sorry! Your answer is wrong.","\n")
                
        counter +=1
    print("All done! Do you want to see the result? [Y] or [N]")

    c = input()
    if (c == 'y' or c == 'Y'):
        print("\n")
        print("------------------------------------")
        print("   This your total score is ", points, "/10.", sep='')
        print("------------------------------------", "\n")
    else:
    
         print("Thank you!")

else:
    print("All right, Thank you!")