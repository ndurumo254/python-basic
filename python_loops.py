#while loop
#used when we dont know number of iteration


x=0  #initializing my x variable to 0

while x<10:
    print('number is  ',x )
    x+=1.5

print('===========================')
print('cool')



import random  #this module generates a randm number

n=20

to_be_guessed=int(n* random.random()) + 1
guess=0
while guess !=to_be_guessed: # while loop is being used bcz no one knows the number of attempt before you get right answer
    guess=int(input('new number:'))

    if guess>0:
        if guess>to_be_guessed:
            print('number too large')
        elif guess <to_be_guessed:
            print('number too small')
    else:
        print('sorry bcz you are giving up')
        break
else:
    print("congratullations my nigga")






print('==================')
#for loops
#used when we know number of iterations

#finding factorials

num=int(input('number:'))
factorial=1
if num<0:
    print('must be a poasitive number')

elif num==0:
    print('factorial=1')
else:
    for i in range(1,num+1):
        factorial=factorial*i

print(factorial)