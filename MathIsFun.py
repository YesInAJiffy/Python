import random
import time
from termcolor import colored
import sys
import os



# Prerequisites
# pip install termcolor

starttime = time.time()
points = 0
isGrade3ORBelow = False
gametime = 90


def printexponent(number, type):
    if type == "cube":
        return(str(number)+"³")  # Output: ³
    elif type == "square":
        return(str(number) + "²")  # Output: ²
    elif type == "one":
        return(str(number) + "¹")  # Output: ¹
    elif type == "quad":
        return(str(number)+ "⁴")  # Output: ⁴
    elif type == "pent":
        return(str(number)+ "⁵")  # Output: ⁵

    
def is_timeover():
    global points
    global gametime
    endtime = time.time()
    elapsedtime = endtime - starttime
    if elapsedtime >= gametime :
        if isGrade3ORBelow :
            print(colored("\n\nChild Mode Enabled*******************", "green"))
            print("Your points are getting doubled")
            points = points * 2

        print(colored("\n\n ⏲️⏲️TIME OVER⏲️⏲️", "red", "on_grey"))
        print(colored(f"\n\n\n\n**********YOUR FINAL SCORE IS {points} ********", "blue"))
        if int(points) >= 100:
            print("You made a century 💯💯\n\n\n\n")
        elif int(points) >= 80:
            print("Awesome score 💕💖\n\n\n\n")
        elif int(points) >= 50:
            print("Great Going 😍🤩\n\n\n\n")
        elif int(points) >= 20:
            print("Yes you are improving ❤️‍🩹❤️‍🩹 \n\n\n\n")
        elif int(points) >= 10:
            print("Keep Practicing 😟😟\n\n\n\n")
        else:
            print("Work hard 💔💔\n\n\n\n")
        sys.exit(0)
        return True
    else:
        print(f"⌛⌛ Keep going, you have {gametime - int(elapsedtime)} seconds left ⌛⌛ \n\n")
        return False


def Choice():
    print(colored("Choose what you want to play", "blue", "on_grey"))
    print(colored("Addition ~ 1 | Substraction ~ 2 | Multiplication ~ 3 | Division ~ 4 | Exponents ~ 5 | EXIT ~ 6" ,"yellow",attrs=["bold"]))
    print(colored("Points : \nAddition = 3 points per correct answer | \nSubstraction = 1 points per correct answer | \nMultiplication = 4 points per correct answer | \nDivision = 4.5 points per correct answer |\nExponent = 5.5 points per correct answer |\n**NO NEGATIVE MARKING**\n\n\n", "white"))
    

    choice = input()
    while not (choice.isdigit() and int(choice) < 7):
            print("**Please enter a valid choice**")
            choice = input()
    return choice

def addition():
    global points
    while (True):
        random_integer1 = random.randint(1, 100)
        random_integer2 = random.randint(1, 100)
        print(colored(f"   {random_integer1} ➕ {random_integer2} = ?   ","blue", "on_white",attrs=["bold"]))
        print ("Write answer and press enter. Press 'e' to switch mode.")
        answer = input()

        while not (answer == "e" or answer.isdigit()):
            print("**Please enter a valid choice**")
            answer = input()

        if answer == "e":
            print("you have exited the game.")
            print(f"your final score is {points}")
            break
        if int(answer) == random_integer1 + random_integer2 :
            points = points + 3
            print(colored(f"Great Job, points = {points}", "green", "on_white", attrs=["bold"]))
        else :
            print(colored("Wrong answer, try again.", "red", attrs=["bold"]))
            # This will print the ASCII Bell character to produce a beep sound
            os.system('echo \a')
        
        is_timeover()
        
def substraction():
    global points
    while (True):
        random_integer1 = random.randint(50, 100)
        random_integer2 = random.randint(1, 50)
        print(colored(f"   {random_integer1} ➖ {random_integer2} = ?   ","blue", "on_white",attrs=["bold"]))
        print ("Write answer and press enter. Press 'e' to switch mode.")
        answer = input()
        while not (answer == "e" or answer.isdigit()):
            print("**Please enter a valid choice**")
            answer = input()
        if answer == "e":
            print("you have exited the game.")
            print(f"your final score is {points}")
            break
        if int(answer) == random_integer1 - random_integer2 :
            points = points + 1
            print(colored(f"Great Job, points = {points}","green", "on_white", attrs=["bold"]))
        else :
            print(colored("Wrong answer, try again.", "red", attrs=["bold"]))
            # This will print the ASCII Bell character to produce a beep sound
            os.system('echo \a')
        is_timeover()


