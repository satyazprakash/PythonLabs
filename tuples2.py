#Tuples in Python
''' Tuples are immutalbe which means we cannnot
update or change values of tuples elements
we can change the values of tuple elements to create a
new tumpe '''

tup1 =(12, 34, 56);
tup2 =('abc', 'xyz');

# following action is not avlid for tuples
#tup1[0] = 100;

#so lets create a new tuple as follow

tup3= tup1 + tup2
print(tup3)

# this is how you would delete a tuple

del tup3

print (tup3)
