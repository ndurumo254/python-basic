#python strings
#they are used to represent alphabetical statements
#strings should be enclosed in quatation marks

name='erick'
#print (name)

#checking length of string

print(len(name))


#indexing starts at 0
#printing inex 0 output will be the first letter

print(name[0])
print(name[1:3])#Print letters btn index 1 and 3
n=name.upper()#this will change name to uper case
print(n)



#list is group of related items
#order of list cn be changed and can have duplicate of items

fruits=['banana','oranges','tomatoes','ovacado','apple']
print(fruits)
fruits[3]='kiwi'  #this updates the values in the list
print(fruits)
fruits.append('sas')#adds item at the end of the list
print(fruits)
fruits.insert(3,'orange') #adding oranges at index 3
print(fruits)
fruits.reverse()#reversing the order of list items
print(fruits)



#dictionary
#contain unordered items that can be changed but dont have  duplicate of items
#have key and value

course={1:'python',
        2:'machine_learning',
        3:'ai',
        4:'java'}
print(course)
course[3]='django'#this updates key 3 into django
print(course)


#tuple
#they are orded and can not be changed they can contain duplicate entities

animals=('dog','cat','cow','goat')
print(animals)


#set
#they contain unordered itms and no duplicate items are present
#sets donot support indexing

students={'mark','john','peter'}
print(students)


#data type conversion
#helps to use different data types together

x=10
name='erick'
age=name + ' is ' + str(x) +' years of age'
print(age)