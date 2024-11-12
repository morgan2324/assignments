#program that prints the multiplication table of a given number up to 12

num = int(input("Enter a number: "))

for i in range(1, 13):
    print(f"{num}*{i}={num * i}")