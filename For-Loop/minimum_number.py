n = int(input())

minimum_num = int(input())

for i in range(1, n):
    current_num = int(input())
    if current_num < minimum_num:
        minimum_num = current_num
print(minimum_num)
