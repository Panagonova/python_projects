first_name = input("enter first name: ")
last_name = input("enter last name: ")
age = int(input("enter age: "))
town = input("enter town: ")

# float() int() str() %d
print(f'You are {first_name} {last_name}, a {age}-years old person from {town}.')
print('You are %s %s, a %d-years old person from %s.' % (first_name, last_name, age, town))
