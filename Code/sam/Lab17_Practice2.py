list = ['1', '2', '3', '4', '5']
every_other = []
every_other2 = []
i = 0

while i < len(list):                    # creating a while loop with length of list
    every_other.append(list[i])

    i += 2                              # iterating over every other element

print(every_other)

for i in range(0, len(list), 2):        # in range 0-length of list with an increment of 2
    every_other2.append(list[i])



print(every_other)
