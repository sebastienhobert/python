def generate_multiplication_table(number, up_to=10):
    print(f"Multiplication Table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    # input: get the number from the user
    number = int(input("Enter a number to generate its multiplication table: "))

    # optionally, get the range up to which the table should be generated
    up_to = input("Enter the range (default is 10): ")
    up_to = int(up_to) if up_to else 10

    # generate and display the multiplication table
    generate_multiplication_table(number, up_to)