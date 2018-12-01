s = input()
current_sum = 0
for i in range(0, s.__len__()):
    current_symbol = s[i]
    if current_symbol == 'a':
        current_sum += 1
    elif current_symbol == 'e':
        current_sum += 2
    elif current_symbol == 'i':
        current_sum += 3
    elif current_symbol == 'o':
        current_sum += 4
    elif current_symbol == 'u':
        current_sum += 5
print(current_sum)
