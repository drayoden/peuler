# Longest Collatz Sequence

startNum = 999999
maxlen = 0
maxterms = []

for n in range(startNum,0,-1):
    term = n
    terms = [term]
    while term != 1:
        if term % 2 == 0: # even
            term = int(term/2)
        else:
            term = (3 * term) + 1
        terms.append(term)
        # print(terms)
        # print(term)
    lterms = len(terms)
    print(f'{n}: [{lterms}]')
    if lterms > maxlen:
        maxlen = lterms
        maxterms = terms
    terms = []

print()
print(f'n:{maxterms[0]}: {maxterms} -- [{maxlen}]')
        
# n = 837799 produces 525 terms! Amazing!