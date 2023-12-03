import re
total = 0
f = open("inputraw", "r")
for line in f.readlines():
    fnum = re.compile(r'\d')
    a = ''.join(fnum.findall(line))
    if len(a) == 1:
        a = a+a
    # print(a)
    # print("fixed "+a[:1]+a[-1:])
    total = total+int(a[:1]+a[-1:])
print(total)
