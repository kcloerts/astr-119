#python exceptions let you deal with 
#unexpected results

try:
	print(a)	#this will throw an exception since it is not defined
except:
	print("a is not defined!")


#there are specific errors to help with cases
try:
	print(a)	#this will throw an exceptions since is not defined
except NameError:
	print("a is still not defined!")	
except:
	print("Something else went wrong.")

#this will break our program
#since a is not defined
print(a)				


#use try to test if something works as intended
#or to look for certain likely exceptions