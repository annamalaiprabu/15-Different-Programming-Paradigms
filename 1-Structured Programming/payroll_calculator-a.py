user_name = input("Please enter your name or enter 0 to exit the Payroll Calculator : ")
num_of_work_hours_per_week = 40
while user_name != "0": 
    num_of_hours_worked = int(input("Please enter the number of hours worked : ")) #manually typecast here as int as otherwise it is considering the inputas a string and not allowing to perform arithmetic operations b/w them
    hourly_rate = int(input("Please enter your hourly rate : "))

#round function -- round(num_to_be_rounded,upto how many places) if no places given for 2nd parameter; <5 in decimal then rounds off to previous number and >=5 rounds off to next number  

    if num_of_hours_worked < 40:
        base_pay = num_of_hours_worked * hourly_rate
        extra_pay = 0
        gross_pay = base_pay
        print("The base pay for",user_name,base_pay)
        print("The extra pay for",user_name,extra_pay)
        print("The gross pay for",user_name,gross_pay)
    
    else:
        base_pay = 40 * hourly_rate
        extra_pay = (num_of_hours_worked-40) * hourly_rate
        gross_pay = base_pay + extra_pay
        print("The base pay for",user_name,base_pay)
        print("The extra pay for",user_name,extra_pay)
        print("The gross pay for",user_name,gross_pay)
    
    user_name = input("Please enter your name or enter 0 to exit the Payroll Calculator : ")

print("You have successfully exited from the Payroll Calculator")


    
    
