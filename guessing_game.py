
import  random

print("\n\n--------------------WELCOME TO THE GUESSING GAME--------------------\n\n")

print("Please Select the level :\n")


level = int(input(" 1. Easy \n 2. Medium \n 3. Hard \n\n "))

if(level==1):
   number=  random.randint(1,10)
   print("You have to guess the number between 1 and 10 \n Try Your luck...")

elif(level==2):
       number=  random.randint(1,50)
       print("You have to guess the number between 1 and 50 \n Try Your luck...")

else:
       number=  random.randint(1,100)
       print("You have to guess the number between 1 and 100 \n Try Your luck...")



attempts=0

while(True):
    attempts += 1
    guess = input("Guess the number: \n")
    guess= int(guess)

    if (guess < number):
        print("Your guess was too low. Try Again ")

    elif (guess > number):
        print("Your guess was too high. Try Again")  

    else:
        print("Hurray... Your guess was correct")  
        break      


print("You won the game in " + str(attempts) + " attempts" )

print("Thanks for playing ...")