with open('input', 'r') as file:
    total_area = 0
    line = file.readline()
    while line != "":
        l, h, w = line.split('x')
        l, h, w = int(l), int(h), int(w)
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        total_area += area + slack
        line = file.readline()
print(total_area)
