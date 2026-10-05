# WAP to check weather the age is
# valid and eligible for voting or not 

age = int(input("Enter the age :"))

if age >= 18:
    print("Eligible for Voting")
elif age <= 18:
    print(" Not Eligible for Voting")
else:
    print("Invalid age")