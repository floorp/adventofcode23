import re
#the goal is to find which games could have equal to or less than 12R, 13G, 14B cubes per game
#will need to find the maximum amount of dice per color is pulled per game and compare it against the goal
#throw out the other results and add up the numerical value of the game IDs

pointCheck = {"red" : 12,
              "green": 13,
              "blue" : 14}
totalscore = 0
passcheck = []
redvals = []
bluevals = []
greenvals = []
totalvalueGame = 0
def start():
    global totalscore
    global passcheck
    global totalvalueGame
    totalscore = 0
    f = open("inputtest", "r")
    for line in f.readlines():

        getgameID = line.split(":")
        cleangameid = int(''.join(re.compile(r'\d').findall(getgameID[0])))
        
        #passcheck[:] = []
        dicelist = getgameID[1].split(";")
        for hands in dicelist:
            hands = hands.split(",")
            for dicecount in hands:
                dicecount = ''.join(dicecount)
                dicecount = dicecount.split(" ")
                #print(dicecount[1])
                #print(dicecount[2])
                valuecheck(dicecount, cleangameid)
        
        #if "fail" not in str(passcheck):
            #print(cleangameid)
            #print(str(passcheck))
            #totalscore = totalscore + cleangameid
    totalvalueGame = int(max(redvals))*int(max(bluevals))*int(max(greenvals))
    print(totalvalueGame)   
    #print("final result is {}".format(totalscore))

                        
def valuecheck(valuecheck, gameid):
    global passcheck
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

