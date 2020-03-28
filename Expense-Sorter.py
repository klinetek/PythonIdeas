
text_file = open(r"transactions.csv", "r")
lines = text_file.read().split('\n')
fast_food = ['TACO', 'PAPA', 'DUNKIN', 'MCDONALD', 'YANGS', 'BURGER', 'STARBUCKS', 'CHINA', 'LYNDON', 'IHOP']
totalSpent=0

for i in range(0, len(lines)):
<<<<<<< HEAD
  if (0, len(fast_food[i])):
      for i in range (0, len(lines[i])):
          tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
          totalSpent += float(tempStr)
=======
  if('WAWA' in lines[i]): #do an str(input) for interactivity
    tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
    totalSpent += float(tempStr)
>>>>>>> 5461467be9bed31a60d990725033610557b42d55
print(totalSpent)
