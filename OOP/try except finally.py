try:
    n=int(input("Enter a number:"))
except ValueError:
    print("Its a error buddy")
    
finally:
    print("I always run")
