# Contain at least three vowels
def cond1(s: str) -> bool:
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
    return count >= 3


# Contains at least one letter that appears twice in a row
def cond2(s: str) -> bool:
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            return True
        i += 1
    return False


# Does not contain the strings: ab, cd, pq, xy
def cond3(s: str) -> bool:
    if ('ab' in s) or ('cd' in s) or ('pq' in s) or ('xy' in s):
        return False
    return True


with open('input', 'r') as f:
    line = f.readline()
    nice_string = 0
    while line != '':
        if cond1(line) and cond2(line) and cond3(line):
            nice_string += 1
        line = f.readline()

print(nice_string)
