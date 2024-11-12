#python program that takes list of integers as input and returns a list of even numbers.

nums= input("Enter a list of integers:").split()

even_numbers=[]

for num in nums:
    if int(num) % 2 == 0:
        even_numbers.append(int(num))
        
        print("Even numbers:", even_numbers)

