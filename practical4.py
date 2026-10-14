# # #Rectangle Pattern
# for i in range(4):
#     for r in range(6):
#         print("*",end=" ")
#     print()


# Increasing trangle
# for i in range (1,8):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# Number square
# for i in range(4):
#     for r in range(1,5):
#         print(r,end=" ")
#     print()


#Multiplication tables
# for i in range(1,11):
#     print("Table", i)
#     for r in range(1,11):
#         print(i,"*",r,"=",i*r)
#     print()


#  Prime numbers
# for num in range(2, 51):
#     prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num, end=" ")


# Classroom  Seating
# for row in range(1,6):
#     for seat in range(1,9):
#         print(f"R{row}S{seat}", end=" ")
#     print()


# Pattern challenge
rows = 5
for i in range(1, rows +1):
    for j in range(rows - i):
        print(" ",end= " ")
    for r in range(2*i -1):
        print("*",end= " ")
    print()

    
    