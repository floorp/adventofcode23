import re
valuedict = {"one" : 1,
             "two" : 2,
             "three" : 3,
             "four" : 4,
             "five" : 5,
             "six" : 6,
             "seven" : 7,
             "eight" : 8,
             "nine" : 9
             }
total = 0
f = open("inputtest", "r")
for line in f.readlines():
    for key in valuedict:
        if line.__contains__(key):
            line = re.sub(key, str(valuedict[key]), line)
            #print(line)
    fnum = re.compile(r'\d')
    a = ''.join(fnum.findall(line))
    if len(a) == 1:
        a = a+a
    #print(a)
    print("fixed "+a[:1]+a[-1:])
    total = total+int(a[:1]+a[-1:])
print(total)