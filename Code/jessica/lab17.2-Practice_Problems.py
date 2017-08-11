# Print out every other element of a list, first using a while loop, then using a for loop.

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
#print(colors[::2])
i = 0
while i in range(len(colors)):
    print(colors[i])
    i += 2


for i in range(0, len(colors), 2):
    print(colors[i])
