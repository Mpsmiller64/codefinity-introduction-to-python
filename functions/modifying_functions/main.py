def apply_discount(price, discount=0.05):
    disc_price = price - price * discount
    return(disc_price)
def apply_tax(price, tax=0.07):
    tax_price = price + price * tax
    return(tax_price)
def calculate_total(price, discount=.05, tax=.07):
    total_price = apply_tax(price, tax)
    total_price = apply_discount(total_price,discount)
    return(total_price)
################################################
total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${total_price_default}")
total_price_custom = calculate_total(100, .10,.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")