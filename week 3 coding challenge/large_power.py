def large_power(base, exponent):
    if pow(base, exponent) > 5000:
        return True
    else:
        return False

base_value = int(input("Enter the base: "))
exponent_value = int(input("Enter the exponent: "))
print(large_power(base_value, exponent_value))