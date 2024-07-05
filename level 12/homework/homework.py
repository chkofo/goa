#დავალება 1

# for i in range(10):
#     print(i)


# for i in range(10):
#     print(str(i) + "." + "spain will win euro 2024")

#დავალება 2

# age = 0
# while age < 6 :
#     print(age) 
#     age = age + 1

# num = 0
# while num < 3 :
#     print("hello")
#     num = num + 1

#დავალება 3

# num1 = int(input("enter your age:"))
# if num1 > 0 :
#     print("დადებითი")
# else:
#     print("უარყოფითი")

# num2 = int(input("enter number:" ))
# if num2 == 10 :
#     print("ათია")
# else:
#     print("არ არის ათი ")

#დავალება 4

# num3 = int(input("enter your age :"))
# if 0 < num3 < 10 :
#     print("child")
# else :
#     print("adult")

#დავალება 5

a = int(input("enter first side:"))
b = int(input("enter seceond side:"))
c = int(input("enter third side :"))

if a + b > c and a + c > b and b + c > a :
    print("ჭეშმარიტია")
else :
    print("მცდარია")