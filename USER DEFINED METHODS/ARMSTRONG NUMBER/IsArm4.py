#Program to check whether a number is Armstrong or not
#With argument but without a return value. (3rd Method)

def IsArm(x): #Function Declaration | suppose, x = 153
    #Function Definition [Starts]
    arm=0
    temp=x #Storing the original input value to keep it safe

    while x!=0: #153!=0 {T} | 15!=0 {T} | 1!=0 {T} | 0!=0 {F}
        rem = x % 10 #rem=153%10 {3} | rem=15%10 {5} | rem=1%10 {1}
        arm = arm + rem * rem * rem #arm=0+3*3*3 {27} | arm=27+5*5*5 {152} | arm=152+1*1*1 {153}
        x //= 10 #x=153//10 {15} | x=15//10 {1} | x=1//10 {0}

    if temp == arm: #153 is equal to 153 {T}
        return True
    else:
        return False
    #Function Defintion [Ends]

if IsArm(int(input("Enter any number: ")))==True: #Function Calling
    print("Yes, It's an Armstrong number.")
else:
    print("Sorry, It's not an Armstrong number.")

input() #Hold the console screen