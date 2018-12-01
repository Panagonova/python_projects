import math

n = int(input())
left_sum = 0
right_sum = 0
for i in range(1, n + 1):
    current_num = int(input())
    left_sum += current_num
for i in range(1, n + 1):
    current_num = int(input())
    right_sum += current_num

sum_diff = left_sum - right_sum
sum_mod = math.fabs(sum_diff)

if sum_diff == 0:
    print(f"Yes {left_sum}")
else:
    print("No %i" % sum_mod)