def multiplication():
    global points
    while (True):
        random_integer1 = random.randint(1, 12)
        random_integer2 = random.randint(1, 12)
        print(colored(f"   {random_integer1} ❌ {random_integer2} = ?   ","blue", "on_white",attrs=["bold"]))
        print ("Write answer and press enter. Press 'e' to switch mode.")
        answer = input()
        while not (answer == "e" or answer.isdigit()):
            print("**Please enter a valid choice**")
            answer = input()
        if answer == "e":
            print("you have exited the game.")
            print(f"your final score is {points}")
            break
        if int(answer) == random_integer1 * random_integer2 :
            points = points + 4
            print(f"Great Job, points = {points}")
        else :
            print(colored("Wrong answer, try again.", "red", attrs=["bold"]))
            # This will print the ASCII Bell character to produce a beep sound
            os.system('echo \a')
        is_timeover()

def division():
    global points
    while (True):
        random_integer1 = random.randint(5, 15) #19
        random_integer2 = random.randint(3, 8) # 2
        random_integer1 = random_integer1 * random_integer2 #38
        print(colored(f"   {random_integer1} ➗ {random_integer2} = ?   ","blue", "on_white",attrs=["bold"]))
        print ("Write answer and press enter. Press 'e' to switch")
        answer = input()
        while not (answer == "e" or answer.isdigit()):
            print("**Please enter a valid choice**")
            answer = input()
        if answer == "e":
            print("you have exited the game.")
            print(f"your final score is {points}")
            break
        if int(answer) == random_integer1 // random_integer2 :
            points = points + 4.5
            print(f"Great Job, points = {points}")
        else :
            print(colored("Wrong answer, try again.", "red", attrs=["bold"]))
            # This will print the ASCII Bell character to produce a beep sound
            os.system('echo \a')
        is_timeover()

def exponents():
    global points
    while (True):
        random_integer1 = random.randint(1, 10)
        random_integer2 = random.randint( 1, 5)
        if(random_integer2 == 1):
            print(colored(printexponent(random_integer1, "one"),"blue", "on_white",attrs=["bold"]))
        elif(random_integer2 == 2):
            print(colored(printexponent(random_integer1, "square"),"blue", "on_white",attrs=["bold"]))
        elif(random_integer2 == 3):
            print(colored(printexponent(random_integer1, "cube"),"blue", "on_white",attrs=["bold"]))
        elif(random_integer2 == 4):
            print(colored(printexponent(random_integer1, "quad"),"blue", "on_white",attrs=["bold"]))
        elif(random_integer2 == 5):
            print(colored(printexponent(random_integer1, "pent"),"blue", "on_white",attrs=["bold"]))
        #print(colored(f"   {random_integer1}{random_integer2} = ?   ","blue", "on_white",attrs=["bold"]))
        print ("Write answer and press enter. Press 'e' to switch mode.")
        answer = input()
        while not (answer == "e" or answer.isdigit()):
            print("**Please enter a valid choice**")
            answer = input()
        if answer == "e":
            print("you have exited the game.")
            print(f"your final score is {points}")
            break
        if int(answer) == random_integer1 ** random_integer2 :
            points = points + 5.5
            print(f"Great Job, points = {points}")
        else :
            print(colored("Wrong answer, try again.", "red", attrs=["bold"]))
            # This will print the ASCII Bell character to produce a beep sound
            os.system('echo \a')
        is_timeover()


printexponent(5 , "square")

printexponent(6, "cube")
print("\n\n\n\n")
author_name =   "************** Shlok Singh Rana "
author_school = "************** Parmenter Elementary "
print(colored("*".ljust(50,'*'), "white", "on_blue", attrs=["bold"]))
print( colored(author_name.ljust(50, '*'), "green", attrs=["bold"]))
print(colored(author_school.ljust(50, '*'), "green", attrs=["bold"]))
print(colored("*".ljust(50,'*'), "white", "on_blue", attrs=["bold"]))
print("\n\n\n\n")

# Check if user needs easy mode
print("Press 'Y' if you are in Grade 3 or below, any other key for higher grades.")
x = input()
if (x.upper() == "Y"):
    print("Okay you go with the easy scoring mode\n\n")
    isGrade3ORBelow = True
else :
    print("Okay you go with the normal scoring mode\n\n")
    isGrade3ORBelow = False



while True:
    i = Choice()
    if int(i) == 1:
        #print(colored("You choose addition. You have 1 minute, let's see how much you score", "green", attrs=["bold"]))
        addition()
    elif int(i) == 2:
        #print("You choose substraction. You have 1 minute, let's see how much you score")
        substraction()
    if int(i) == 3:
        #print("You choose multiplication. You have 1 minute, let's see how much you score")
        multiplication()
    if int(i) == 4:
        #print("You choose division. You have 1 minute, let's see how much you score")
        division()
    if int(i) == 5:
        #print("You choose exponents. You have 1 minute, let's see how much you score")
        exponents()
    if int(i) == 6:
        print("Thank you for playing with us. Bye for now.")
        sys.exit()
