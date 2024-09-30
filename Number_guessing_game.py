# Generate a random number
#Ask user to make a guess
#If guess > genNum then: Guess is high 
#If guess < genNum then: Guess is low 
#If guess = genNum then: Well done

import random

genNum = random.randint(1,100)

while True:
    
 guess = int(input("guess the number:  "))

 if guess > genNum : 
    print ("guess was high, Try Again ")
    
    
 elif guess < genNum:
     print("Guess wwas low, Try Again ")
     
 elif guess == genNum:
     print ("Comgrats , Number was " + str(genNum))
     break