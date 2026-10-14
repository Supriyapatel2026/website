# print("Hello")



# age=int(input(" Enter your age "))
# if age >= 18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))


# _marks_aipa=["Ajeet","Aditya","Aditi","Ajeet"]
# print(_marks_aipa)


# std=["Supriya","Shivangi","Prateeksha","Ritika"]
# print(std)



# marks=[57,54,55,67]
# print(marks)

# python is a case sensitive
# name="Supriya"  
# Name="AIPA Student"
# NAME="Allahabad"
# print(name)
# print(Name)
# print(NAME)


# class AIPA:
#     def __init__(self, name, mobile, address, uid):
#         self.name = name
#         self.mobile = mobile
#         self.address = address
#         self.uid = uid

# student1 = AIPA("Supriya", "9876543210", "Prayagraj", "AIPA001")
# student2 = AIPA("Anjali Singh", "9876543211", "Lucknow", "AIPA002")
# student3 = AIPA("Priya Sharma", "9876543212", "Varanasi", "AIPA003")
# student4 = AIPA("Ritika Maurya", "9876543213", "Kanpur", "AIPA004")
# student5 = AIPA("Pooja Verma", "9876543214", "Ayodhya", "AIPA005")

# print(student1.name, student1.mobile, student1.address, student1.uid)
# print(student2.name, student2.mobile, student2.address, student2.uid)
# print(student3.name, student3.mobile, student3.address, student3.uid)
# print(student4.name, student4.mobile, student4.address, student4.uid)
# print(student5.name, student5.mobile, student5.address, student5.uid)
   
    
# list
# students = ["Supriya","Priya","Riya"]
# print(students[0])   #access the emenet at 0 index
# print(students[1])    #access the emenet at 1 index
# students[0]="Ritika"    #modify the element of list
# students[2]="Sonam"    #modify the element of list
# print(students)
# students.remove("Riya")  #remove the element of list
# print(students)

# Tuple
# marks=(79,89,90,100)
# print(marks)


#Set
# name={"Shreya","Supriya","Shreya","Shivangi","Supriya"}
# name.add("Prateeksha")
# name.add("Priyanshi")
# name.remove("Shreya")   #remove the element
# name.update(["Ankit","Pritam","Pushpendra"])  #add multiple name
# print(name)

#Dictionary
# student={
#     "name":"Ankit",  #key-name  ,  value-Ankit
#     "age":16,
#     "course":"AIPA"
# }
# student["Address"]="Allahabad"
# student["Mobile NO"]="5263419875"
# print(student)

# student=[
#     {
#         "name":"Ravi",  
#         "age":15,
#         "course":"Copa",
#         "Address":"Prayagraj",
#         "Mobile No":"7412589630"
#     },
#     {
#         "name":"Raj",
#         "age":15,
#         "course":"EM",
#         "address":"Allahabad",
#         "Mobile No":"9874563210"
#     }
# ]
# # print(student[1]["name"])
# student[1]["address"]="Lucknow"
# print(student)


#Operater
# x = 75
# x += 10      
# x = x - 10
# x = x * 10
# x = x / 10
# x = x // 10
# x = x % 10
# x = x ** 10



#Comprarision
# age = int(input("Enter your age"))
# if age>18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")


# x=10
# y=20
# if y>=x:
#     print("x is greater")
# else:
#     print("Invalid")


# marks=70
# print(marks >=30)

# marks=45
# if marks>=20:
#     print("Pass")
# else:
#     print("Fail")

# marks=int(input("Enter your marks"))
# if marks >=50:   #conditional statement
#     print("Pass")
# else:
#     print("Fail")


# a=20
# b=35
# if a<b:
#     print("A is smaller")
# else:
#     print("B is greater")

# a=10
# b=10
# if a >= b:
#     print("Both are equal")
# else:
#     print("B is greater")


# a=20
# b=22
# if a>=b:
#     print("Both are equal")
# else:
#     print("B is greater")


# a = int(input("Enter first no.:"))
# b = int(input("Enter second no.:"))
# if a > b:
#     print("First number is greater.")
# elif b > a:
#     print("Second number is greater.")
# else:
#     print("Both are equal.")


#Password ke coding
# password = "Supriya2009"
# enter=input("Enter your password:")
# if password == enter:
#     print("Login successfully")
# else:
#     print("Invalid password")
     

#control flow (For loop)
# for i in range(1,11):
#     print(i)


#range
# for i in range(2,10,3):
#     print(i)



