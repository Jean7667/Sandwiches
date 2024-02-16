""" value = 1 
while value < 10:
    print(value)
    if value == 5:
        break
    value +=1 """
 
""" while value <= 10:
   value += 1
   if value == 5:
      continue
   print(value)
else:
   print("value is now equal to " + str(value)) """
   

names = ["dave", "Sara", "Jean", "Jack"]

""" for names in names: 
    print (names)

for i in "Jeanbaptiste":
    print(i)    """

# in this example the for loop stop when it find Jean and print each name before 
for name in names:
    if name == "Jean":
        break
    print(name)

# in this example the for loop stop on the name Jean and print the name before and after
""" for name in names:
    if name == "Jean":
        continue
    print(name)
# for loop between 0 and 8
for x in range(9):
    print(x)
# it won't include the last number 
for x in range(1,5):
    print(x)

for x in range(1,30,10):
    print(x),

for i in range(0,100,10):
    print([i], end =" ")  """

"""If you want to print all the values of x on a single line in Python, you can use the end parameter of the print() function to specify what character to print at the end of the line. By default, end is set to '\n', which means a newline character. You can change it to an empty string to print everything on the same line."""


for x in range(0, 101, 5):
    print(x, end='|')

print("\n", end='')

for x in range(0, 101, 3):
    print(x, "\n", end='|')
    
else: print ("Python is cool that\'s it")

print("\n", end='')

print("*.*" * 10) 
#for x in range(0, 101, 5):
#    print(x, end='  ')
#   print("\n", end='')  # This prints a newline character after each value of x
#   print("-" * 2)  # This prints a line separator after each value of x

# help(print) end='space' to print in line - parameter of print fct

# nested loops 

names = ["dave", "Sara", "Jean", "Jack"]
actions = ["eats", "sleeps", "codes", "runs","plays"]
obj = ["with his knife", "in your bed", "outside", "tennis"]

for name in names :
    for action in actions :
        for objet in obj :
            print (name + ' ' + action + ' ' + objet , end='   ')

# add code to remove all the n

# Initialize an empty list to store the values
result_array = []

# Iterate through the range and append each value to the list
for x in range(0, 101, 5):
    result_array.append(x)

# Print the resulting array
print(result_array)

#
""" def validate_data(values):
    """
    check format of data
    converts all strings values into int 
    raises value erroe if strings cannont be converted
    """
    #print(values)
    try:
        if len(values) != 6:
            raise ValueError(  
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
"""
#e shorthand error python - review

# convert String in Integer
Array_of_String = ['3','6','6','9','99','56','67','43']
[int(value) for value in Array_of_String]
#same as loop

