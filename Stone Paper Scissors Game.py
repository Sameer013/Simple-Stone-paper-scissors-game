#Stone paper scissors game
import random



def game():
    cpu = random.randint(1,3)
    if user == 1 and cpu == 1:
        print("You Both use STONE!")
        print("\tTIE")
    elif user == 2 and cpu == 2:
        print("You Both use SCISSORS!")
        print("\tTIE")
    elif user == 3 and cpu == 3:
        print("You Both use PAPERS!")
        print("\tTIE")
        
     #Now main deciding algorithm
        
    elif user == 1 and cpu == 2:
        print("CPU has SCISSORS and You have STONE")
        print("\tYou WIN!")
    elif user == 1 and cpu == 3:
        print("CPU has PAPERS and You have STONE")
        print("\tYou LOSE!")
    elif user == 2 and cpu == 3:
        print("CPU has PAPERS and You have SCISSORS")
        print("\tYou WIN!")
    elif user == 2 and cpu == 1:
        print("CPU has STONE and You have SCISSORS")
        print("\tYou LOSE!")
    elif user == 3 and cpu == 2:
        print("CPU has SCISSORS and You have PAPERS")
        print("\tYou LOSE!")
    elif user == 3 and cpu == 1:
        print("CPU has STONE and You have PAPERS")
        print("\tYou WIN!")
    elif user != cpu:
        print("\tWrong Choice")
        

while True:
    print("Enter Your choice ")
    print("  -->      1. for STONE \n  -->      2. for SCISSORS \n  -->      3. for PAPERS")
    user = int(input("  ------>  "))
    game()   #function to decide 
    
    print("------------------x------------------")