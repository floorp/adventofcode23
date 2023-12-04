import re

def _init_():
    f = open("inputraw", "r")
    final = 0
    for line in f.readlines():
        ticketnum = line.split(":")
        gamenums = ticketnum[1].split("|")
        winnums = gamenums[0].split(" ")
        playnums = gamenums[1].split(" ")
        while("" in winnums):
            winnums.remove("")
        while("" in playnums):
            playnums.remove("")
        #print(games)
        gametotal = 0
        for w in winnums:
            w = re.findall("\d+", w)
            for p in playnums:
                p = re.findall("\d+", p)
                if p == w:
                    #print("{} is a winner".format(p))
                    if gametotal == 0:
                        gametotal=1
                    else:
                        gametotal = gametotal*2
        print("{} total is {}".format(ticketnum[0],gametotal))
        final = final+gametotal    
    print(final)
_init_()