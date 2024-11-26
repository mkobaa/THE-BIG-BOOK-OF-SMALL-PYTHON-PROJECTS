

file = open("map.txt")

content = file.read()
ret = ""

x = input("Enter the message to display with the bitmap.");

j = 0

i = 0
while i < len(content) :
    if (content[i] == ' ') :
        ret += ' '
    elif (content[i] == '\n') :
        ret += '\n'
    else:
        ret += x[j]
        j += 1
        if j == len(x) :
            j = 0
    i += 1

print(ret)