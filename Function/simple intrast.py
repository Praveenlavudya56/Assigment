# # Input principal amount, rate of interest, and time period
# principal = float(input("Enter the principal amount: "))
# rate_of_interest = float(input("Enter the rate of interest (as a percentage): "))
# time_period = float(input("Enter the time period (in years): "))

# # Convert the rate of interest from percentage to decimal
# rate_of_interest /= 100

# # Calculate simple interest
# simple_interest = principal * rate_of_interest * time_period

# # Calculate the total amount (principal + simple interest)
# total_amount = principal + simple_interest

# # Display the results
# print(f"Principal Amount: ${principal}")
# print(f"Rate of Interest: {rate_of_interest * 100}%")
# print(f"Time Period: {time_period} years")
# print(f"Simple Interest: ${simple_interest}")
# print(f"Total Amount: ${total_amount}")
#---------------------------------------------------------------
# Function to calculate simple interest
def calculate_simple_interest(principal, rate_of_interest, time):
    # Convert the rate of interest from percentage to decimal
    rate_of_interest /= 100
    
    # Calculate simple interest for months
    simple_interest_months = (principal * rate_of_interest * time) / 12
    
    # Calculate simple interest for years
    simple_interest_years = principal * rate_of_interest * time
    
    return simple_interest_months, simple_interest_years

# Input principal amount, rate of interest, and time period (in months)
principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (as a percentage): "))
time_months = float(input("Enter the time period (in months): "))

# Calculate simple interest for months and years
simple_interest_months, simple_interest_years = calculate_simple_interest(principal, rate_of_interest, time_months)

# Display the results
print(f"Principal Amount: ${principal}")
print(f"Rate of Interest: {rate_of_interest}%")
print(f"Time Period (months): {time_months} months")
print(f"Simple Interest (months): ${simple_interest_months:.2f}")
print(f"Simple Interest (years): ${simple_interest_years:.2f}")
