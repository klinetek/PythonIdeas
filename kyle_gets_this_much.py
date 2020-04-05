"""You have worked for Sygma for {} years, you make ${} per hour, and you will make {}"""
print("What was your hourly rate at Sygma?")
dph = float(input())
print("How many years did you work there?")
years_worked = int(input())
print("After working for {} years, making ${} per hour, you'll get ${} in severance".format(years_worked, dph, 240*dph))
