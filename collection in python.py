from collections import namedtuple

#implementinting namedtuple

discription=namedtuple('course','name,tech')
reg=discription('python','django,back_end')
print(reg)


#chainmap
#used to combine diff classes

from collections import ChainMap
a={ 1:'ml',
    2: 'ai',
    3: 'comp'}
b={1:'chem',
     2:'bio',
     3:'math'}
c=ChainMap(a,b)
print(c)


#counter
#creates dictionary from the list

from collections import Counter
a=[1,2,3,4,5,5,6,7,6,5,3,2,2,1,1,1,2,33,4,4,5,5,6,7,7,6,5,4,4]
b=Counter(a)
print(b)