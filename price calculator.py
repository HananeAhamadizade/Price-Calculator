
# GitHub Repository: https://github.com/HananeAhamadizade/Price-Calculator
def calculate_price(price, tax_rate=0.1):
    final_price = price * (1 + tax_rate)
    return final_price


def main():
    price = float(input())
    tax_input = input()

    if tax_input:
        tax_rate = float(tax_input)
        result = calculate_price(price, tax_rate)
    else:
        result = calculate_price(price)

    print(result)


main()
