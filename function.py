def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = discount_percent * price / 100
        return price
    return price
price = input("Enter the original price: ")
discount = input("Enter the discount rate: ")

price = int(price)
discount = int(discount)

print(calculate_discount(price, discount))
