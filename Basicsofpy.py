"""
# data type name
name = "sahil "
age =24.66
marks = 200 
print(type(name))
print(type(age))
print(type(marks))

# sum of two integer

a= 27
b= 25
sum= a+b
print(sum)

#multiple of string and numeric value *
a,b = 2,3
Txt = "@"
print(2*Txt*3)

# addition of str + str

A,B = "6 ",5
Txt = "sahil"
print((Txt+A)*B)

a = "sahil "
b = "upadhyay"
print(a+b)

A,B = 8,6
C = 5.2
print(A*B*C)

#integer division 
A,B = 20,6
C=(A//B)
print(C)

A,B = -25,3
C= (A//B)
print(C)

# taking input from user
name = str(input("name : "))
print(name)
age = int(input("age : "))
print(age)
marks = float(input("marks : "))
print(marks)

print("my name is" , name ," and i am " ,age ,"years old and i got ",marks,"in eglish that is my compulsory lang")

# conditional statemen
  

light = input("light: ")
if(light=="red"):
  print("STOP")
elif(light=="yellow"):
  print("look")
elif(light=="green"):   
  print("GO") 
else:
  print("light is broken ")


marks = int(input("marks : "))
if(marks >= 90):
  print("A")
elif(marks >= 80 and marks < 90):
  print("B")
elif(marks >= 70 and marks < 80):
  print("C")
else:
  print("D")

age = int(input("age: "))
if(age >= 18 and age < 75):
  print("you are eligible to vote ")
elif(age < 18 ):
  print("underage")
elif(age > 75):
  print("why are you living so much")
else: 
  print("go and die")
  

A = int(input("A: "))
G = input("M/F : ")
if((A == 1 or A == 2) and G == "F" ):
  print("good ")
elif(A == 3 or A == 4 and  G == "M"):
  print("better")
elif(A == 6 and G == "F"):
  print("best")
else:
  print("thankyou")
  
# ternary ( one line else and if condition ) 
food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat) 

grade = input("grade : ")
goodgrade = "yes" if grade == "A" else"not goood grades"
print(goodgrade)

license = input("license: ")
office = "he have the license" if license == "yes" else"chalan kat do"
print(office)

food = input("food: ")
print("sweet") if food == "sweet" or food == "junk food" else print("not sweet ")

#cleaver statement 
age = int(input("age: "))
vote = ("yes" , "no") [age <  18]

sal = float(input("salary: "))
tax = sal*(0.1,0.2) [sal>50000]
print(tax)

age = int(input("age: "))
print("you are eligible to vote") if(age >= 18) else print("you are not eligible to vote")

#arithmetic oprator

a = 7
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b) 
print(a % b) # reminder 
print(a // b) # integer division
print(a ** b) # power asterisk a^b

# relational operator
a = 60
b = 20
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# assignment operator
num = 10
num = num + 20
print(num)


num = 10
num += 30
print("num : ",num )

A = 10
A %= 3
print("num : ", A)

val1 = True
val2 = False

print("and operator: ", val1 and val2)
print("or operator: ", val1 or val2)

a = 50
b = 30
print(not False)
print(not (a>b) or (a>b))

num = 10
num += 30
print(num)

val = input("enter value: ") # input always convert it in [string]
print(type(val), val)       # OUTPUT = enter value: 65
                            #          <class 'str'> 65
a = 52
print(type(a))

# input 2 value and print their sum
A = int(input("number1: "  ))
B = int(input("number2: " ))
sum = A + B
print(sum)

# area of square
side = float(input("side: " ))
print(("area: "), side * side )

# average of 2 num
A = float(input("num1: "))
B = float(input("num2: "))

print("average: ",(A+B)/2)

# logical true and false
A = int(input("num1: "))
B = int(input("num2: "))
print(A>=B)

str1 = "apna"
str2 = "college"

len1 = len(str1)
print(len1)

len2 = len(str2)
print(len2)

print(str1 + " " +str2)

# indexing of string
str1 = "sahil upadhya"
print(str1[6])

str1 = "apna college"
print(len(str1))

print(str1[1:4]) #slicing of string
print(str1[0:6])
print(str1[0 :len(str1) ]) # also can write str1([0: ])

  #Negative indexing  
str = "i am eating apple"
print(str[-5:-1])
print(str.endswith("le")) # RETURN TRUE IF STRING ENDS WITH SUBSTR
print(str.capitalize()) # capitalize 1st char
print(str) # return apple (doesn't change) for change create variable

print(str.replace("apple", "orange")) # replce string
print(str.find("m"))
print(str.count("a"))
A = input("enter you name: ")
print(str.find("e"))
print(len(str)) 

light = input("light: ")

if (light == "red"):
    print("stop")
elif(light == "yellow"):
    print("be ready")
elif(light == "green"):
    print("GO")
else:
    print("malfunction light is broken ")        

marks = int (input("marks : "))
if (marks >=90):
    print("A")
elif(marks>=80 and marks < 90):
    print("B")
elif(marks>=70 and marks < 80):
    print("C")
else:
    print("fail")      

    # EVEN ODD IDENTIFIER
num = int(input("num: "))
rem = num % 2
if (rem == 0):
    print("EVEN")  
else :
    print("odd") 

a =int(input("a = "))
b =int(input("b = "))
c =int(input("c = "))
 
if (a>b and a>c): 
    print("greatest no. is A",a)
elif(b>a and b>a):
    print("greatest no is B",b)
else :    
    print("greatest no. is C",c)
               
    

num = int(input("enter no. : "))
if (num % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")    

#   LIST AND TUPLE
str = "hello"
print(str[ 0 ]) # will not run
str[0] = "hgchc" #strings are immutable can access but cannot change 
print(str)

student = ["sahil", 52.5, 75.3, "gatsby"]
print(student[0])
student[0] = "dhruv"
print(student)

marks = [1,2,3,64,5,8]
print(marks[1:4]) #indexing

print(marks[-3:-1])# negative indexing

list = [1,2,3,4,5,6,7,8,9,]
print(list.append(10))
print(list.sort(reverse=True)) # sort in descending order
print(list)

list = ['banana','apple' , 'cherry']
list.sort() #(ascending) and only this function will give none 
list.sort(reverse=True) # by char
print(list)

list = ['a','b','c']
list.reverse() # reverse the list
list.insert(1,'z') # insert something in perticular index
print(list)

list =  [1,2,3,4,5,3,6]
list.remove(3) # remove the first occurence of element 3
print(list)

list =  [1,2,3,4,5,3,6]
list.pop(3) # remove index 3
print(list)

# TUPLE 
tup = (60,60,35,65,68)
print(tup[0])
print(tup[3]) # tup[0] = 5 (ERROR = tuple doesn't support item assignment )
print(type(tup))
print(tup[1:3]) # slicing of tuple

tup = (5,) # IF (,) IS NOT included it persived as  = "int" 
print(tup) # empty tuple 
print(type(tup))

# tuple method 
tup  = (4,5,6,5,4,5,6)
print(tup.index(6))  # return index of first occurence of eliment  
print(tup.count(5))  # count total occurence  of an element

A = input("movie1: ")
B = input("movie2: ")
C = input("movie3: ")
list = [A,B,C]
print(list)

#same code diff method
movie = []

movie.append(input("movie1: "))
movie.append(input("movie2: "))
movie.append(input("movie3: "))
print(movie)

 
# palindrom check copylist(1,2,1) == reverse(1,2,1)
list = [1,2,3]
   
copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("pelindrom")
else:
    print("not pelindrom")

tup = ('a','b','c','a','d','c','a')
print(tup.count('a'))

list = ['a','b','c','a','d','c','a']
print(list.sort())
print(list.sort(reverse=True))
print(list)
 
 # DICTIONARY 
dict = {
    "name" : "sahil",
    "age" :  25 ,
    "class" : ["MCA","BCA","BTECH","MTECH"], # CAN ADD LIST
    55 : 66, # CAN ADD INT AND FLOAT VALUE
    3516.15: 84, # IN KEY WORDS CAN ONLY ADD TUPLE BECAUSE they are["immutable" ]
}
 
print(dict["name"])
print(dict["class"])
print(dict["age"])
dict["name"] = "shradha" # assign new name ==mutable 
dict["surname"] = "upadhyay"
print(dict)

null_dict = {}
null_dict["name"] = "rahul",
print(null_dict)

# NESTED DICTIONARY
student = {
    "name" : "sahil",
    "sub"  : {                # dictionary in dict. called nested dict.
              "python" : 99,  
              "java": 95,
              "C++" : 52,
              }
}

# print(student["name"])
# print(student["sub"]["python"])
print(student.keys())   #dict_keys(['name', 'sub']) output not include nested dict
 
print(type(student.keys()))
print(len(student.keys()))
print(student.values())
print(student.items()) # ruturn all (key,value ) pairs as tuple

 # return "none" in case wrong key in given
# print(student["sub"]) # give ERROR  in case wrong key in given

student.update({
    "city" : "udaipur",
    "pin"  : 313001
           
})
print(student)

new_dict = { "STATE" : "RAJASTHAN",
    "MOB"  : 31351454744}
student.update(new_dict)
print(student)

collection = {1,5,3,4,1,2,5,"hello","hello",52.33,(64)}
print(collection) #  {64, 1, 2, 3, 4, 5, 52.33, 'hello'}
print(type(collection)) # set
print(len(collection)) #8 (ignore duplicate items)

# null = set()
# null = ("dsd",5858,95)  # wrong  synetx try new one 
# print(null)    # need to use ADD METHOD
# print(type(null))  


collection = set()
collection.add(24)
collection.add(25)
collection.add(2.3)
collection.add(("apna college"))
collection.remove(25)
collection.clear() # clear all element

print(len(collection))

store = {"hello","sahil","dakshu","world"}
print(store.pop()) #  give a random element

set1 = {1,2,3,4,5} #UNION
set2 = {3,4,5,6}
print(set1.union(set2))  #  {1, 2, 3, 4, 5, 6}

set1 = {1,2,3,4,5} #INTERSECTION
set2 = {3,4,5,6}               # return common value
print(set1.intersection(set2)) #{3, 4, 5}

# PRACTICE QUESTION
word  = {
    "table" : ["a piece of furniture","list a facts & figures"],
    "cat" : "a small animal "

 }
print(word)

# practice question                        
sub1 = {'python','java','c++','python','javascript'}
sub2 = {'java','python','java','c++','c'}
print(len(sub1.union(sub2)))   # len  = 5

subjects = {'python','java','c++','python','javascript','java','python','java','c++','c'} 
print(len(subjects))         # len = 5

marks = {}
marks['science'] = 98 
marks['math'] = 99
marks['english'] = 100 
print(marks) 

# marks by user update
marks  = {}
x = int(input("physics: "))
marks.update({"phy" : x})

y = int(input("chem: "))
marks.update({"chem" : y})

z = int(input("math: "))
marks.update({"math": z})

print(marks) 

# store 9 and 9.0 in a set
value = {9,"9.0"}  # by string 
print(value)

num  = {("float",9), ("int",9.0)} # by pair of tuple
print(num)

# LOOP WHILE
# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1
# print(count)

i = 1   # i ( as varible is called "iterators")
while i <= 100 :    
     print("sahil")   
     i += 1    # loop cycle is called "iteration"
       
print(i)


x = 1
while x<= 3:
     print("ram",x)
     x  += 1
print(x)          

num = 1
while num <= 5:
      print(num)
      num += 1
print("loop ended")


num = 5
while num >= 0 :
      print(num)
      num -= 1
print("loop ended")

#practice question
f = 1
while f<= 100 :
      print(f)
      f += 1
print("1 to 100")


h = 100
while h >= 1 : # STOPING COND.
      print(h)
      h -= 1
print("100 to 1")

i = int(input("enter a num : "))
m = 1
while m <= 10 :
      print(i*m)
      m += 1
print("multiplication of 2")  


nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
      print(nums[idx]) # nums[0],numd[1],nums[3]
      idx += 1


heroes = ["superman","batman","ironman"]
idx = 0
while idx < len(heroes) :
      print(heroes[idx])
      idx  += 1

friends = ["sachin","dakshita","antima","rupesh","dev","ujjwal","arvind"]
idx = 0

while idx < len(friends):
      print(friends[idx])
      idx += 1
      



i = 1
while i <= 10:
    print(4*i)
    i += 1


heroes = ["hulk","spiderman"]
idx = 0
while idx < len(heroes):
      print(heroes[idx])
      idx += 1 


num = (5,6,8,7,6,9,8,6,5,9,8,7,5,4,1,8)
x = 8
idx = 0
while idx < len(num):
      if(num[idx] == x ):
            print("found at idx ",idx)
      else:
            print("finding")
      idx += 1


i = 0
while i <= 5:
    print(i)
    if (i == 3):
      break
    i +=1
print("end of loop")
    
    
A = 10
A %= 3
print("num : ", A)     
      

A = int(input("num1: "))
B = int(input("num2: "))
print(A>=B) 


num = int(input("num: "))
rem =  num % 2
if num == 0 :
     print("EVEN")
else:
     print("odd")     
 
student = ["sahil", 52.5, 75.3, "gatsby"]
print(student[0])
student[0] = "dhruv"
print(student)


list = [1,2,3,4,5,6,7,8,9,]
print(list.append(10))
print(list.sort(reverse=True)) # sort in descending order
print(list)



list = ['a','b','c']
list.reverse() # reverse the list
list.insert(1,'z') # insert something in perticular index
print(list)

# palindrom check copylist(1,2,1) == reverse(1,2,1)
list = [1,2,3]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):

    print("pelindrom")
else:
    print("not pelindrom")


list = [1,2,1]
copy_list = list.copy()
copy_list.reverse()

if copy_list == list :
     print("pelindrom ")
else :
     print("not a pelindrom")

     
tup = ('a','b','c','a','d','c','a')
print(tup.count('a'))

info = {
     "name" : "sahil" ,
     "sub"  : {"pyhton" : 95 ,
              "chem"  : 96  ,
              "math"  : 100,


              } ,
              "additional_info" : "vuvuv" 
            
     } 
print(info)

count = 1
while count <= 5 :
    print("ram")
    count += 1
    
print(count)

x = 1 
while x <= 3 :
    print("krishna",x)
    x += 1
print(x) 


heroes = ["superman","batman","ironman"]
idx = 0
while idx < len(heroes) :
      print(heroes[idx])
      idx  += 1

num = (1,2,3,4,5,6,7,8,9,4,5,6,1,23,)
i = 0 
while i < len(num) :
     print(num[i])
     i += 1 


num = (1,2,3,4,5,6,7,8,9,23,4,5,6,1,23,)
x = 23
i = 0 
while  i < len(num) :
     if (num[i] == x ):
          print("num  at i = ", i)
        
     else :
          print ("finding ")
     i += 1
    
num = (5,6,8,7,6,9,8,6,5,9,8,7,5,4,1,8)
x = 8
idx = 0
while idx < len(num):
      if(num[idx ] == x ):
            print("found at idx ",idx)
      else:
            print("finding")
      idx += 1



i  = 0 
while i <= 5 :
     print (i)
     if i == 3 :
        break
     i +=1     
print ("end of loop")
  

num = (5,6,8,7,4,6,9,8,6,5,9,8,7,5,4,1,8)
x = 4 
i = 0 
while i < len(num) :
     if(num[i] == x) :
          print ("found at index hgdddgj : ", i) 
     else :
          print("finding")
     i += 1

   
num = (5,6,8,7,6,9,8,6,5,9,8,7,5,4,1,8)
x = 8
idx = 0
while idx < len(num):
      if(num[idx ] == x ):
            print("found at idx ",idx)
      else:
            print("finding")
      idx += 1

i = 0 
while i <= 5 :
     if i == 3 : 
          i += 1 
          continue  # skip
     print(i)
     i += 1

i = 0 
while i <= 10 :
     if (i %2 == 0) : 
          i += 1      # to print odd num 
          continue  # skip
     print(i)
     i += 1


i = 0 
while i <= 10 :
     if (i %2 != 0) : 
          i += 1      # to print even num 
          continue  # skip
     print(i)
     i += 1

list = (1,4,9,16,25,36,49,64,81,100)
x = 36
i = 0

for val in list :
     if (val == x ):
          print("found at idx ", i)
          break
     i += 1

str = "sahil upadhyay"
for char in str :
     if (char == "l"):
          print("found l")
          break
     print(char)
else :
     print("end")



i = 0 
while i <= 10 :
     if (i %2 == 0) : 
          i += 1      # to print odd num 
          continue  # skip
     print(i)
     i += 1


                              # RANGE
seq = range(5)
for i  in seq :
    print(i)
 
for i  in range(11):
    print(i)   # stop 

for i in range (2,20,2):# (start? , stop,step?)
    print(i)
    
# practice quesion

for i in range(101):
    print(i)

for i in range(100, 0,-1):
    print(i)     

for i in range(int(input("num :")), 20 ,int(input("num :"))): 
    print(i)

n = int(input("num : "))

for  i in range(1,11):
    print(n*i) 

                           # pass statement
for i in range(10):
    pass 
print("some usefull work for future")

if (i > 5) :
    pass

n = 10 
sum = 0
i = 0
for i in range(1,n+1) :
    sum += i 
print("total sum of num :  ", sum)

n= 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    
print("total = ",sum)

n = 5
fact = 1
i = 1 
while i <= n:
    fact *= i 
    i += 1

print(fact) 
    
n  = 10
sum = 0
i = 1 

while i <= n:
      sum += i
      i += 1
print("total addition = " ,sum)

       
n = 8 
sum = 0 
i = 1 

while i <= n :
    sum += i 
    i += 1 
print("total add : ", sum)


n = 6 
sum = 0 
for i in range(n,n+1):
    sum += i

n = 6 
sum = 0 
i = 1 
while i <= n :
    sum += i 
    i += 1 

n = int(input("fact no. : "))
fact = 1
i = 1 

while i <= n :
    fact *= i 
    i += 1
print("factorial of 5: ", fact)

n = 5 
fact =  1 
for i in range(1,n+1):
    fact *= i 

print("FACT ",fact)

                                           
                                                      # FUNCION 
# fuction definition 
def cal_sum(a,b): # parameter 
    sum = a + b 
    print(sum)
    return sum 

cal_sum(5,20) # function call ;argument

cal_sum(20,50)

def print_ram(): # no paramete
    ram = print("ram")
    return  ram

output = print_ram()
print(output)

def avg_num(a,b,c):
    sum = a + b + c 
    avg = sum/3
    print(avg)
    return avg

avg_num(5,9,8)  


print("sahil", end=" ") # sep = " "
print("upadhyay") # by end= [  same line ]

def cal_prod(b,a=2):
    print(a*b)
    return a * b  

cal_prod(1)

sub = ["java", "python","c","c++","react js"]

def len_list(list):
    print(len(list))

len_list(sub)

    

sub = ["java", "python","c","c++","react js"]
    
def same_line(list):
     for item in list:
         print(item,end= " ") # for diffrent line end= "/n"
         
same_line(sub)

n = 2
fact = 1

for i in range(1,n+1):
    fact *= i 
    print(fact)
    
def fact(n):
   fact = 1
   for i in range(1, n+1):
    fact *= i 
    print(fact)

fact(5)

def converter(usd_val): 
    inr_val = usd_val * 83 
    print("USD= ",usd_val,"INR=",inr_val)

converter(5) 

def ident(n):
    if (n%2 == 0) :
        print("even")
    else:
        print("odd no.")

ident(5)

#recursion 
def show(n):
    if (n == 0):
        return
    print(n)  
    show(n-1)

show(10)

def fact(n):
    if (n==1 or n == 0 ):
        return 1
    return  fact(n-1) * n
     
print(fact(5))

def sum(n):

    if (n == 0):
        return 0
    return sum(n-1) + n

print(sum(5))
    


def sum(n):
    if n == 0 :
        return 0
    return sum(n-1) + n


     

print(sum(5))

def fact(n):
    if n == 0 or n == 1 :
        return 1
    return fact(n-1) * n

print(fact(5))




def print_list(list,idx):
    if (idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx +1 ) 

cars  = ["farrari","od","BMW","jaguare",]
print_list(cars,0)

# FILE INPUT AND OUTPUT

f = open ("D:\python\demo.txt","rt")
data = f.read(10)
print(data)
print(type(data))
f.close()
  

f = open ("D:\python\demo.txt","rt")
line1= f.readline()
print(line1)

line2= f.readline()
print(line2)

f.close()

f = open ("D:\python\demo.txt","a ")
f.write(" after python")
f.close()

f = open("sample.txt","w")
f.close()   # create the file if it doesn't exist

# OBJECT ORIENTED PROGRAMING 

class Student() :
    name = "karan"
    marks = 99

s1 = Student()
s2 = Student()
print(s1.name)
print(s2.marks)


class cars:
    name = "farari"
    color = "white"

c1 = cars()
print(c1.name)
print(c1.color)


class cars :
    
    def __init__(self,fullname ):
        self.name = fullname
        print("adding new cars in database")

c1 = cars("porche")
print(c1.name)


class brand : #paramererized constructor 
    def __init__(self,brandname,color,prize) :
        self.name = brandname
        self.color = color
        self.prize = prize

    def feature(self):
        print("welcome to cars world ",self.name)
  

b1 = brand("bugati","red",500000)       
print(b1.name)
print(b1.color)
print(b1.prize)
b1.feature()

b2 = brand("land rover", "black",100000)
print(b2.name)
print(b2.color)
print(b2.prize)

class student :
    def __init__(self,name,marks) : # by list mthod
        self.name = name 
        self.marks = marks
      

    def avrage(self) :
        sum = 0 
        for val in self.marks : # ADDITION BY LOOP
            sum += val 
        print("hy", self.name,"your marks average is : ",sum/3)

s1 = student("karan",[98,95,96])  
print(s1.name,s1.marks)
s1.avrage()

#  diffrent style 

class student :
    def __init__(self,name,phy,chem,math) :
        self.name = name 
        self.phy = phy 
        self.chem = chem 
        self.math = math 

    @ staticmethod 
    def hello() :         # staticmathod 
        print("hello")



    def avrage(self) :
        sum = self.phy + self.chem + self.math 
        print("average is : ",sum/3)
s1 = student("karan",98,95,96)
print(s1.name,s1.phy,s1.chem,s1.math)

    
s1.avrage()
s1.hello()


class car :                           # example of abtraction
    def __init__(self) :
        self.acc = False 
        self.brk = False 
        self.clutch = False 

    def start(self):
        self.clutch = True 
        self.acc = True
        print("car started....")

c1 = car() 
c1.start()

class  account :
    def __init__(self,bal,acc):
        self.balance = bal 
        self.account_no= acc
    
    def debit(self,amount) :
        self.balance -= amount     
        print("ypur account is debited by ",amount,"Rs.") 
        print(" and your available balace is",self.avail_bal())

    
    def credit(self,amount) :
        self.balance += amount
        print("ypur account is credited by ",amount,"Rs. ") 
        print(" and your available balace is",self.avail_bal())

    def avail_bal(self):
       return self.balance

acc1  = account(10000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.credit(1000)
acc1.debit(2000)
 
class student:                # delete object
    def __init__(self,name,bank_pass):
        self.name = name 
        self.__bank_pass = bank_pass # for private attributr we add (__2 semicolon like self.__bank_pass)
s1 = student("sahil",784512)
print(s1.name)
print(s1.name)
print(s1.__bank_pass)
del s1
print(s1.name)  


class person :
    __name = "sahil"      # it is used to prevent instance attribute out of the class
    def __hello(self) :    # if we direct call __hello fx it won't work                     
         print("hello person")  # by making wecome fx we indirectly call it 
    
    def welcome(self) :  
       self.__hello()

p1 = person()
print(p1.welcome())
"""
    # inheritance
 
