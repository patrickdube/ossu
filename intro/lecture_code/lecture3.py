i = 0
where = input("Go left or go right?")
while where == "right":
    where = input("Go left or go right?")
    i += 1
    print(i)
    if i > 2:
        print(":(")
print("You got out!")
