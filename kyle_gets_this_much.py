"""You have worked for Sygma for {} years, you make ${} per hour, and you will make {}"""
dph = float(input("What was your hourly rate at Sygma?"))
years_worked = int(input("How many years did you work there?"))
print(f"After working for {years_worked} years, making ${dph} per hour, you'll get ${240*dph} in severance")
