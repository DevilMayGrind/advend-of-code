with open('input') as f:
    for line in f:
        if line.startswith('turn on'):
            line = line[8:]

        elif line.startswith('turn off'):
            line = line[9:]
        else:
            line = line[8:]


def draw(grid, instr: str):
    start, finish = instr.split(' through ')
    sx, sy = start.split(',')
    fx, fy = start.split(',')
    sx, sy, fx, fy = int(sx), int(sy), int(fx), int(fy)
