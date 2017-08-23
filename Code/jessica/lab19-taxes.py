income = int(input('Enter your income: '))


def incometax_bracket(income):
    if income <= 3350:
        return income * .05
    elif income <= 3350 + 5050:
        return (income - 3350) * .07 + 167.50
    elif income <= 116000 + 5050 + 3350:
        return (income - 5050 - 3350) * .09 + 353.50 + 167.50
    else:
        return (income - 116000 - 5050 - 3350) * .099 + 353.50 + 167.50 + 10440
incometax_bracket(income)
print(incometax_bracket(income))


def tax_brackets(income):
    brackets = [
        (3350, 0.05),
        (5050, 0.07),
        (116000, 0.09),
        (float('inf'), 0.099),
        ]
    bracket_total = 0
    accumulated_tax = 0
    for bracket in brackets:
        bracket_range = bracket[0]
        percent = bracket[1]

        bracket_difference = bracket_total
        bracket_total += bracket_range

        if income < bracket_total:
            return (income - bracket_difference) * percent + accumulated_tax

        accumulated_tax += percent*bracket_range


print(tax_brackets(income))
