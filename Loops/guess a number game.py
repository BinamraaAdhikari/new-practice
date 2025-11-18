for i in range(5):
    a=int(input("Please select a random number between 1 to 100:"))
    if a==27:
        print("You win")
        break
    elif a<0:
        print("Only numbers above 0. Please try again")
    elif a>100:
        print("Only numbers below 100. Please try again")
    elif a>27:
        print("You are higher than the required number")
    elif a<27:
        print("You are lower than the required number")
    
else:
    print("Game Over")
        
