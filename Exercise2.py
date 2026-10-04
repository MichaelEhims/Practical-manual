# Exercise 1

selection = input('Kindly select an option \n1. To convert from Celsius to Fahrenheit. \n2. To convert from Fahrenheit to Celsius:\n ')

if selection == '1':
    celsius = float(input("Kindly input the temperature in °C: "))
    result = (9/5 * celsius) + 32
    print(f"Temperature in Fahrenheit: {result} °F")

elif selection == '2':
    fahrenheit = float(input('Kindly input the temperature in °F: '))
    result = 5/9 * (fahrenheit - 32)
    print(f"Temperature in Celsius: {result} °C")

else:
    print('Bye')
   
# Exercise 2

name = "Ehims Michael Ariomodeake"
matric_no = 256613
height = 1.97
student = True

print(name)
print(type(name))

print(matric_no)
print(type(matric_no))

print(height)
print(type(height))

print(student)
print(type(student))

# Exercise 3

choice = input('Kindly select the shape whose area you want to calculate:\n1. Circle\n2. Rectangle\n3. Triangle\n')

if choice == "1":
    radius = float(input('Enter the radius: '))
    area = 3.14 * (radius ** 2)

elif choice == "2":
    length = float(input('Enter the length of the rectangle: '))
    breadth = float(input('Enter the breadth of the rectangle: '))
    area = length * breadth

elif choice == "3":
    base = float(input('Enter the base: '))
    height = float(input('Enter the height: '))
    area = 0.5 * base * height

else:
    area = "Invalid option"

print(f"The area is {area}")