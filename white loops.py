i = 1
while i <= 10:
    print(i * "*" )
    i = i + 1

names = [ "Musa", "Kofi", "David", "john", "fred" ]
print(names[2])
print(names[-2])
names[0] = "Dog"
print(names)
print(names[1: 3])

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)
numbers.append(6)
numbers.remove(3)
print(numbers)
print(1 in numbers)
print(len(numbers))
for item in numbers:
    print(item)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i - 1

