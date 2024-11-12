#program to find the largest number in a list without using max() function

nums = list(map(int, input("Enter a list of numbers: ").split()))

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num
        
        print("The largest number is:", largest)
        