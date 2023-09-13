# special pythagorean triplet

from itertools import combinations
from sys import exit

nums = range(199,426)
gsum = 1000
count = 0

for seq in combinations(nums,3):
    # test for the correct sum:
    # print(f'{seq}:{sum(seq)}')
    if sum(seq) == gsum:
        print(f'sum of {gsum}: {seq}')
        count += 1
        sqrs = (seq[0]**2,seq[1]**2,seq[2]**2)
        print(f'     squares: {sqrs}')
        # test for a^2 + b^2 = c^2
        if (sqrs[0] + sqrs[1]) == sqrs[2]:
            print(f'      Haazah! -- {seq} -- {count}')
            print(f'      product of seq: {seq[0]*seq[1]*seq[2]}')
            exit()

print(f'Done... {count}')




