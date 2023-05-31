
def sum(x,y):
    return(x + y)

def subtract(x,y):
    return(x - y)

def multiply(x,y):
    return(x * y)

def divide(x,y):
    return(x / y)

print("  Welcome To The Calculator:")

while True:
    
        print("\nOPERATIONS")
        print("1. Sum\n2. Subtract\n3. Multiply\n4. Divide\n")

        user_choices = (1 ,2, 3, 4)
        if user_choices == (1,2,3,4): 
            try:
                user_choice = float(input("Type your operation (1, 2, 3, 4): "))
            except ValueError:
                print("Invalid option")
                continue
        if user_choice in user_choices :
            try:
                num_1 = float(input("\nType first number: "))
                num_2 = float(input("Type second number: "))
            except ValueError: 
                print("Invalid input\nPlease type a number")
                continue

            match user_choice:
                case 1:
                    print(f"\n{num_1} + {num_2} = {(num_1+num_2)}")
                case 2:
                    print(f"\n{num_1} - {num_2} = {(num_1-num_2)}")
                case 3:
                    print(f"\n{num_1} * {num_2} = {(num_1*num_2)}")
                case 4:
                    print(f"\n{num_1} / {num_2} = {(num_1/num_2)}")
            
            if not input("\nMove to next?(y/n): ").lower() == "y":
                print("Come Again!")
                break
        
        else:
         print("Invalid option")
