# if condition :
# indentation is most 
# x = int(input("Enter a number: "))
# if x<0:
#     print("Negative")
# if x>0:
#     print("Positive")
# print()


# # if else statement
# # tue then if ,false the else 

# num = int(input("Enter a number: "))
# if num<0:
#     print("Negative")
# else:
#     print("Positive")
# print()


# if elif else statement
# elif is else if   , if the first condition is false then elif will check the condition


# write a program toprint the garde obtaoined by the student in a test .take marks obtained from the user and sidplay the grade
#90<grade<100 A+
#80<grade<90 A
#70<grade<80 B+
#60<grade<70 B
#50<grade<60 C
#40<grade<50 D
# blow 50 

# marks = int(input("Enter the marks obtained: "))
# if marks>90:
#     print("A+")
# elif marks>80:
#     print("A")
# elif marks>70:
#     print("B+")
# elif marks>60:
#     print("B")
# elif marks>50:
#     print("C")
# else:
#     print("below 50")


# marks=int(input("Enter the marks obtained: "))
# if 90<=marks<=100:
#     print("A+")
# elif 80<=marks<=90:
#     print("A")
# elif 70<=marks<=80:
#     print("B+")
# elif 60<=marks<=70:
#     print("B")
# elif 50<=marks<=60:
#     print("C")
# else:
#     print("below 50")
    
    
    
    
# single line if statement

# syntax
# if condition is true else statement
# diffrent between sindline if else stateme if if else satatemanet 

# 1 if else satetment can not write in a single line 
# single line if else is an expression but if elase is not anexpression 





# write a program to chack whethe a given number is positive or non positive 

# num=int(input("Enter a number: "))
# print("Positive") if num>0 else print("Non positive")

# print("positive" if int(input("please enter number"))>0 else "non positive")
    
    
    
    
    
# nested if else statement

# if conditin:
#    --------------
#    --------------
#     if condition:
#         ------------
#         ------------
#         ------------
#     else:
#         ------------
#         ------------
# else:
#   ------------
#   ------------



# write a program to check whether a given number is even or odd and positive or negative

"""num=int(input("Enter a number: "))
if num>0:
    if num%2==0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    if num%2==0:
        print("Negative and even")
    else:
        print("Negative and odd")
print()"""


""" match statement
match is a shoft keyword

syntax

match expression:

MATCH subject expression:
case constant:
    -------------
    -------------
case constant:
    -------------
    -------------
case constant:
    -------------
    -------------
case constant:
    -------------
    -------------
case constant:
    -------------
    -------------
break key word is not required in match statement
default:  # default is optional""" 
   
x = int(input("Enter a number: "))
match x:
       case 1:
           print("one")
       case 2:
           print("two")
       case 3:
           print("three")
       case 4:
           print("four")
       case 5:
           print("five")
       case 6:
           print("six")
       case 7:
           print("seven")
       case 8:
           print("eight")
       case 9:
           print("nine")
       case 10:
           print("ten")
       case _:
           print("invalid number")












    