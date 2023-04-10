# get two integer parameters
# return sum
def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def mul(x, y):
    return x*y

def div(x, y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus, 2:minus, 3:mul, 4:div")
        check = int(input())
        
        if check == 1:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", plus(x,y))
            
        elif check == 2:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", minus(x,y))
            
        elif check == 3:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", mul(x,y))
            
        elif check == 4:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            if y != 0:
                print("answer : ", div(x,y))
            else:
                print("Error : Enter a non-zero number for division")
            
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
