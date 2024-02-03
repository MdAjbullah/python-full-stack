# # while-loop
# # iterative control
# # while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# # while loop is used when the number of iterations is not known in advance.
# # while
# # do
# # syntax:
# # while condition:
#      # statement(s)
     
     
# # Example 1:
# # Program to print 1 to 10 using while loop 
# # initializing the value of i to 1
# # i = 1
# # using while loop to print 1 to 10
# i=1
# while  i <= 10:
#     print(i)
#     i = i + 1
    

# # Output: 1 2 3 4 5 6 7 8 9 10


# # print Mysirgi 5 times

# i = 1
# while i <= 5:
#     print("Mysirg")
#     i = i + 1
    
    
# # Output: Mysirg


# # Example 2:
# # write a program to print firsr 10 even numbers using while 10 natural number in reverse order

# i=10
# while i >= 0:
#     print(i ,end=" ")
#     i = i - 1
    
    
# # write a program to print fist 10 even natural numbers 

# i = 2
# while i <= 20:
#     print(i ,end=" ")
#     i = i + 2
    
    
# # wite a program to print first 10 odd natural numbers
# i = 1
# while i <= 20:
#     print(i ,end=" ")
#     i = i + 2
    
    
    
    
# # write a program to print first 10 odd natural numbers in reverse order
# i = 19
# while i >= 1:
#     print(i )
#     i = i - 2
    
    
    
# # write a program to print first 10 even natural numbers in reverse order
# i = 20
# while i >= 2:
#     print(i,end='')
#     i = i - 2
     
# 
i=1
while i <= 3:
    a=int(input(" enter even a number:"))
    if a%2==0:
        print(a,"is even number")
        break
    
   
    i = i + 1
if i == 4:
    print("you have entered 3 even numbers")
else:
    print("you have entered less than 3 even numbers")
    
    
#  impty bolck
# i = 1
# while i <= 3:
#     pass




