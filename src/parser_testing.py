
text = 'hello there eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee hello hehe i like pennies'

lines = []
linelength = 24

line = ''
for i in text.split():
    if len(i) + len(line) <= linelength:
        line += i + ' '
    elif len(i) > linelength:
        while len(i) > linelength:
            line += i[:linelength%len(line)]
            lines.append(line)
            line = i[linelength%len(line):linelength%len(line)+linelength]
            i = i[linelength%len(line)+linelength:]
        line += i[:linelength%len(line)]
        lines.append(line)
        line = i[linelength%len(line):linelength%len(line)+linelength] + ' '
        i = i[linelength%len(line)+linelength:]
    else:
        lines.append(line)
        line = i + ' '
if line != '':
    lines.append(line)

print('\n'.join(lines))
