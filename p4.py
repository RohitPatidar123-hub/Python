          ##Dictionary A Python dictionary is a data structure that stores the value in key:value pairs.
                                # dict = {
                                #     1: 'Python', 
                                #     2: 'dictionary', 
                                #     3: 'example'
                                # }
student={'name':'Rohit patidar','age':25,'course':['Maths','computer science','DBMS','CN']}
print("Your Dictionary :",student)
print(student['name'])
print(student['course'])
##we can also print like that 
student={1:'Rohit patidar',2:25,3:['Maths','computer science','DBMS','CN']}
print("Your Dictionary :",student)
student={'name':'Rohit patidar','age':25,'course':['Maths','computer science','DBMS','CN']}
## print(student['phone'])     ##give key error because phone key is not present in dict. that we are trying to access
print(student.get('name'))
print("default vale:",student.get('phone'))     ## instead of key error give none[default value]
print("We give explict value :",student.get('phone','not found'))  #we give expliciy  value if not found then print not found
##add new entry in dict.
student['phone']=12345678    ## add key : value in dict
student['name']='Kratika'   ## update name value
print("update with name,phone separately :",student)
## update and add multiple key at a time 
student.update({'name':'XYZ','age':30,'phone': 87654321,'address':'colony'})  ## update and add multiple key at a time and add 
print("Update with name , age , phone,address at a time : ",student)
##delete key from dict
del student['age']
print("After delete age from dict :",student)
## pop function delete key as well as it return value
NAME=student.pop('name')
PHONE=student.pop('phone')
print("poped key : ",NAME,PHONE)
student={'name':'Rohit patidar','age':25,'course':['Maths','computer science','DBMS','CN']}
print("Dict :",student)
print(len(student))
print("Dict keys :",student.keys())
print("Dict value :",student.values())
print("Dict items :",student.items())
##keys in dict from loop
print("keys in dict :")
for keys in student.keys():       
     print("    ",keys)
##value in dict from loop      
print("values in dict :")
for value in student.values():
     print("    ",value)
##value and keys from loop using item()     
print("key and value in dict : ")     
for key,value in student.items():
     print("    ",key,value)     





