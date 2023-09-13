# find the largest palendrome made from the product of two three digit numbers

pnum = 0

def palnum(n):
    strnum = str(n)
    lnum = len(strnum) -1
    for i in range(0, len(strnum)):
        if strnum[i] == strnum[lnum]:
            lnum -= 1
        else: return False
    return True

for i in range(100, 1000):
    for y in range(100, 1000):
        p = i * y 
        # print(f'i: {i}  x   y: {y}  =  {p}')
        if palnum(p):
            if p > pnum:
                pnum = p
            print(f'{p} is a PALENDOME!')

print(f'Largest palendrome: {pnum}')
