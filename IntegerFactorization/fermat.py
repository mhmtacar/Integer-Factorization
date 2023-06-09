
from math import ceil, sqrt

def FermatFactors(n):

	if(n<= 0):
		return [n]

	if(n % 2) == 0:
		return [n / 2, 2]
		
	a = ceil(sqrt(n))

	if(a * a == n):
		return [a, a]

	while(True):
		b1 = a * a - n
		b = int(sqrt(b1))
		if(b * b == b1):
			break
		else:
			a += 1
	return [a-b, a + b]
	
# Driver Code
num = int(input("Enter a number whose factors are to be found: "))
a = FermatFactors(num)
print("The factors of " + str(num) + " are " + str(a) );




