principal = float(input("Please enter the principal amount : ")) # while taking inputs from the users we need to mention the datatype explicitly
rate_of_interest = float(input("Please enter the rate of interest in decimal : "))
time_in_years = float(input("Please enter the time in years : "))
total_amount = principal * pow((1 + (rate_of_interest/100)),time_in_years)
compound_interest = total_amount - principal
print("Therefore the compound interest is ",compound_interest)