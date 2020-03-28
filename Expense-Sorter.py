
text_file = open(r"transactions.csv", "r")
lines = text_file.read().split('\n')
fast_food = ['TACO', 'PAPA', 'DUNKIN', 'MCDONALD', 'YANGS', 'BURGER', 'STARBUCKS', 'CHINA', 'LYNDON', 'IHOP']
totalSpent=0

for i in range(0, len(lines)):
  for j in range(0, len(fast_food)):
      if (fast_food[j] in lines[i]):
          tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
          totalSpent += float(tempStr)
print(totalSpent)
