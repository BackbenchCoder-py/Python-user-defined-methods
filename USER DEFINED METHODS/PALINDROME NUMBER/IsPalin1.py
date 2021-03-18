#Program to check palindrome number
#Without argument and without return value (1st Method)

def IsPalin(): #Function Declaration
    
    #Function Definition [Starts]
    num = int(input("Enter any number: ")) #121
    rev = 0
    temp = num #Storing the original input value to keep it safe

    while num != 0: #121!=0 {T} | 12!=0 {T} | 1!=0 {T} | 0!=0 {F}
        rem = num % 10 #rem=121%10 {1} | rem=12%10 {2} | rem=1%10 {1}
        rev = rev * 10 + rem #rev=0*10+1 {1} | rev=1*10+2 {12} | rev=12*10+1 {121}
        num //= 10 #num=121//10 {12} | num=12//10 {1} | num=1//10 {0}
    
    if temp == rev: #121 is equal to 121
        print("Yes, It's a Palindrome Number.")
    else:
        print("Sorry, It's not a Palindrome Number.") 
    #Function Definition [Ends]

IsPalin() #Function Calling

input() #Hold the console screen