# find largest prime factor of 600851475143
import math

num = 600851475143
# num = 13195

# count the number of
# times 2 divides
# while ((n % 2 > 0) == False):
        
#     # equivalent to n = n / 2;
#     n >>= 1;
#     count += 1;

# # if 2 divides it
# if (count > 0):
#     print(2, count);

# check for all the possible
# numbers that can divide it
for i in range(3, int(math.sqrt(num)) + 1):
    count = 0;
    while (num % i == 0):
        count += 1;
        num = int(num / i);
    if (count > 0):
        print(i, count);
    i += 2;

# if n at the end is a prime number.
if (num > 2):
    print(num, 1);
 

