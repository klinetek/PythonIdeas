
text_file = open(r"transactions.csv", "r")
lines = text_file.read().split('\n')
totalSpent=0
#date, vendor_name, type, empty, cost+/-
for i in range(0, len(lines)):
  if('CMSVEND*CV HARRISBURG MIDDLETOWN PA' in lines[i]):
    tempStr=lines[i]

    #totalSpent += double(lines[i])
print(tempStr)
