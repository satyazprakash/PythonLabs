# while loop example
''' while loop simply repeats as long as a certain boolean condition is met
'''

count = 0

while count < 5 :
    print (count)
    count +=1   # this is the same as count = count +1 

# this is how you would break a loop
''' Break is used to exit a loop whether
the loop is while or for loop
'''

#prints out 0,1,2,3,4,

count = 0
while True:
    print(count)
    count +=1
    if count>=5:
        break


