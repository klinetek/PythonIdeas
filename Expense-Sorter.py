import timeit

text_file = open(r"transactions.csv", "r")
lines = text_file.read().split('\n')

fast_food = ['TACO', 'PAPA', 'DUNKIN', 'SONIC', 'MCDONALD', 'YANGS', 'BURGER',
            'STARBUCKS', 'CHINA', 'LYNDON', 'IHOP', 'PIZZA', 'COUSINS', 'EVANS']
stores = ['MARSHALLS','AMAZON', 'DOLLAR', 'GOODWILL', 'FYE']
makeup = ['KYLIE', ' MERCARI', 'BEAUTY', 'COLOURPOP', 'MAC', "THE COSMETICS CO"]

fast_food_spent=0
stores_spent = 0
makeup_spent = 0
nsffeesspent = 0

for i in range(0, len(lines)):
     if('NSF' in lines[i]):
         tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
         nsffeesspent += float(tempStr)
print("Fee's " + str(nsffeesspent))

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
  for j in range(0, len(makeup)):
      if (makeup[j] in lines[i]):
          tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
          makeup_spent += float(tempStr)
print("makeup " + str(makeup_spent))
#break
print("\tKyles Version ======================================================<3")
#this version is harder on RAM because of all the splits

text_file = open(r"transactions.csv", "r")
lines = text_file.read().split('\n')

#def kyleIsAwsome():
nlist = ["TACO,PAPA,DUNKIN,SONIC,MCDONALD,YANGS,BURGER,STARBUCKS,CHINA,LYNDON,IHOP,PIZZA,COUSINS,EVANS","MARSHALLS,AMAZON,DOLLAR,GOODWILL,FYE","KYLIE,MERCARI,BEAUTY,COLOURPOP,MAC,THECOSMETICSCO"]
fast_food_spent=0
stores_spent = 0
makeup_spent = 0

for i in range(0, len(lines)):
    for j in range(0, len(nlist)):
        tempList = nlist[j].split(',')
        for k in range(0,len(tempList)):
            if (tempList[k] in lines[i]):
                tempStr=lines[i][(int(lines[i].find('$'))+1):(int(lines[i].find(')'))-1)]
                if(j==0):
                    fast_food_spent += float(tempStr)
                elif(j==1):
                    stores_spent += float(tempStr)
                else:
                    makeup_spent += float(tempStr)
print("Fast Food " + str(fast_food_spent))
print("Stores " + str(stores_spent))
print("makeup " + str(makeup_spent))
#def main():
    #timeit.timeit(kyleIsAwsome, 100)

#if __name__ == "__main__":
    #main()
