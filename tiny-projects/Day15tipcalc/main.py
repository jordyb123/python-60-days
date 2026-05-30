def main():
    bill = float(input("Enter the bill amount: "))
    tip_percent = float(input("Enter the tip percentage amount: "))
    people = int(input("Enter the amunt of people splitting the bill: "))

    tip = calculate_tip(bill, tip_percent)
    print(f"Tip: ${tip:.2f}")

    total = calculate_total(bill, tip)
    print(f"Total: ${total:.2f}")

    split = split_bill(total, people)
    print(f"Bill split between {people}: ${split:.2f}")

def calculate_tip(bill, tip_percent):
    tip = bill * (tip_percent / 100)
    return tip

def calculate_total(bill, tip):
    total = bill + tip
    return total

def split_bill(total, people):
    split = total / people
    return split

main()