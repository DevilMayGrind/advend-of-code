with open('input', 'r') as f:
    directions = f.read()
    grid = {}
    sx, sy = 0, 0
    rx, ry = 0, 0
    grid[(0, 0)] = 1

    i = 0
    while i < len(directions):
        # Santa's move
        match directions[i]:
            case '^':
                sy += 1
            case 'v':
                sy -= 1
            case '>':
                sx += 1
            case '<':
                sx -= 1
        if (sx, sy) in grid:
            grid[(sx, sy)] += 1
        else:
            grid[(sx, sy)] = 1
        i += 1

        # Robo-Santa's move
        if i >= len(directions):
            break
        match directions[i]:
            case '^':
                ry += 1
            case 'v':
                ry -= 1
            case '>':
                rx += 1
            case '<':
                rx -= 1
        if (rx, ry) in grid:
            grid[(rx, ry)] += 1
        else:
            grid[(rx, ry)] = 1
        i += 1

    print(len(grid))
