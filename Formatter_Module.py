"""
    Number Formatter Module
    Author: Joe Scott
    Started: 09-10-2025
    Purpose: Take in input and give the user a user friendly menu 
             for formatting.
"""

def nummat(num):
    # User input
    choice = input("[ Number Format Options | I = int | O = 0.0 | P = 0.00 | Q = Cancel ]: ").lower()
    try:
        if choice == "I":
            num = int(num)
        elif choice == "O":
            num = f"{num:.1f}"
        elif choice == "P":
            num = f"{num:.2f}"
        elif choice == "Q":
            print(" ! Canceled ! ")
        return num
    except:
        print("\n ! Invalid input; Enter specified command ! ")
    
    print(num)

# Example Initial

number = 2.54986
nummat(number)
