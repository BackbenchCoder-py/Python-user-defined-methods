#Program to check whether a number is Armstrong or not
#Without argument and without return value. (1st Method)

def IsArm(): #Function Declaration
    #Function Definition [Starts]
    num=int(input("Enter any number: ")) # num = 153
    arm=0
    temp=num #Storing the original input value to keep it safe

    while num!=0: #153!=0 {T} | 15!=0 {T} | 1!=0 {T} | 0!=0 {F}
        rem = num % 10 #rem=153%10 {3} | rem=15%10 {5} | rem=1%10 {1}
        arm = arm + rem * rem * rem #arm=0+3*3*3 {27} | arm=27+5*5*5 {152} | arm=152+1*1*1 {153}
        num //= 10 #num=153//10 {15} | num=15//10 {1} | num=1//10 {0}

    if temp == arm: #153 is equal to 153 {T}
        print("Yes, It's an armstrong number.")
    else:
        print("Sorry, It's not an armstrong number.")
    #Function Defintion [Ends]

IsArm() #Function Calling

input() #Hold the console screen