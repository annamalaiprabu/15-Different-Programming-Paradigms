num = int(input("Please enter the number you want to be reversed : "))
lastDigit = 0
revNum = 0
while num > 0 :
    lastDigit = num % 10
    revNum = revNum * 10 + lastDigit
    num = num/10
    num = int(num) #this is a very important step otherwise the num will never become 0 as it will consider the num as a float and keep accomodating the new decimal values
#be wary of how the program works and imagine the dry run for python and then only code; don't directly copy a program for C++ onto Python and expect it to work
print("The reversed number is ",revNum)
