user_input = input('Type your word. ')
ui_doubled = ''

i = 0
while i < len(user_input):
    ui_doubled += user_input[i] * 2         # adding index of user_input * 2 to ui_doubled
    i += 1

print(ui_doubled)

