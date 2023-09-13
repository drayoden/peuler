# find sum of even fibonacci numbers below four million

last_two = [1,2]
MAX = 4000000
sumofEvens = 2

while True:
    print(last_two)
    nextfib = last_two[0] + last_two[1]
    if nextfib % 2 == 0:
        if nextfib < MAX:
            sumofEvens += nextfib
        else:
            break
    last_two[0] = last_two[1]
    last_two[1] = nextfib
print(f'Answer: {sumofEvens}')


