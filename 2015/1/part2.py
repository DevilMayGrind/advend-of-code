with open('input1', 'r') as file:
    content = file.read()

floor = 0
ch_pos = 0
while floor != -1:
    if content[ch_pos] == '(':
        floor += 1
    elif content[ch_pos] == ')':
        floor -= 1
    ch_pos += 1

print(ch_pos)
