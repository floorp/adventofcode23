import re

pointCheck = {"red" : 12,
              "green": 13,
              "blue" : 14}
totalscore = 0
redvals = []
bluevals = []
greenvals = []
totalvalueGame = 0
def start():
    global totalscore
    global totalvalueGame
    totalscore = 0
    f = open("inputtest", "r")
    for line in f.readlines():

        getgameID = line.split(":")
        cleangameid = int(''.join(re.compile(r'\d').findall(getgameID[0])))
        
        dicelist = getgameID[1].split(";")
        for hands in dicelist:
            hands = hands.split(",")
            for dicecount in hands:
                dicecount = ''.join(dicecount)
                dicecount = dicecount.split(" ")
                valuecheck(dicecount, cleangameid)
              
    totalvalueGame = int(max(redvals))*int(max(bluevals))*int(max(greenvals))
    print(totalvalueGame)   
    #print("final result is {}".format(totalscore))

                        
def valuecheck(valuecheck, gameid):
    global redvals
    global bluevals
    global greenvals

    if str(valuecheck[2]) == "red" or str(valuecheck[2]) == "red\n":
        redvals.append(valuecheck[1])
    elif str(valuecheck[2]) == "blue" or str(valuecheck[2]) == "blue\n":
        bluevals.append(valuecheck[1])
    elif str(valuecheck[2]) == "green" or str(valuecheck[2]) == "green\n":
        greenvals.append(valuecheck[1])

    #print(gameid)

start()            