class  car :
    def ___init__(self,alloywheel) :
        self.alloywheel = alloywheel

    color = "blue"

    @staticmethod 
    def start():
        print("car started")
    
    @ staticmethod
    def stop():
        print("car stoped")

class toyotacar(car):  # multilevel
    def __init__(self,brand,alloywheel):
        self.brand = brand
        super().___init__(alloywheel)   # super CONSTRUCTER INHERITANCE PRARENT TO CHILD 

class fortuner(toyotacar) :
    def __init__(self,type,alloywheel):
        self.type = type
        super().___init__(alloywheel) 
        super().start()
          # super CONSTRUCTER INHERITANCE PRARENT TO CHILD 


car1 = toyotacar("punch","alloywheel")
print(car1.brand)
print(car1.start())
print(car1.color)
print(car1.alloywheel)

car2 = fortuner("diesel","alloywheel")
print(car2.alloywheel)
print(car2.type)
car2.start()

  

class A :
       
    @staticmethod    # static method can't access or modify clss satate & generally for utility.
    def start():
        print("car started")
    
    varA = "welcome to class A"
        
class B :
    varB = "welcomw to class B"

class C(A,B):
    varC = "welcome to class C"
    # super().start()
   
C1 = C
print(C1.varC)
print(C1.varB)
print(C1.varA)
# print(C1.start())

