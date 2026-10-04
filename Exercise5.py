#Exercise1
contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Find contact")
    print("3. View contacts")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact saved!")

    elif choice == "2":
        name = input("Enter name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        
#Exercise 2
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.remove(25)
print("After remove:", numbers)

numbers.pop(1)
print("After pop:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

position = numbers.index(40)
print("Position of 40:", position)

numbers.append(40)
number_of_40 = numbers.count(40)
print("Number of times 40 appears:", number_of_40)

total_items = len(numbers)
print("Total items:", total_items)

part = numbers[1:4]
print("Sliced list:", part)


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nOriginal Set A:", A)
print("Original Set B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Symmetric difference:", A ^ B)

A.add(7)
print("After add:", A)

A.remove(7)
print("After remove:", A)

A.discard(100)
print("After discard:", A)

A.pop()
print("After pop:", A)

C = {1, 2}
D = {1, 2, 3, 4}
print("Is C a subset of D?", C.issubset(D))

D.clear()
print("D after clear:", D)

#Exercise3
students = {
    "Michael": 85,
    "John": 72,
    "David": 91,
    "Peter": 68
}

scores = students.values()

highest = max(scores)
average = sum(scores) / len(scores)

names = sorted(students.keys())

print("Highest score:", highest)
print("Average score:", average)
print("Names in alphabetical order:")

for name in names:
    print(name)