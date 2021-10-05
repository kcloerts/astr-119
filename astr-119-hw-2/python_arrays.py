x = [0.0, 3.0, 5.0, 2.5, 3.7]    #define array
print(type(x))

#remove the third element
x.pop(2)    #the number 2 represents the third element
print(x)    #always starts with 0 element

#remove the element equal to 2.5
x.remove(2.5)  #pop is based on the element
print(x)       #remove is based on the value 

#add an element at the end
x.append(1.2)
print(x)

#get a copy
y = x.copy()    #make a copy to alter an array
print(y)        #without changing the original array

#how many elements are 0.0
print(y.count(0.0))

#print the index with value 3.7
print(y.index(3.7))  #will tell which element is 3.7
                     #in this case it should be 2

#sort the list
y[0] = 5.9  #makes the first item in list 5.9
y.sort()    #orders the list from smallest to largest      
print(y)

#reverse sort
y.reverse()    #orders list from largest to smallest
print(y)

#remove all elements
y.clear()         #produces empty brackets/blank list
print(y) 