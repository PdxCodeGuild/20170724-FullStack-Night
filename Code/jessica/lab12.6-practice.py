# 6 write a function that returns the reverse of a list
# reverse using reverse function


def reverse():
    colors = ['blue', 'green', 'purple', 'orange']
    colorsreverse = list(reversed(colors))
    print(colorsreverse)
reverse()


# reverse without using reverse function
def reverse2():
    objects = ['table', 'cup', 'phone', 'computer']
    print(objects[3], objects[2], objects[1], objects[0])
reverse2()

# list builder pattern
# xr = []
#for e in x:
#   xr.append(e)
# print(xr)

# use insert instead of append


def reverse3(nums):
    list = []
    for num in nums:
        list.insert(0, num)
    print(list)

nums = [2, 3, 8, 4, 0]
reverse3(nums)





