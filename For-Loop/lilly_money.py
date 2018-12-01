years_Lilly = int(input())
price_game = float(input())
peralnq_coast = float(input())
sum_money = 0

for i in range(1, years_Lilly + 1):
    if i % 2 != 0:
        sum_money += price_game
    else:
        sum_money += 5*i - 1
print(sum_money)
print(peralnq_coast - sum_money)
