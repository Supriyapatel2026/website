#1.safe division calculator(take two numbers from the user and handle invalid input and division by zero)


# try:
#     a=float(input("Enter first number: "))
#     b=float(input("Enter second number: "))

#     result=a / b
#     print("Result =", result)

# except ValueError:
#     print("Invalid input!")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")



#2.Positive number validator
#(ask the user to enter a number and raise a ValueError if the number is negative.)

# try:
#     num=float(input("Enter a number: "))

#     if num <0:
#         raise ValueError("Negative numbers are not allowed.")

#     print("Valid number:", num)

# except ValueError as e:
#     print("Error:", e)



#3.list index handling
#(create a list of five numbers and handle an invalid index using IndexError.)

# numbers=[10,20,30,40,50]

# try:
#     index=int(input("Enter an index(0-4): "))
#     print("Number=",numbers[index])

# except IndexError:
#     print("Invalid index!")

# except ValueError:
#     print("Please enter a valid integer.")



#4.Dictionary lookup
#(create a student dictionary and handle a missing key using keyError.)

# student={
#     "name": "Supriya",
#     "trade": "AIPA",
#     "marks": 90
# }

# try:
#     key=int(input("Enter a key(name, trade, marks):"))
#     print("Value=", student[key])

# except KeyError:
#     print("Key not found in the dictionary.")


#5.File reading
#(ask the user for a filename and handle FileNotFoundError if the file does not exist.)

# try:
#     filename = input("Enter the filename: ")

#     with open(filename, "r") as file:
#         content = file.read()
#         print("File contents:")
#         print(content)

# except FileNotFoundError:
#     print("File not found!")


#6.Integer input validation
#(keep asking the user to enter an integer until valid input is provided.)

# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         print("Valid integer:", num)
#         break

#     except ValueError:
#         print("Invalid input! Please enter an integer.")



#7.Custom exception
#(create an INsufficientBalanceError exception and raise it when the withdrawal amount exceeds the available balance.)

# class InsufficientBalanceError(Exception):
#     pass

# balance = 5000

# try:
#     amount = float(input("Enter withdrawal amount: "))

#     if amount > balance:
#         raise InsufficientBalanceError("Insufficient balance!")

#     balance = balance - amount
#     print("Withdrawal successful.")
#     print("Remaining balance:", balance)

# except InsufficientBalanceError as e:
#     print("Error:", e)

# except ValueError:
#     print("Invalid input! Please enter a valid amount.")


#8.Employee salary validation
#(accept an employee's salary,reject negative salaries, and handle invalid numeric input.)

try:
    salary = float(input("Enter employee salary: "))

    if salary < 0:
        raise ValueError("Salary cannot be negative.")

    print("Employee salary:", salary)

except ValueError as e:
    print("Error:", e)