#Sum from 1 to given upper bound

n = int( input(" Enter then upper bound : " ))

i = 1
sum = 0

while (i <=n):
    sum += i
    i += 1

print("Sum of Numbers from 1 to UpperBound : ", n , "provided is : " , sum)
