    # -*- coding: utf-8 -*-
    """
    Created on Tue Dec  3 19:37:20 2019
    
    defino funciones
    """
    def add(x, y):
        
        return x + y
    
    "esta función agrega dos números"
    
    def subtract(x, y):
        
        return x - y
    
    "resta dos números"
    
    def multiply(x, y):
        
        return x * y
    
    "multiplica dos numeros"
    
    
    def divide(x, y):
        
        return x / y
    
    "divide"
    
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    
    
    "creo una variable llamada elección para que el usuario pueda elegir"
    
    choice = input("Enter choice(1/2/3/4):")
    
    "hago el input de los números"
    
    
    n1=int(input("Enter the first number"))
    n2=int(input("Enter other number"))
    
    
    if choice =='1':
       print(n1, "+", n2, "=", add(n1,n2))
       
    elif choice == '2':
        print(n1, "-" ,n2, "=" ,subtract(n1,n2))
    elif choice == '3':
        print(n1, "*", n2, "=", multiply(n1,n2))
    elif choice == '4':
        print(n1,"/",n2, "=", divide(n1,n2))
        
    else:
        print("Invalid input")
        
        
        
