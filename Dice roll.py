import random               

while True:  
   
 choice = (input("Roll dice? (Y/N) ")).lower()
   
 if choice == "y":
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print(f"({num1},{num2})")
   
 elif choice == "n":
    print("Thanks for Playing!")
    break

 else : 
    print("Invalid Input")
    

