# sum square difference

sumOs = 0
sqrOs = 0

for x in range(1,101):
    sumOs += x ** 2
    sqrOs += x
    print(f'{sumOs}:{sqrOs}')

print(f'result: {sqrOs ** 2} - {sumOs} = {(sqrOs ** 2) - sumOs} ')
