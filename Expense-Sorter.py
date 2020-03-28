
text_file = open(r"transactions.csv", "r")
lines = text_file.read().split('\n')

totalSpent=0

for i in range(0, len(lines)):
  if('STEAMGAMES' in lines[i]): #do an str(input) for interactivity
    tempStr=lines[i][(int(lines[i].find('#'))+9):(int(lines[i].find('DR'))-1)]
    totalSpent += float(tempStr)
print(totalSpent)
