#1.Age Verification System

# try:
#     age=int(input("Enter your age: "))

#     if age <0 or age >120:
#         raise ValueError("Age must be between 0 and 120.")
    
#     print("Valid age:", age)

# except ValueError as e:
#     print("Error:", e)


# #2.Product Price checker

# try:
#     price=float(input("Enter product price: "))

#     if price <0:
#         raise ValueError("Price cannot be negative.")

#     print("Product price:", price)

# except ValueError as e:
#     print("Invalid price:", e)


# #3.Tuple Element Access

# cities =("Delhi","Mumbai","Lucknow","Kolkata","Chennai","Jaipur","Bhopal")

# try:
#     positon = int(input("Enter position (0-6):"))
#     print("City:", cities[-positon])

# except IndexError:
#     print("Error: Invalid position.")

# except ValueError :
#     print("Error: Please enter an integer.")



# #4.Contact Information lookup

# contacts={"Ankit": "7412589630","Pritam": "7896541230","Pushpendra":"8521236547"}


# try:
#     name=input("Enter contact name: ")
#     print("Phone number:", contacts[name])

# except KeyError:
#     print("Error: Contact not found.")



# #5.File writing operation

# try:
#     filename=input("Enter filename: ")
#     text=input("Enter text to write: ")

#     with open(filename, "w") as file:
#         file.write(text)

#         print("Text written successfully.")

# except PermissionError:
#     print("Error: Permission denied while writing the file.")



# #6.Valid roll no input

# while True:
#     try:
#         roll=int(input("Enter a positive roll number: " ))

#         if roll <=0:
#             print("Roll number must be greater than zero.")

#             continue
#         print("Valid roll number: ", roll)
#         break
#     except ValueError:
#         print("Invalid input. Enter an integer.")



# #7.Custom exception for boting eligibility

# class NotEligibleToVoteErro(Exception):
#     pass
# try:
#     age=int(input("Enter your age: "))

#     if age < 18:
#         raise NotEligibleToVoteErro("You are not eligible to bote.")

#     print("You are eligible to vote.")

# except ValueError:
#     print("Please enter a valid age.")

# except NotEligibleToVoteErro as e:
#     print(e)




# #8.Bank account deposit vgalidation

# try:
#     amount=float (input("Enter deposit amount."))

#     if amount <= 0:
#         raise ValueError("Deposit must be greater than zero.")

#     print("Deposit successful:",amount)

# except ValueError as e:
#     print("Error:",e)



# #9.Shopping cart quantity check

# try:
#     quantity = int(input("Enter item quantity: "))

#     if quantity < 1:
#         raise ValueError("Quantity must be at least 1.")

#     print("Quantity added to cart:", quantity)

# except ValueError as e:
#     print("Error:",e)



# #10.Password strenght validator

# try:
#     password=input("Enter your password: ")

#     if len(password)< 8:
#         raise ValueError("Password must contain at least 8 characters.")

#     print("Password lenght is valid.")
    
# except ValueError as e:
#     print("Error:",e)



# #11. Student Grade Calculator


# try:
#     marks1 = float(input("Enter marks for subject 1: "))
#     marks2 = float(input("Enter marks for subject 2: "))
#     marks3 = float(input("Enter marks for subject 3: "))

#     marks = [marks1, marks2, marks3]

#     for mark in marks:
#         if mark < 0 or mark > 100:
#             raise ValueError("Marks must be between 0 and 100.")

#     total = sum(marks)
#     average = total / 3

#     print("Total marks:", total)
#     print("Average marks:", average)

# except ValueError as e:
#     print("Invalid input:", e)



# #12.ATM PIN Verification

# correct_pin = "1234"

# try:
#     for attempt in range(3):
#         pin = input("Enter your ATM PIN: ")

#         if pin == correct_pin:
#             print("PIN verified successfully.")
#             break
#         else:
#             print("Incorrect PIN.")

#     else:
#         raise Exception("Three attempts failed. Access denied.")

# except Exception as e:
#     print("Error:", e)



# #13.Email Address Validator

# try:
#     email=input("Enter your email address: ")

#     if"@"not in email or"."not in email:
#         raise ValueError("Invalid email address.")

#     print("Email address is valid.")

# except ValueError as e:
#     print("Error:", e)



# #14.Division of List Elements

# numbers = [10, 20, 0, 40, 50]

# try:
#     index1 = int(input("Enter first index (0-4): "))
#     index2 = int(input("Enter second index (0-4): "))

#     result = numbers[index1] / numbers[index2]

#     print("Result:", result)

# except IndexError:
#     print("Error: Index is out of range.")

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# except ValueError:
#     print("Error: Please enter valid integer indexes.")
    


# #15.Username Availability Checker

# class UsernameAlreadyExistsError(Exception):
#     pass

# existing_usernames=["Supriya","Priya","Prachi"]

# try:
#     username=input("Choose a username:")

#     if username in existing_usernames:
#         raise UsernameAlreadyExistsError("Username is already taken.")

#     print("Username is available.")

# except UsernameAlreadyExistsError as e:
#     print("Error:", e)


# #16.Electricity Bill Calculator

# try:
#     units = float(input("Enter electricity units consumed: "))

#     if units < 0:
#         raise ValueError("Units cannot be negative.")

#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = 100 * 5 + (units - 100) * 7
#     else:
#         bill = 100 * 5 + 100 * 7 + (units - 200) * 10

#     print("Electricity bill: Rs.", bill)

# except ValueError as e:
#     print("Error:", e)


# #17.Student Record Search

# students = {
#     101: "Rahul",
#     102: "Amit",
#     103: "Priya"
# }

# try:
#     student_id = int(input("Enter student ID: "))
#     print("Student name:", students[student_id])

# except KeyError:
#     print("Error: Student record not found.")

# except ValueError:
#     print("Error: Student ID must be an integer.")


# #18.Mobile Number Validation

# try:
#     mobile = input("Enter your 10-digit mobile number: ")

#     if not mobile.isdigit() or len(mobile) != 10:
#         raise ValueError(
#             "Mobile number must contain exactly 10 digits."
#         )

#     print("Valid mobile number:", mobile)

# except ValueError as e:
#     print("Error:", e)


# #19.Online Ticket Booking

# class TicketsUnavailableError(Exception):
#     pass

# available_seats = 50

# try:
#     tickets = int(input("Enter number of tickets to book: "))

#     if tickets < 1:
#         raise ValueError("Book at least one ticket.")

#     if tickets > available_seats:
#         raise TicketsUnavailableError(
#             "Requested tickets exceed available seats."
#         )

#     available_seats -= tickets

#     print("Tickets booked successfully:", tickets)
#     print("Remaining seats:", available_seats)

# except ValueError as e:
#     print("Invalid input:", e)

# except TicketsUnavailableError as e:
#     print("Booking error:", e)



# #20.Number Range Validator

# try:
#     number = int(input("Enter a number between 1 and 50: "))

#     if number < 1 or number > 50:
#         raise ValueError("Number must be between 1 and 50.")

#     print("Valid number:", number)

# except ValueError as e:
#     print("Error:", e)