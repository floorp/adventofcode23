import re
total =0 

f = open("inputraw", "r")
for line in f.readlines():
    pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d+))')
    matches = [match.group(1) for match in pattern.finditer(line)]
    # Define a mapping from words to numbers
    word_to_number = {'one': 1, 'two': 2, 'three': 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    # Convert matched strings to integers using the mapping or keep the original string if it's a digit
    converted_values = [word_to_number.get(match, match) if not match.isdigit() else int(match) for match in matches]
    # Create a new string by joining the converted values
    result_string = ''.join(map(str, converted_values))
    print(result_string)
    fnum = re.compile(r'\d')
    a = ''.join(fnum.findall(result_string))
    if len(a) == 1:
        a = a+a
    #print(a)
    print("fixed "+a[:1]+a[-1:])
    total = total+int(a[:1]+a[-1:])
print(total)
