# highly divisible triangular number

# NOTE: ran on 09/10/2023 -- started run at j = 5400. To get final 
#       answer of first triangle number to have over 500 divisors:
#       Triangle number 12375
#       value: 76576500 with 576 divisors!
# This answer took around 2 1/2 to 3 hours to complete!

# create some triangle numbers:

# n = 10 # nth triangle number

done = False
j = 5400
maxdivs = 500

def divisors(x):
    divs = 0
    for i in range(1,x+1):
        if x % i == 0:
            divs += 1
    return divs

tdivs = 0
while not done:
    tnum = j * (j+1) // 2
    divs = divisors(tnum)
    if divs >= tdivs:
        print(f'{j} -- {tnum} -- divisors: {divs}')
        tdivs = divs
    j += 1
    if divs > maxdivs:
        print(f'We have a winner!')
        done = True




