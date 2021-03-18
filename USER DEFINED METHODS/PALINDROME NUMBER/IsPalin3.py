#Program to check palindrome number
#With argument but without a return value (3rd Method)

def IsPalin(x): #Function Declaration

    #Function Definition [Starts]
    rev = 0 
    temp = x #Storing the original input value to keep it safe

    while x != 0: #121!=0 {T} | 12!=0 {T} | 1!=0 {T} | 0!=0 {F}
        rem = x % 10 #rem=121%10 {1} | rem=12%10 {2} | rem=1%10 {1}
        rev = rev * 10 + rem #rev=0*10+1 {1} | rev=1*10+2 {12} | rev=12*10+1 {121}
        x //= 10 #x=121//10 {12} | x=12//10 {1} | x=1//10 {0}
    
    if temp == rev: #121 is equal to 121
        print("Yes, It's a Palindrome Number.")
    else:
        print("Sorry, It's not a Palindrome Number.") 
    #Function Defintion [Ends]

IsPalin(int(input("Enter any number: "))) #Function Calling

input() #Hold the console screen