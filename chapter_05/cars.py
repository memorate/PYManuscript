cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

out_put = []
for num in range(1, 19):
    if num == 1:
        out_put.append("1st")
    elif num == 2:
        out_put.append("2nd")
    elif num == 3:
        out_put.append("3rd")
    elif num in range(4, 11):
        out_put.append(str(num) + "th")
print()
print(out_put)
