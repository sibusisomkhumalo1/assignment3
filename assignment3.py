def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percentage)
    
    if final_price == original_price:
        print("No discount applied. The original price is:", final_price)
    else:
        print("The final price after applying the discount is:", final_price)

except ValueError:
    print("Please enter valid numerical values.")
