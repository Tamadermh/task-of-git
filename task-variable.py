#Create a Boolean variable named x
x= False
print(type(x))

#Create an integer variable named y

y= 4
print(type(y))

#Create a float variable named z

z= 5.3
print(type(z))

#Create a string variable names s
s= "8889"

Convert the int variable to float

print(float(y))

# Can we convert the str to int ?
# yes but if the string not litter
print(int(s))

#Create a list of numbers from 1 to 5
ty=[1,2,3,4,5]


#Create a tuple from 10 to 15
so=(10,11,12,13,14,15)

#Convert the list to tuple
tuple(ty)
print(type(tuple(ty)))

#Create a dict of 3 values
rt={1:"r",3:"m",5:"p"}
print(type(rt))


#Can we use semi colon ; with python
#Python is interpreted or compiled ?
# What is the differences between low level & high level
# What is the differences between = , ==
# What do we mean by using !=
# What is the operator precedence

'''

لانحتاج استخدام الفاصلة المنقوطة لان اللغة تعتمد على المسافات
 python is inerpreted
 low level لغة صعبة الاستخدام الانساني وتكون اقرب للغة الالة
 high level لغة تكون سهلة ومفهومة للانسان


 تعني اسناد قيمة الى متغير ما (==) تعني المقارنة بين قيمتين(=)


 (==)تعني هل القيمة لاتساوي القية الاخرى بمعنى اصح هي عكسس(!=)

 
 '''

#Create a variable x with value of 10

x=10
#Increase x value by 15 using assignment operators
x+=15
#Divide the x value by 5 using assignment operators
x/=5

#Multiply the x value by 10 using assignment operator

x*=10

#Get module of x on 3 using assignment operators

print(x)
x%=3
print(x)


# Using python print the module of 11 to 4
print(11%4)


# Print the exponent of 2,3
print(2**3)


# Divide 11 by 3 using python division
print (11/3)

#Can we divide 11 by 3 and get an integer number ?

q=11/3
round(q)


# Check if 10 is bigger than 15 or not
#If 10 is not bigger than15 print x is smaller than 15
if 10>15 :
    print ('x is smaller than 15')
else :
    print ('no')


# In which cases we will use all
'''and'''

#What is the differences between all , and
# تستخدم عند تواجد اكثر من شرط ويلتزم تحقق الشروط جميعها(and)
# وهي دالة ويتم ادخال كافة الشروط بدالخلها كمتغيرات لست  andتحل محل (all)


#What is the differences between any , or
'''
(or) تتواجد بين الشروط عندما يتطلب تحقيق شرط واحد فقط 
(any) تحل محل (or) ولكن لايشترط تكرارها بين الشروط تكتب مرة واحدة فقط وهي دالة وتكون الشروط بداخلها كمتغيرات list
'''

#If we need all the conditions to be true we will use ….

'''
نستخدم دالة (all)
'''

#What is the differences between if , elif
 
'''
(if) هي الشرط الاساسي 
(elif)
هي شرط اخر في حال لم يتحقق شرط
(if)
ويكون (elif)
تابع
لل(if)
'''

#What is the differences between elif else
#(else) لاتتطلب كتابة شرط بعدها
#(elif)تطلب كتابة شرط بعدها


#Can we use more than one elif
'''yes'''

# Can we use more than one else
'''no'''

#write s simple ternary operator

a=5
b=7
print(a,"is greater") if (a>b) else print(b,"is Greater")

#in elif , python will check all the conditions no matter what ?
'''no . لن يختبر باقي الشروط عندما يجد شرط صحيح'''


#in elif we use else for ... ?
'''
لاي احتمال خارج عن الشرط المحددة '''


a=[2,4,6,8,10]

#check to see if 4 in this list or not

if 4 in a:
    print (a.index(4))
else :
    print ('is not there')

    
#check to see if 4 and 6 in this list on not
if 4 and 6 in a:
    print (a.index(4),a.index(6))
else :
    print ('is not there')


#check to see if 3 or 6 in this list
if 3 or 6 in a:
    print ('yes')
else :
    print ('is not there')

#check to see if 2 , 4 and 5 in this list
if 2 in a and 4 in a and 5 in a:
    print ('yes')
else :
    print ('is not there')

