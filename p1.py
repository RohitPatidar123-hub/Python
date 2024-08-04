#Basic Prgraam Of Python print string on display differnet method
print("Print string in python:\n")
print("Hello Rohit, How are you?")
print('I am Fine Bro')
message ='How are you ?'
print(message)
message='I am also fine bro.'
print(message)
message='What\'s the matter'    #probem with ' is that if we use without \ it give syntax error
print("message :",message)
message="Just a conflict Between two friend Rohit And Manish"

print("\nAccessing Character in String:\n")
print("message :",message,len(message)) #lengh of string
print("message[2]=",message[2])   #accessing element in string through index
print("message[5]=",message[5])
print("message[6]=",message[6])
print("message[12]=",message[12])

print("message[22]=",message[22])
#accessing elemnet from one index  to a particular location using subscript operator
print("\naccessing elemnet from one index  to a particular location using subscript operator\n")
print(message)
print(message[0:20])    #print begin to just before last index 
print(message[:5])      #by default starting index is zero
print(message[7:])      #from index 7 to inxed=lem(message) it skip last index because it is null
print(message[0:34])
#from lower to upper vice vera
print("\n from lower to upper vice vera\n")
print("Message :{} \n".format(message))
print(message.lower())    #to lower case
print(message.upper())    #to lupper case
# count no of time character present in srtring
print('\n count no of time character present in srtring \n')
message="a friend is like a rainbow of positivity, which gives a happy ending to even the stormiest days. Thank you for understanding me and always being there for me. Happy Friendship Day my love."
print("Message :{}\n".format(message))
a=" days "
print("No. of \'days\' present in string is :",message.count(a))         #count no of time it present in string
print("No. of \'a\' in message is :",message.count('a'))                 #by default starting is 0 and ending is last index
print("No. of \'e' in message is :",message.count('e',4,34))             #count no of e from starting locatin=on 4 to 34
#find string and return index at which it present other wise return -1
print('\nfind string and return index at which it present other wise return -1\n')
print("\'days\' find at indexn :",message.find("days"))                  # return index where it present
print("\'present\' find at index",message.find("like"))
 
# replace two words in string  
message="Hello! world"
message.replace("Hello!","Hii")                                         #does not replace in variable space replace  string in new variable 
print(message)                                                          #Output is Hello! world
message=message.replace("Hello!","Hii")                                       
print(message)                                                          #message.replace(source,destination)
# concatinating two string
first ="Rohit"
second="Patidar"
print(first +' '+ second+' Welcome\'s You')
#print string in string 
print("Print string in string\n\n\n")
message="{} {} Welcome!".format(first,second)
print(message)

message=f"{first} {second} Welcome's you"
print(message)

print(dir(message))  #give all the attribute and method that are available to you for that variable

