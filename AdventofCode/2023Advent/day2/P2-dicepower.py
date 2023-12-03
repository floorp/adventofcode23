import re
#the goal is to find which games could have equal to or less than 12R, 13G, 14B cubes per game
#will need to find the maximum amount of dice per color is pulled per game and compare it against the goal
#throw out the other results and add up the numerical value of the game IDs

pointCheck = {"red" : 12,
              "green": 13,
              "blue" : 14}
totalscore = 0
passcheck = []
redvals = 0
bluevals = 0
greenvals = 0
totalvalueGame = 0
totalvalueAll = 0
def start():
    global totalscore
    global passcheck
    global totalvalueGame
    global totalvalueAll
    global redvals
    global bluevals
    global greenvals
    totalscore = 0
    f = open("inputraw", "r")
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
        totalvalueGame = int(redvals)*int(bluevals)*int(greenvals)
        redvals = 0
        bluevals = 0
        greenvals = 0
        print("totalvalueGame = {}".format(totalvalueGame))
        totalvalueAll = totalvalueAll + totalvalueGame 
    print("totalvalueall = {}".format(totalvalueAll))
    print(totalvalueAll)   

                        
def valuecheck(valuecheck, gameid):
    global passcheck
    global redvals
    global bluevals
    global greenvals

    if str(valuecheck[2]) == "red" or str(valuecheck[2]) == "red\n":
        if int(valuecheck[1]) > redvals:
            redvals = int(valuecheck[1])
    elif str(valuecheck[2]) == "blue" or str(valuecheck[2]) == "blue\n":
        if int(valuecheck[1]) > bluevals:
            bluevals = int(valuecheck[1])
    elif str(valuecheck[2]) == "green" or str(valuecheck[2]) == "green\n":
        if int(valuecheck[1]) > greenvals:
            greenvals = int(valuecheck[1])


start()            

