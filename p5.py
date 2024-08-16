   ##boolean &Condition
 # Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.
if True:
    print("Condition is true")
elif False:   
    print("condition is false") 
    ##anotherr   
language ='Python'
if language=='Pyhton':
    print("Language is Python")
else : 
    print("Language is not Python")
    ##another
language='Java'        

if language=='Pyhton':
    print("Language is Python")
elif language=='Java' : 
    print("Language is Java")
else:
    print("Another Language") 
##Amdin and user
user='Admin'
logged_in=True
if user=='Admin' and logged_in :
    print("Admin Approved")
else :
    print("Bad creds")  
## #Amdin and use
user='Admin'
logged_in=False
if user=='Admin' and logged_in :
    print("Admin Approved")
else :
    print("Bad creds")
#Amdin or use
user='Admin'
logged_in=False
if user=='Admin' or logged_in :
    print("Admin Approved")
else :
    print("Bad creds")  
logged_in=False
if not logged_in:
    print("please log in ")
else :
    print('Welcome! Rohit') 
a=[1,2,3]
b=[1,2,3]
print("a=",a)
print("b=",b)
print("a is b",a is b)
print("id of a",id(a))
print("id of b",id(b))
a=b  
print("a=",a)
print("b=",b)
print("a is b",a is b)
print("id of a",id(a))
print("id of b",id(b))  

a=''
b=[]
c={}
d=0
e=False
f=None
if d:
    print("d")
if not (a or b or c or d or e or f) :
    print("atlest one value  is false :")
else :
    print("Their exist atleast one value which is True")    
   