class person :

    name = "rahul"

    # def change_name(self,name):
    #     self.name = name
    @classmethod   #  classmethod change in  name permanently
    def changename (cls,name) :
        cls.name = name

per1 = person()
per1.changename("rythem")
print(per1.name)
print(person.name)    # for change the class name 



class person :

    name = "rahul"

    def change_name(self,name):
        self.__class__.name = name  # 1M change in class
       # person.name = name  # 2M change in class

per1 = person()
per1.change_name("sahil") 
print(per1.name)
print(person.name)


class student :
    def __init__(self,phy,chem,math) :
        self.phy = phy
        self.chem = chem 
        self.math = math 
        # self.percentage = str((self.phy+self.chem + self.math) / 3 ) + "%"
    
    # def calcpercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3 ) + "%"
     
    @property                           # by prperty 
    def percentage(self):  
        return str((self.phy + self.chem + self.math) / 3 ) + "%"


stu1 = student(98,97,94)
print(stu1.percentage)

stu1.phy = 86
# stu1.calcpercentage()
print(stu1.percentage)


n = 10 
sum = 0
i = 0
for i in range(1,n+1) :
    sum += i 
print("total sum of num :  ", sum)

                 #revision
num = 1
sum = 0
i = 0
while i <= 5 :
    sum += i
    i += 1   

