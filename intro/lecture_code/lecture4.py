secretNumber = 4
numbers = range(1, 11)
found = False
for number in numbers:
    if number == secretNumber:
        print(number)
        found = True
        break
if not found:
    print("not found")
