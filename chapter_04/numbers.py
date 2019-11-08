import time

numbers = list(range(1, 6))
print("numbers: " + str(numbers))
print("sum of numbers: " + str(sum(numbers)) + "\nmin of numbers: " + str(min(numbers)) + "\nmax of numbers: " + str(
    max(numbers)))
print()

squares = []
for num in range(1, 11):
    squares.append(num ** 2)
print("squares: " + str(squares))
print("sum of squares: " + str(sum(squares)) + "\nmin of squares: " + str(min(squares)) + "\nmax of squares: " + str(
    max(squares)))
print()

odd = list(range(1, 21, 2))
print("odd: " + str(odd))
print("sum of odd: " + str(sum(odd)) + "\nmin of odd: " + str(min(odd)) + "\nmax of odd: " + str(max(odd)))
print()

even = [num * 2 for num in range(1, 11)]
print("even: " + str(even))
print("sum of even: " + str(sum(even)) + "\nmin of even: " + str(min(even)) + "\nmax of even: " + str(max(even)))
print()

start = time.perf_counter()
bigData = list(range(1, 10000001))
print("10 million's sum: " + str(sum(bigData)))
print("The first three numbers are: " + str(bigData[:4]))
print("The last three numbers are: " + str(bigData[-4:]))
print("elapse time: " + str(time.perf_counter() - start) + "s")
