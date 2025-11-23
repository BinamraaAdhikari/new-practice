class calculator():
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print("The square is:",self.n*self.n)
    
    def cube(self):
        print("The cube is:",self.n*self.n*self.n) 
    
n=(int(input("Enter a number:")))
       
a=calculator(n)
a.square()
a.cube()       
