c=['A','B','C','D']     #list
print(c)
print("c[1]   ",c[1])   #accessing element of list using index 0based indexing
print("c[2:]  ",c[2:])   
print("c[-4:] ",c[-4:])      #accessing element of list using -1 based indexing 
print("Our List Before Append:",c)  #append item at last
c.append('E')                 
print("Our List After Append E :",c)
c.insert(0,'F')                       #insert element at given index
print("Our List After insert at 0 :",c)
d=['X','Y','Z']
print("List C :",c)
print("List D :",d) 
c.append(d)                          #append list at last
print("List C after append D:",c)
c.insert(0,d)                            #append list at given index
print("List C after insert D List at 0 index",c)
c.extend(d)                             #just mix item
print("List C after extend D ",c)

##remove element from list
print("List before remove any element ",c)
c.remove('E')
print("List after removing 'E' from the list :",c)
      #pop last element from list and return
print("Last element pop from the list :",c.pop())
a=c.pop()
print("Last 2 nd element : ",a)

##reverse list
print("List before reverse : ",c)
c.reverse()
print("List after reverse : ",c)
c=['a','b','CN','DBMS','OS','CD']
a=[1,543,78,34,67,53,34,4]
##sort list
print("List Before sort :",c)
c.sort()
print("List after sort(By default Ascending order alphabatical) :",c)
c.sort(reverse=True)
print("List sort in desc :",c)
print("List Before sort :",a)
a.sort()
print("List after sort (By default ascending order):",a)
a.sort(reverse=True)
print("List after sort in desc:",a)
c1=sorted(c)    #we can also sort our list without altering main list using sorted(argue)
a1=sorted(a)
print("Without Altering main list ",a1)
print("Without Altering main list",c1)

###min,max,sum in list 
print("Our list a:",a)
print("Min in list a :",min(a))
print("Max in list a :",max(a))
print("Sum of our list element a :",sum(a))

##finding value in list
print("List a :",a)
print("78 found at",(a.index(78,0,7)))
print(1 in a)                         ##insted of index we jsut check if either element present or not
print(100 in a)                      ##return true if yes otherwise false
print('TOC' in c)
  ##print all item of list using for loop
print("Value of list a :",a)
for item,id in enumerate(a):
    print(item,id)                    ###by defaut start from 0
print("Value of List a :",a)    
for item,id in enumerate(a,start=5):
    print(item,id)    

##spliting from list to string
print("list a : ",c)
b=' - '.join(c)      ##join only list of string not int
print("From list to strin : ",b)
##spliting from string to list 

print("String b :",b)
b1=b.split(' - ')
print("String b to list c ",b1)

## list is mutable 
a=['ADS','CN','OS','COA','DM']
b=a
print("b :{}  ,a :{}".format(b,a)) 
a[0]='Blockchain'
print("Changes reflect in both because list is mutable")
print(" b :{}  ,a :{}".format(b,a)) 

##tuple
a=('ADS','CN','OS','COA','DM')
b=a
print("b :{}  ,a :{}".format(b,a)) 
##a[0]='Blockchain'
print("Changes not reflect in both because tuple  is immutable")
print(" b :{}  ,a :{}".format(b,a))    ##tuple' object does not support item assignment

###set
print("IN list :",a)
a={'ADS','CN','OS','COA','DM'}
print("in set :",a)  ##print in random sequence 
