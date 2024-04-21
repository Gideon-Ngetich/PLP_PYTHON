def divisible_by_ten(num):
    if num % 2 == 0:
        return True
    else:
        return False

value = int(input("Enter a value: "))
print(divisible_by_ten(value))