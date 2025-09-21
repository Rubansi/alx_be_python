# multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# loop from 1 to 10 and display table
for num in range(1, 11):
    product = number * num
    print(f"{number} * {num} = {product}")