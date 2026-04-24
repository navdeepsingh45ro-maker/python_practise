name =input("Enter Your Name: ")
print("Welcome", name)

def greet(name):
    print("hello",name)





while True:
    greet(name)
    choice1=int(input("Enter Number: "))
    choice2=int(input("Enter Number: "))
    choice = int(input("Enter Choice: Add(1), Subtract(2), Multiply(3), Divide(4): "))
    if choice == 1:
        print("Result: ",choice1 + choice2)
    elif choice == 2:
        print("Result: ",choice1 - choice2)
    elif choice == 3:
        print("Result: ",choice1 * choice2)
    elif choice == 4:
        print("Result: ",choice1 / choice2)
    else:
        print("Invalid Choice")
    cont= int(input("Do you want to continue? (yes(1)/no(0)): "))
    if cont ==1:
        print("Continuing...")
    else:
        print("Goodbye!")
        break


