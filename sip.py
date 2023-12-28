# Defining a function to calculate the maturity amount of a SIP investment
def sip_calculator(amount, years, rate):
  # Convert the yearly rate to monthly rate
  monthly_rate = rate / 12 / 100
  # Calculate the number of months
  months = years * 12
  # Apply the formula for future value of an annuity
  maturity_amount = amount * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate)) / monthly_rate
  # Round the result to two decimal places
  maturity_amount = round(maturity_amount, 2)
  # Return the maturity amount
  return maturity_amount

# Ask the user for the input values
amount = float(input("Enter the monthly SIP amount: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the yearly rate of return: "))

# Call the function and print the result
maturity_amount = sip_calculator(amount, years, rate)
print(f"The expected amount you will get is: {maturity_amount}")
