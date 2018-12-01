n = int(input())

maximum_num = int(input())

for i in range(1, n):
    current_num = int(input())
    if current_num > maximum_num:
        maximum_num = current_num
print(maximum_num)
