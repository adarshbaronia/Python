card_number = list(input("Enter the card number: ").strip())

check_digit = card_number.pop()

card_number.reverse()
processed_digit = []

for index, digit in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(float(digit)) * 2

        if doubled_digit > 9:
            doubled_digit = doubled_digit - 9

        processed_digit.append(doubled_digit)

    else:
        processed_digit.append(int(digit))

total = sum(processed_digit) + int(check_digit)
if total % 10 == 0:
    print('Valid Credit Card Number!')
else:
    print("Not A Valid Card Number!")
