import math

hall_length = float(input("Hall width: "))
hall_width = float(input("Hall length: "))
wardrobe_side = float(input("Wardrobe size: "))

hall_area = hall_length * hall_width
wardrobe_area = wardrobe_side * wardrobe_side
bench_size = hall_area / 10

free_area = hall_area - wardrobe_area - bench_size

dancer_area = 7040

dancer_count = math.floor(free_area / dancer_area)

print(dancer_count)
