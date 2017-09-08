"""
Lab 19: Taxes
Using the tax brackets from 2014, calculate the tax for a given income
"""


def income_tax_bracket_v1(income):
    if income <= 3350:
        return income * .05
    elif income <= 3350 + 5050:
        return (income - 3350)*.07 + 167.50
    elif income <= 3350 + 5050 + 116000:
        return (income - (5050 + 3350))*.09 + 353.50 + 167.50
    else:
        return (income - (116000 + 5050 + 3350))*.099 + 353.50 + 167.50 + 10440
# print(income_tax_bracket_v1(income))


def income_tax_bracket_v2(income):

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

        # print(f'let\'s check if income < {bracket_total}')
        if income < bracket_total:
            # print(f'we\'re in the ${bracket_cutoff} bracket')
            return (income - bracket_difference)*percent + accumulated_tax

        accumulated_tax += percent*bracket_range


def main():
    income = 130000
    print(income_tax_bracket_v1(income))
    print(income_tax_bracket_v2(income))

main()
