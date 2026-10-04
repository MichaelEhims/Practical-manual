#Exercise 1
def square_list(numbers):
    result = []

    for number in numbers:
        square = number * number
        result.append(square)

    return result

print(square_list([1, 2, 3, 4]))

#Exercise 2
# 1. triple
a = list(map(lambda x: x * 3, [1, 2, 3, 4]))
print(a)   # [3, 6, 9, 12]

# 2. subtract 1
b = list(map(lambda x: x - 1, [10, 20, 30]))
print(b)   # [9, 19, 29]

# 3. square
c = list(map(lambda x: x ** 2, [2, 4, 6, 8]))
print(c)   # [4, 16, 36, 64]

# 4. halve
d = list(map(lambda x: x / 2, [10, 20, 30, 40]))
print(d)   # [5.0, 10.0, 15.0, 20.0]

# 5. add "Mr " before names
e = list(map(lambda n: "Mr " + n, ["Ade", "John", "Peter"]))
print(e)   # ['Mr Ade', 'Mr John', 'Mr Peter']

# 6. lowercase
f = list(map(lambda w: w.lower(), ["Cat", "DOG", "Bird"]))
print(f)   # ['cat', 'dog', 'bird']

# 7. last letter
g = list(map(lambda w: w[-1], ["cat", "apple", "banana"]))
print(g)   # ['t', 'e', 'a']



#Exercise 3
students = [
    {"name": "John", "age": 20},
    {"name": "Peter", "age": 18},
    {"name": "Mary", "age": 22}
]

students.sort(key=lambda student: student["age"])

print(students)