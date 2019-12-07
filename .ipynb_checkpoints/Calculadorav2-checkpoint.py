    import re
    
    print("Hi Calcule")
    print("Type 'quit' to exit\n")
    
    previous=0
    run = True
    def performMath():
        "defino la variable y despues la aplico en el ciclo while"
        equation = input("Enter equation:")
        if equation == 'quit':
            run = False 
        print("you tiped",equation)
        
    while run:
        performMath()
