def Trailing_Zeroes(x):
    count = 0
    while(True):
            if x % 10 != 0:
                    return count
            x /= 10
            count += 1
            
def Finding_Factorials():
    num = int(input("Enter a number: "))
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial*i
        print("The factorial of",num,"is",factorial)
        tmp = Trailing_Zeroes(factorial)
        print("The number of trailing zeroes is ", tmp)
Finding_Factorials() 
