# Lab 19    Taxes


def tax_bracket(gross_income):
    count_index = 0
    #tax_income_bracket = [3350, 5050, 116000]
    tax_percentage = [.05, .07, .09, .099]
    taxes = 0

    if gross_income >= 3350:
        taxes += (3350 * tax_percentage[count_index])
        count_index += 1
        gross_income -= 3350
    elif gross_income < 3350:
        taxes += (gross_income * tax_percentage[count_index])
        return taxes
    if gross_income >= 5050:
        taxes += (5050 * tax_percentage[count_index])
        count_index += 1
        gross_income -= 5050
    elif gross_income < 5050:
        taxes += (gross_income * tax_percentage[count_index])
        return taxes
    if gross_income >= 116000:
        taxes += (116000 * tax_percentage[count_index])
        count_index += 1
        gross_income -= 116000
    elif gross_income < 116000:
        taxes += (gross_income * tax_percentage[count_index])
        return taxes
    if gross_income > 0:
        taxes += (gross_income * tax_percentage[count_index])
        return taxes


def main():
    gross_income = int(input('Enter you gross income: '))
    print('You owe $' + str(tax_bracket(gross_income)) + ' in taxes.')


main()
