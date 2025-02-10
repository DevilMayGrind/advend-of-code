with open('input', 'r') as f:
    directions = f.read()
    grid = {}

    x, y = 0, 0
    grid[(x, y)] = 1
    for dir in directions:
        if dir == '^':
            y += 1
        elif dir == 'v':
            y -= 1
        elif dir == '>':
            x += 1
        elif dir == '<':
            x -= 1

        if (x, y) in grid:
            grid[(x, y)] += 1
        else:
            grid[(x, y)] = 1

    print(len(grid))
