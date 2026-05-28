#task1:Create a program to convert one data type into another  
num=267
print(num)
print(type(num))
print(complex(num))
print(type(complex(num)))
print(float(num))
print(type(float(num)))

print("_______________________________________________")

#task2:build a salary bonus calculator using arithmetic operators.
emp_1=15000
emp_2=30000
bonus=5000
add=emp_1+bonus
print(add)
print(type(add))

print("___________________________________________________")

#task3:write a comparison program for product prices.
product_1=30
product_2=80
product_3=30
print(product_1==product_3)
print(product_1==product_2)
print(product_2==product_3)
print(product_1!=product_2)
print(product_1!=product_3)
print(product_2!=product_3)
print(product_1<product_2)
print(product_1<product_3)
print(product_2<product_3)
print(product_1>product_2)
print(product_1>product_3)
print(product_2>product_3)
print(product_1<=product_2)
print(product_1<=product_3)
print(product_2<=product_3)
print(product_1>=product_2)
print(product_1>=product_3)
print(product_2>=product_3)

print("__________________________________________________")

#task4:build a string indexing application.
name="alakam bhavya sree"
print(name[10])
print(name[7])
print(name[5])
print(name[14])

print("______________________________________________________-") 

#task5:Write a slicing program to extract usernames from emails.
mail="alakambhavya@gmail.com,alakamnandhakishore@gmail.com"
print(mail[0:12:1])
print(mail[23:42:1]) 

print("__________________________________________")

#task6:Build a marks update system using assignment operators.
std="bhavya"
marks=79
marks=5
print(marks)
marks+=9
print(marks)
marks-=4
print(marks)
marks*=8
print(marks)
marks/=2
print(marks)
marks//=6
print(marks)
marks%=7
print(marks)
marks**=3
print(marks)

print("_____________________________________________")

#task7:write a program to manage employee records using dictionaries.
employee={"emp_records":({"emp_id":"3201","emp_name":"bhavya","emp_salary":20000},
                         {"emp_id":"3202","emp_name":"suchi","emp_salary":40000},
                         {"emp_id":"3203","emp_name":"bhanu","emp_salary":50000})}
print(employee["emp_records"])
print(employee["emp_records"][0]["emp_name"])

print("_________________________________________")

#task9:Build a program demonstrating set data types  
fruits={"banana","apple","orange",}
print(fruits)
fruits.add("grapes")
print(fruits)
fruits.remove("banana")
print(fruits)

print("__________________________________")
#task10:Write a program to rotate list elements using slicing.
std=[1,2,3,4,5,6,7,8,9,10,"bhavya",387,'suchi',2390]
print(std[-1::-1])

print("____________________________________________________")


#task11:create a program to reverse a string using slicing.
data="thinking provides knowledge, and knowledge makes you great."
print(data[-33:-42:-1])
print(type(data))
print(data[-43:-51:-1])
print(type(data))



 








