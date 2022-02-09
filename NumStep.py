
enterNum = int(input("enter a number : "))
numbers = [10,100,1000,10000]
i = 0
newHighest = 0
for i in range(len(numbers)):
    if enterNum >= numbers[i]:
        newHighest = numbers[i]
    else:
        pass

print(newHighest)