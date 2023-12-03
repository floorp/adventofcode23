
f = open("inputraw", "r")
elfdict = {}
elfHoldings = 0
elfnumber = 0
maxCalories = 0
for line in f.readlines():
    if line != "\n":
        elfHoldings = elfHoldings + int(line.strip()) 
        elfdict.update({elfnumber: elfHoldings})  
    else:
        elfHoldings = 0
        elfnumber = elfnumber + 1

for key, value in elfdict.items():
    if value >= maxCalories:
        maxCalories = value
    else:
        maxCalories = maxCalories
print(maxCalories)
