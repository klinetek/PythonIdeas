text_file = open(r"transactions.csv", "r")
lines = text_file.read().split('\n')

fast_food = ['TACO', 'PAPA', 'DUNKIN', 'SONIC', 'MCDONALD', 'YANGS', 'BURGER', 'STARBUCKS', 'CHINA', 'LYNDON', 'IHOP', 'PIZZA', 'COUSINS', 'EVANS']
stores = ['MARSHALLS','AMAZON', 'DOLLAR', 'GOODWILL', 'FYE']
Makeup = ['KYLIE', ' MERCARI', 'BEAUTY', 'COLOURPOP', 'MAC', "THE COSMETICS CO"]

fast_food_spent=0
stores_spent = 0
MakeupSpent = 0

for i in range(0, len(lines)):
  for j in range(0, len(fast_food)):
      if (fast_food[j] in lines[i]):
          tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
          fast_food_spent += float(tempStr)
print("Fast Food " + str(fast_food_spent))

for i in range(0, len(lines)):
  for j in range(0, len(stores)):
      if (stores[j] in lines[i]):
          tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
          stores_spent += float(tempStr)
print("Stores " + str(stores_spent))

for i in range(0, len(lines)):
  for j in range(0, len(Makeup)):
      if (Makeup[j] in lines[i]):
          tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
          MakeupSpent += float(tempStr)
print("Makeup " + str(MakeupSpent))
