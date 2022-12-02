import random
import time
import os

def play ():

    os.system('cls')
    print("\n\nWelcome to Conditional Statement Quiz by Group 4!\n\n")
    
    questionnaires = {
        "1. Consist of a Boolean expression followed by one or more statements:\n\ta. if statement\n\tb. else statement\n\tc. or statement\n\td. and statement" : ["a", "A"],
        "2. Analyze the following line of codes:\na = 3; b=4;\nif (a > b):\n\tprint(“a is greater than b”)\nelse:\n\tprint(“b is greater than a”)\n\n\ta. a is greater than b\n\tb. b is greater than a\n\tc. error\n\td. none of the above" : ["b", "B"],
        "3. The ___ keyword is a logical operator, and is used to combine conditional statement.\n\ta. If\n\tb. Else\n\tc. Or\n\td. And" : ["d", "D"],
        "4. You can have if statements inside if statements, this is called ___ statements.\n\ta. And\n\tb. Or\n\tc. Elif\n\td. Nested If" : ["d", "D"],
        "5. The following are all Arithmetic Operation except?\n\ta. Addition\n\tb. Multiplication\n\tc. Division\n\td. Factor" : ["d", "D"],
        "6. An ___ statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 or a FALSE value.\n\ta. If statement\n\tb. Else statement\n\tc. Elif statement\n\td. Short-Hand If statement" : ["b", "B"],
        "7. If you have only one statement to execute, you can put it on the same line as the if statement.\n\ta. If statement\n\tb. Else statement\n\tc. Elif statement\n\td. Single line If statement" : ["d", "D"],
        "8. The following are all logical operator except:\n\ta. And\n\tb. Or\n\tc. Equal\n\td. Not" : ["c", "C"],
        "9. If you have only one statement to execute, one for if, and one for else, you can put it in all on the same line.\n\ta. If statement\n\tb. Else statement\n\tc. Single line If Else statement\n\td. Single line If statement" : ["c", "C"],
        "10. The following are all Arithmetic operator except:\n\ta. Or\n\tb. Addition\n\tc. Division\n\td. Multiplication" : ["a", "A"],
    }

    score = 0

    questionnaires_list = list(questionnaires.items())
    random.shuffle(questionnaires_list)
    questionnaires = dict(questionnaires_list)

    for questions, answers in questionnaires.items():
        print(questions)
        answer = input("\nAnswer: ")

        if answer ==  answers[0] or answer ==  answers[1]:
            print("Correct!\n\n\n")
            score += 1
        else:
            print("Incorrect!\n\n\n")
            continue


#LOADING COUNTDOWN
    def countdown(t):
        
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Loading", timer, end="\r")
            time.sleep(1)
            t -= 1

 #CALLING FUNCTION COUNTDOWN  
    t = 3   
    countdown(int(t))


    print("Your Score: " + str(score) + "/" + str(len(questionnaires)))
    percentage = score / len(questionnaires)

    print("Percentage: " + f"{percentage:.0%}")

#TRY AGAIN
    def again():
        play_again = input("\nDo you want to take a quiz again? [y/n]:")
        if(play_again == "y" or play_again =="Y"):
            os.system('cls')
            play()
        elif play_again == "n" or play_again == "N":
            os.system('cls')
            print("\n\nQuiz shutting down...")
            quit()
        else:
            print("\nIncorrect input!")
            again()

 #CALLING FUNCTION TRY AGAIN           
    again()


#INTRO

def intro():
    print("\n\nWelcome to Conditional Statement Quiz by Group 4!\n\n")
    take_quiz = input ("Wanna take a quiz? [y/n]: ")

    if take_quiz == "y" or take_quiz == "Y":
        play()
    elif take_quiz == "n" or take_quiz == "N":
        os.system('cls')
        print("\n\nQuiz shutting down...")
        quit()
    else:
            print("\nIncorrect input!")
            intro()

#CALLING FUNCTION INTRO 
os.system('cls')
intro()