count = 1 
while count <= 5 :
    print("ram")  
    count += 1

i = 1 
while i <= 10 :
    print("sita",i)
    i +=1 
    
# print no. 1 to 5 
i = 0
while i <= 5 :
    print(i)
    i += 1

print("loop ended")

i = 5 
while i >= 1:
    print(i)
    i -=1

i = 0 
while i <= 10 :
    print(i)
    i += 1


i = 100 
while i >= 1 :
    print(i)
    i -= 1

n = int(input("num : "))
i =  1
while i <= 10 :
    print( n *i ) 
    i += 1
  
list = [1,4,9,16,25,49,64,81,100]
idx = 0 
while idx < len(list) :
    print(list[idx]) # list[0],list[1],list[2]....
    idx += 1

animal = [ "cat","dog","cow","lion"]
idx = 0 
while idx < len(animal):
    print(animal[idx])
    idx += 1

birds  = ["parrot","pecock","sparrow"]
idx = 0 
while idx < len(birds):
    print(birds[idx])
    idx += 1

num  = [1,2,3,4,5,6,7,8,9]
idx = 0 
x = 8
while idx < len(num):
    if num[idx] == x:
     print("found x at idx",idx)
    else :
        print("finding")

    idx += 1

for i in range(2,21,+2) :
    print(i)

