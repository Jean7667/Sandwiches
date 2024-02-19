users = ['rob', 'jack', 'Jo', 'mark','Sean','Jim']

data = ['Jo', 43,True]

empty_list = []


# check if you are in the list
print ('Jo' in users)

#list start at 0 index

print(users[0])

print(users[-2])

# index from the end
print(users[-1])

#give the index
print(users.index('rob'))

#want a range of value
print(users[0:3])
# ?
print(users[-3:-1])

print (len(data))
# added elsa
users.append('elsa')
print (users)

# adding to another list
users += ['Jason']
print(users)
# users += 'Jason'

users.extend(['Robert','Jacky','Fab'])

print(users)

# items are added at the end of the list 

users.insert(0, 'Bob')
print(users)
#insert 2 values in the users list  at position 2 
# start and end at 2 push the value without deleting it
users[2:2] = ['Eddie','Alex']
print(users)
### Slice method
users[1:3] = ['Robers','JPG']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)









