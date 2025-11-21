class car(): 
def __init__(self,name,color,price): 
  self.name=name self.color=color self.price=price 
  def getinfo(self): print("The color of ",self.name,"car is",self.color,"and it cost about Rs",self.price) 
    
car1=car("Harry","Red",120000) 
car2=car("Dogesh","Green",344200) 
car3=car("Shyam","Black",560000) 
car4=car("Sita","White",7890000) 
car1.getinfo() 
car2.getinfo() 
car3.getinfo() 
car4.getinfo()
