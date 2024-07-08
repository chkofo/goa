# 1
# for i in range(20) :
#     print(i)

#2
# for i in range(10) :
#     print(i)

#3
# for i in range (1 , 100 , 2) :
#     print (i)

# for i in range (0, 100 ,2) :
#     print(i)

#4
# num = int(input("enter number:"))

# sum = 0

# for i in range (num) :
#     sum += i
# print(sum)

#5

# for i in range (5 , 50 , 5) :
#     print(i)

#while loop :

#1

# num = 2

# while num < 20 :
#     print(num) 
#     num += 2

#2

# num = 1
# sum = 0

# while num < 10 :
#     sum += num 
#     num += 1

# print (sum) 

#3


# user_number = None

# while user_number != 7 :
#     user_number = int(input("enter phone number :"))
#     if user_number == 7 :
#         print("yes")
#     else :
#         print("try again")

#4

# num = 0

# while num < 11  :
#     print(num * 2) 
#     num += 1     

#5

# user_password = None  

# while user_password != "passsword 123" :
#     user_password = (input("enter your password :"))
#     if user_password == "password 123" :
#         print("correct")
#     else :
#         print ("incorrect")


# if-else

#1

# clock = 15 

# if clock < 12 :
#     print ("good morning")
# else : 
#     print ("good afteroon")

#2

# num = int(input("enter number :"))
# if num % 2 == 0 :
#     print ("even")
# else :
#     print ("odd")

#3

# num = int(input("enter gradus :"))
# if num > 30 :
#     print("it is hot outside")
# else :
#     print("it is not to hot outside")

#4 

# age = int(input("enter your age :"))
# if age > 13 and  age < 19 :
#     print (" you are a teenager")
# else :
#     print ("you are not teenager")

#1
# sum = 0

# for i in range(1 ,10 ) :
#     sum += i 
# print(sum)

#2

# for i in range (1 ,15) :
#     print (i**2)

#3

# sum = 0

# for i in range (1 ,5) :
#     sum += i**2
# print(sum)

#4

# for i in range (1 , 100) :
#     if i % 3 == 0 and i % 5 == 0 :
#         print(i)
    

#5

# for i in range (10 , 1 , -1) :
#     print(i)

#while loop

#1

# num = 0
# user_number = int(input("enter your number :"))
# sum = 0

# while num < user_number :
#     sum += num 
#     num += 1
# print(sum)

#2

# num = 10

# while num > 1 :
#     print(num)
#     num -= 1

#3

# num = 1 
# sum = 0

# while num < 100 : 
#     sum += num
#     num += 1
# print (sum)

#4

# num = 1

# while num < 10 :
#     print(num**2)
#     num += 1

#if-else

#1

# num = int(input("enter year :"))
# if num % 4 == 0 :
#     print("leap year")
# else :
#     print ("NO")

#2

# user_string = input("enter some word :")
# if user_string == user_string[::-1] :
#     print("palindrom")
# else :
#     print("no")

#3

# num = int(input("enter your number :"))
# if num > 0 :
#     print("positive")
# elif num < 0 :
#     print("negative")
# else :
#     print("equal to zero")

#4

height = int(input("enter your height :"))
weight = int(input("enter your weight :"))
bmi = weight / ((height / 100)**2)
print(bmi)
if bmi < 18.5 :
    print ("naklebia")
elif bmi > 18.5 and bmi < 24.9 :
    print("normaluri")
elif bmi > 25 and bmi < 29.9 :
    print ("metia")
else :
    print("zedmeti")