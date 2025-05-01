# Boolean operators used for small values (and, or , not)
x = 18.0
y = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(x > 10 and x < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(x < 14 or x > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(2 * x < 3 * y)

print(not(not(x < 3) and not(y > 14 or y > 10)))


#Boolean Operators for arrays
import numpy as np
a=np.array([1,2,3,9])
b=np.array([ 5,8,4,27])
print(np.logical_or(a>7,a<5))
'''np.logical_or , np.logical_and, np.logical_not are used instead of simply using boolean operators and, or, not
because when there is arrays then the simple boolean operators cannot handle the large number of input or arrays '''
print(np.logical_and(a>7,b>7))
'''the variable of both the operators need to have same length for comparision '''