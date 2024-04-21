def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = price - (price * discount_percent / 100)
        return discount_percent
    else:
        return price
    
def main():
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if final_price != original_price:
        print("The final price is ", final_price)
    else:
        print("The original price is ", original_price)
        

main()