#Table
# num = int (input("Enter number"))
# for i in range(1,11):
#     print(num*i)

# num = int (input("Enter number"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)







#sum of numbers between 1 to 10
# for i in range(1,11):
#     total +=i    #total = total +1
# print(total)



#square
# for i in range(1,11):
#     print(i**2)


#rverse
# for i in range(10,0,-2):
#     print(i)



#count=0
# for i in range(1,104):
#     if i % 7 == 0:
#         count +=1
#         print(count)

    
# # nested loop
# for i in range(1,5):
#     for j in range(1,4):
#         print("Outer loop:",i,"Inner loop:",j)


 
# for i in range(1,4):
#     for j in range(1,3):
#         print("Outer loop:",i,"Inner loop:",j)


# for i in range(1,5):
#     for j in range(1,4):
#         print("Outer loop:",i,"Inner loop:",j)

# for r in range(1,5):
#     for b in range(1,6):
#         print("*",end=" ")
#     print()


# for r in range(1,5):
#     for b in range(1,6):
#         print("*"," ")
#     print()


# for r in range(1,5):
#     for b in range(1,6):
#         print("*",end=" ")
  

# for s in range(1,5):
#     for b in range(s):
#         print("*",end=" ")
#     print()


# #reverse nested loop
# for i in range(5,0,-1):
#     for r in range(i):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for s in range(1,i+1):
#         print(s,end=" ")
#     print()


# #reverse
# for i in range(6,0,-1):
#     for s in range(1,i+1):
#         print(s,end=" ")
#     print()


# for i in range(1,6):
#     for r in range(1,6):
#         print(i,end=" ")
#     print()


# #reverse
# for i in range(6,0,-1):
#     for r in range(6,0,-1):
#         print(i,end=" ")
#     print()



# for i in range(2,11):
#     print("table " , i)
#     for r in range(2,11):
#         print(i, "*",r,"=",i*r)
#     print()


#while loop
# i = 1
# while i <=6:
#     print(i)
#     i +=1



# i = 2
# while i <= 20:
#     if i == 12:
#             i += 2
#             continue
#     print(i)
#     i += 2

   
#calculater program
# print("My calculater  !")
# print("Type 'exit' to quit")

# while True:
#     op=input("Enter operation (+,-,*,/ or exit):")
#     if op == "exit":
#         print("Calculator closed!")
#         break
#     num1=float(input ("Enter first number:"))
#     num2=float(input("Enter second number:"))

#     if op == "+":
#         print(num1,"+",num2,"=",num1+num2)
#     elif op == "-":
#         print(num1,"-",num2,"=",num1-num2)
#     elif op == "*":
#         print(num1,"*",num2,"=",num1*num2)
#     elif op == "/":
#         print(num1,"/",num2,"=",num1/num2)
#     else:
#         print("Invalid operation")


#function
# A function is a resuable block of code that performs a specific task.
# It runs when it is called.

#function_Name()
# def aipa():
#     print("My Class AIPA")
# aipa()

# def aipa_std():
#     print("My name is:","Supriya")
#     print("My name is:","Priya")
# aipa_std()


# def total_bill(price,quantity):
#     total = price*quantity
#     return total 

# price=int(input("Enter the price:"))
# quantity=int(input("Enter the quantity:"))

# print("Total bill:",total_bill(price,quantity))



# def multiply(x):
#     for i in range(1,11):
#         print(x, "x", i, "=", x*i)

# # multiply(5)

# multiply(3)



# def add():
#     a=20
#     b=10
#     print(a+b)
# add()



# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def multiply(a,b):
#     return  a*b
# def div(a,b):
#     if b == 0:
#         return "Connot divide by zero"
#     return a/b

# print(multiply(13,17))
# print(sub(19,11))
# print(div(19,5))


# marks=[33,54,66,89]
# len (marks)

def cal_total(marks):
    return sum(marks)

def cal_avg(marks):
    return sum(marks)/len(marks)

def result(average):
    if average >=40:
        return "Pass"
    else:
        return "Fail"
    
std_name=input("Enter student name: ")

marks=[]

for i in range(1,6):
    mark=int(input("Enter marks for subject " + str(i) + ":"))
    marks.append(mark)


total=cal_total(marks)
average=cal_avg(marks)
Result=result(average)

print("Student name:", std_name)
print("Total marks:", cal_total(marks))
print("Average marks:", cal_avg(marks))
print("Result:",result)





    

  