fruits = ("apple", "banana", "mango", "orange")
vegetables = ("carrot", "broccoli", "spinach")
fast_food = ("burger", "pizza", "fries")
a=input("Enter the food you want to order:")
if a in fruits:
    print("The fruit you want to order is",a)
    c=input("confirm your order with yes/no:")
    if c=="yes":
        print("Order confirmed")
    else:
        print("Order canceled")
    
elif a in vegetables:
    print("The vegetable you want to order is",a)
    d=input("confirm your order with yes/no:")
    if d=="yes":
        print("Order confirmed")
    else:
        print("Order canceled")
elif a in fast_food:
    print("The fastfood you ordered is",a)
    e=input("confirm your order with yes/no:")
    if e=="yes":
        print("Order confirmed")
    else:
        print("Order canceled")
else:
    print("The item you ordered is unavailable")
    
