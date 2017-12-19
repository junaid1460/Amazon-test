from collections import Counter

while True:
    try:
        s = input().strip()
    except:
        break
    tmp = iter(s)
    next(tmp)
    tmp = zip(iter(s), tmp)
    counts = Counter(s)
    killedMissionaries = 0
    skip = False
    for x, y in tmp:
        if x != y and not skip:
            killedMissionaries += 1
            skip = True
            continue
        skip = False
    
    counts['m'] -= killedMissionaries
    m, b = counts['m'], counts['c']
    if m == b:
        print('tie')
    elif m > b:
        print('missionaries')
    else:
        print('cannibals')