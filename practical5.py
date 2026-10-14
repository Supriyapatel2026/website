#Greeting function

# def greet(name):
#     print("Welcome", name)
# greet("Supriya")


#Addition function

# def add():
#     a=10
#     b=30
#     print(a+b)
# add()


#Even or odd

# def even_odd(number):
#     if number % 2 == 0:
#         return "Even Number"
#     else:
#         return "Odd Number"

# number = int(input("Enter nuber: "))
# print(even_odd(number))



#Factorial calulator

# def factorial(number):
#     if number < 0:
#             return "Invalid"
#     fact = 1
#     for i in range(1, number + 1):
#         fact = fact * i
#     return fact
# number = int(input("Enter number: "))
# print(factorial(number))


#Largest of Three Numbers

# def largest(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# print(largest(10, 25, 15))


#Grade Calculator

# def grade(marks):
#     if marks < 0 or marks > 100:
#         return "Invalid marks"
#     elif marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     elif marks >= 60:
#         return "D"
#     else:
#         return "F"

# print(grade(85))



#List Statistics

# def total(numbers):
#     return sum(numbers)

# def average(numbers):
#     if len(numbers) == 0:
#         return 0
#     return sum(numbers) / len(numbers)

# def minimum(numbers):
#     return min(numbers)

# def maximum(numbers):
#     return max(numbers)


# nums = [10, 20, 30, 40, 50]

# print("Total:", total(nums))
# print("Average:", average(nums))
# print("Minimum:", minimum(nums))
# print("Maximum:", maximum(nums))



#Banking Application (Menu Loop)

# balance = 0

# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#         print("Amount deposited successfully")
#     else:
#         print("Invalid amount")

# def withdraw(amount):
#     global balance
#     if amount <= 0:
#         print("Invalid amount")
#     elif amount <= balance:
#         balance -= amount
#         print("Withdrawal successful")
#     else:
#         print("Insufficient balance")

# def show_balance():
#     print("Current balance:", balance)


# while True:
#     print("\n1. Deposit")
#     print("2. Withdraw")
#     print("3. Show Balance")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         amount = float(input("Enter deposit amount: "))
#         deposit(amount)

#     elif choice == "2":
#         amount = float(input("Enter withdrawal amount: "))
#         withdraw(amount)

#     elif choice == "3":
#         show_balance()

#     elif choice == "4":
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice")




# Student Record Processor

# students = [
#     {"name": "Rahul", "marks": [80, 75, 90]},
#     {"name": "Aman", "marks": [40, 45, 50]},
#     {"name": "Priya", "marks": [85, 90, 95]},
#     {"name": "Neha", "marks": [30, 35, 40]}
# ]


# def calculate_average(marks):
#     return sum(marks) / len(marks)


# def passing_students(students):
#     passed = []

#     for student in students:
#         avg = calculate_average(student["marks"])

#         if avg >= 40:
#             passed.append(student["name"])

#     return passed


# for student in students:
#     avg = calculate_average(student["marks"])
#     print(student["name"], "Average:", avg)

# print("Passing students:", passing_students(students))