n = int(input("n : ")) 
i = 1 
while i <= 10 :
    print(n*i)
    i += 1



n= 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)


n = 10  
i = 1 
sum = 0
 
while  i <= n :
    sum += i 
    i += 1
print(sum)


n = 10 
i = 1
fact= 1

while i <= n :
    fact *= i
    i += 1
print("factorial of n : ", fact)


n = int(input("fact no. : "))
fact = 1
i = 1 

while i <= n :
    fact *= i 
    i += 1
print("factorial of n : ", fact)

i = 0 
while i <= 10 :
    print(i)
    if i == 5 :
      break
    i += 1

print("end of the loop")

n = 5 
fact = 1 
for i in range(1,n+1):
    fact *= i 
print(fact)


i = 0 
while i < 11 :
    if i == 3 :
        i += 1
        continue
    print(i)
    i += 1


i = 0 
while i < 11 :
    if (i % 2 == 0) :    # odd no. print
        i += 1
        continue
    print(i)
    i += 1

     

i = 0 
while i < 11 :
    if (i % 2 != 0) :     # even no.print
        i += 1
        continue
    print(i)
    i += 1


list = [1,2,3,4]

for val in list:
    print(val)

name = "sahil upadhyay"

for char in name :
  
    if (char == 'l'):
        print("l found")
        break
    print(char)
else:

    print["end"]

list = [1,4,9,13,25,36,49,81,100]
x = 49
idx = 0
for el in list :
    if (el == x):
        print("found at idx",idx)
    idx += 1
    print(el)
else:
        ("not found")

n = 5 
sum = 0 
i = 0 
while i <= n :
    sum += i 
    i += 1
print(sum)


n = 5
sum = 0
for i in range(1,n+1) :
    sum += i
print(sum)

n = 5
fact = 1
for i in range(1,n+1):
    fact *= i 
print(fact)



