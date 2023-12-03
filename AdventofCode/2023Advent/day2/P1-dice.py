import re
#the goal is to find which games could have equal to or less than 12R, 13G, 14B cubes per game
#will need to find the maximum amount of dice per color is pulled per game and compare it against the goal
#throw out the other results and add up the numerical value of the game IDs

pointCheck = {"red" : 12,
              "green": 13,
              "blue" : 14}
totalscore = 0
passcheck = []
#open input file and read values
    #maybe assign them to a dict with the max number of dice?
def start():
    global totalscore
    global passcheck
    totalscore = 0
    f = open("inputraw", "r")
    for line in f.readlines():
        getgameID = line.split(":")
        cleangameid = int(''.join(re.compile(r'\d').findall(getgameID[0])))
        
        passcheck[:] = []
        dicelist = getgameID[1].split(";")
        for hands in dicelist:
            hands = hands.split(",")
            #print(hands)
            for dicecount in hands:
                dicecount = ''.join(dicecount)
                dicecount = dicecount.split(" ")
                valuecheck(dicecount, cleangameid)
        
        if "fail" not in str(passcheck):
            #print(cleangameid)
            #print(str(passcheck))
            totalscore = totalscore + cleangameid
                
    print("final result is {}".format(totalscore))

                        
def valuecheck(valuecheck, gameid):
    global passcheck
    if str(valuecheck[2]) == "red" or str(valuecheck[2]) == "red\n":
        if int(valuecheck[1]) > 12:
            passcheck.append("fail")
        else:
            passcheck.append("pass")
    elif str(valuecheck[2]) == "blue" or str(valuecheck[2]) == "blue\n":
        if int(valuecheck[1]) > 14:
            passcheck.append("fail")
        else:
            passcheck.append("pass")
    elif str(valuecheck[2]) == "green" or str(valuecheck[2]) == "green\n":
        if int(valuecheck[1]) > 13:
            passcheck.append("fail")
        else:
            passcheck.append("pass")
    #print(gameid)

start()            

