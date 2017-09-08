# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
# if a/2 == a//2 --> 'even'
def eveneven(nums):
    even_count = 0
    for num in nums:
        if num % 2 == 0:
            even_count += 1

    return even_count % 2 == 0




def main():
    nums = ([6, 6, 2])
    print(eveneven(nums))
main()