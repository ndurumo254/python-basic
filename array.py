#array
#array_declarations

import  array as arr

a=arr.array("i",[1,2,3,4,5,6,7,7])
print(a)

#accessing array items

a[6]
print(a[6])

#array cancatenation
#this is joining of two arrays
b=arr.array('i',[1,4,6,7,8,9,5,2,2,1,2,3,4,5,6,6,6,7,7])
c=arr.array('i',[])
c=a+b
print(c)

#slicing of an array
print(c[3:7])
print(c)


#for_loop in python
for i in c:
    print(i)


print('===========')

for i in c[4:9]  :
    print(i)




    #while loops
print('###########')

i=0
while i < c[3]:
    print(c[i])
    i=i+1
