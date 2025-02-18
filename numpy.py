#Nmupy
import numpy as np
import time
import sys
print(np.__version__)
print(dir(np))
my_list=[1,2,3,4,5]
my_array=np.array(my_list)

print(my_list)
print(my_array)

print(50 * "#")

print(type(my_list))
print(type(my_array))

print(50*"#")

a=np.array(10)
b=np.array([10,20])
c=np.array([[30,40],[90,80]])
d=np.array([[[1,5],[2,7],[3,6]],[[4,8],[5,4],[6,1]]])

print(a)
print(b)
print(c)
print(d)

print(50*"#")

#Number of Dimentions

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print(50*"#")

#custom dimention

my_custom_array=np.array([1,2,3], ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim)
print(my_custom_array[0,0,0])
print(my_custom_array[0,0,1])
print(my_custom_array[0,0,2])

print(50*"#")

#compare data location and type

my_List_1=[1,2,3,4]
my_Array_1=np.array([1,2,3,4])

print(id(my_List_1[0]))
print(id(my_List_1[1]))

print(id(my_Array_1[0]))
print(id(my_Array_1[1]))

print(50*"#")

#data type and control array

my_list_of_data=[1,2,"A","B",True,10.5]
my_array_of_data=np.array([1,2,"A","B",True,10.5])

print(my_list_of_data)
print(my_array_of_data)

print(my_list_of_data[0])
print(my_array_of_data[0])

print(type(my_list_of_data[0]))
print(type(my_array_of_data[0]))

print(50*"#")

#compare performance and memroy use

elements=150000

My_List1=range(elements)
My_List2=range(elements)

My_Array1=np.arange(elements)
My_Array2=np.arange(elements)

list_start=time.time()
list_result=[(n1+n2) for n1, n2 in zip(My_List1,My_List2)]
print(f"List Time: {time.time()-list_start}")
array_start=time.time()
array_result=My_Array1+My_Array2
print(f"Array Time: {time.time()-array_start}")
print(50*"#")

#size of elements in array

mmy_array=np.arange(100)

print(mmy_array)
print(mmy_array.itemsize)
print(mmy_array.size)
print(f"All Bytes: {mmy_array.itemsize * mmy_array.size}")

print(50*"#")

mmy_list=range(100)

print(sys.getsizeof(1))
print(len(mmy_array))
print(f"All Bytes: {sys.getsizeof(1) * len(mmy_array)}")

print(50*"#")

#array slicing

a=np.array([["A","B","X"],["C","D","Y"],["E","F","Z"],["M","N","O"]])

print(a.ndim)
print(a[2])

print(a[:3 , 0:2])
print(a[:1:-1 , :1])

print(50*"#")

#show array data type
my__array1=np.array([1,2,3])
my__array2=np.array([10.25,25.2,36.9])
my__array3=np.array(["ibrahim","abdelsattar","abdelgawad"])

print(my__array1.dtype)
print(my__array2.dtype)
print(my__array3.dtype)

print(50*"#")

#create array with specific data type

my__array4=np.array([1,2,3], dtype="f") # float or 'float' or 'f'
my__array5=np.array([10.25,25.2,36.9], dtype=int) # int or 'int' or 'i'
#my__array6=np.array(["ibrahim","abdelsattar","abdelgawad"], dtype=int) #Value Error

print(my__array4.dtype)
print(my__array5.dtype)
#print(my__array6.dtype)

print(50*"#")

#Change Date Type Of Existing Array

my__array7=np.array([0,1,2,3,0,4])
print(my__array7.dtype)
print(my__array7)

print(50*"#")

my__array7=my__array7.astype("float")
print(my__array7.dtype)
print(my__array7)

print(50*"#")

my__array7=my__array7.astype("bool")
print(my__array7.dtype)
print(my__array7)

print(50*"#")

# Test Capacity

my__array8=np.array([100,200,300,400],dtype='f')
print(my__array8.dtype)
print(my__array8[0].itemsize) #4 bytes

print(50*"#")

my__array8=my__array8.astype("float")
print(my__array8.dtype)
print(my__array8[0].itemsize) #8 bytes

print(50*"#")

#Arithmetic Operations

myy_array1=np.array([10,20,30])
myy_array2=np.array([5,2,4])

print(myy_array1+myy_array2)
print(myy_array1-myy_array2)
print(myy_array1*myy_array2)
print(myy_array1/myy_array2)

print(50*"#")

myy_array3=np.array([[1,4],[5,9]])
myy_array4=np.array([[2,7],[10,5]])

print(myy_array3+myy_array4) # result [[3 , 11],[15 , 14]]
print(myy_array3-myy_array4) # result [[-1 , -3],[-5 , 4]]
print(myy_array3*myy_array4) # result [[2 , 28],[50 , 45]]
print(myy_array3/myy_array4) # result [[0.5 , 0.57142857],[0.5 , 1.8]]

print(50*"#")

#min, max, sum

myy_array5=np.array([20,30,40])

print(myy_array5.min())
print(myy_array5.max())
print(myy_array5.sum())

print(50*"#")

myy_array6=np.array([[20,30,40],[50,60,70]])

print(myy_array6.min())
print(myy_array6.max())
print(myy_array6.sum())

print(50*"#")

#Ravel

myy_array7=np.array([[20,30,40],[50,60,70]])
print(myy_array7.ravel())

myy_array8=np.array([[[20,30,40],[50,60,70],[80,90,100],[110,120,130]]])
print(myy_array8.ndim)
print(myy_array8.ravel())
x=myy_array8.ravel()
print(x.ndim)

print(50*"#")

#Shape

my_array__1=np.array([1,2,3,4])
print(my_array__1.ndim)
print(my_array__1.shape)

print(50*"#")

my_array__2=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(my_array__2.ndim)
print(my_array__2.shape)

print(50*"#")

my_array__3=np.array([[[1,2,3,4,5],[1,2,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])
print(my_array__3.ndim)
print(my_array__3.shape)

print(50*"#")

#Reshape

my_array__4=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(my_array__4.ndim)
print(my_array__4.shape)

reshaped_array4=my_array__4.reshape(3,2,2)
print(reshaped_array4)
print(reshaped_array4.ndim)
print(reshaped_array4.shape)

print(50*"#")

my_array__5=np.array([[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]])
print(my_array__5.ndim)
print(my_array__5.shape)

print(50*"#")

#reshaped_array5=my_array__5.reshape(-1)
#reshaped_array5=my_array__5.reshape(4,5)
reshaped_array5=my_array__5.reshape(2,5,2)
print(reshaped_array5.ndim)
print(reshaped_array5.shape)
print(reshaped_array5)