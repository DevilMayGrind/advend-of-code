# Contains a pair of any two letters that appears at least
# twice in the string without overlapping
def cond1(s: str) -> bool:
    if len(s) < 4:
        return False
    for i in range(len(s)-3):
        pair = s[i: i+2]
        if pair in s[i+2:]:
            return True
    return False


# Contains at least one letter wich repeats with
# exactly one letter between them
def cond2(s: str) -> bool:
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False


with open('input', 'r') as f:
    nice_strings = 0
    for line in f:
        if cond1(line) and cond2(line):
            nice_strings += 1

    print(nice_strings)
