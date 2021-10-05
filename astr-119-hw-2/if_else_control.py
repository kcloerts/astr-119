#define function 
def flow_control(k):

	#define a string  based on the value
	# of k

	if(k==0):

		s = "Variable k = %d equals 0." % k

	elif(k==1):
	
		s = "Variable k = %d equals 1." % k 

	else:
	
		s = "Variable k = %d does not equal  or 1." % k 
		

	#using %d tells python to use an integer number 
	# to place into the string
	# in this case the value for k placed into the string
	#to replace %d with the integer value for k


	#print the variable
	print(s)

#define the main function
def main():
	
	#declare an integer
	i = 0

	#try flow_control for 0,1,2
	flow_control(i)

	i = 1
	flow_control(i)
	i = 2
	flow_control(i)

#run the program
if __name__=="__main__":
	main()					