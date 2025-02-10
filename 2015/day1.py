with open('input1', 'r') as file:
    content = file.read()

current_floor = 0

for ch in content:
    if ch == '(':
        current_floor += 1
    elif ch == ')':
        current_floor -= 1

print(current_floor)
