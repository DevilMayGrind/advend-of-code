with open('input', 'r') as file:
    line = file.readline()
    total = 0
    while line != '':
        l, h, w = line.split('x')
        l, h, w = int(l), int(h), int(w)
        smallest_perimeter = l*2 + h*2 + w*2 - max(l, h, w)*2
        volume = l*h*w
        total += smallest_perimeter + volume
        line = file.readline()
    print(total)
