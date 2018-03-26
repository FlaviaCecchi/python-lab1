a = int(input("Insert the first number: "))
b = int(input("Insert the second number: "))
print("The sum is", a + b)

# SOLUTION

first_number = ""
second_number = ""
print("Hi, I will sum two integer numbers...")
while not first_number.isdigit():
    first_number = input("Please, insert a number: ")
while not second_number.isdigit():
    second_number = input("Now, insert another number: ")
result = int(first_number) + int(second_number)
print(first_number, "+", second_number, "is equal to", result)