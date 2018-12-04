import math
import time
number = int(input('√'))
start = time.time()
squared = []
for item in range(1,int(math.sqrt(number))+1):
	if (number/item) % 1 == 0:
		squared.append(item**2)
# print (squared)
if math.sqrt(number) % 1 == 0:
	print ("answer: %d" % (int(math.sqrt(number))))
else:
	for item in squared:
		if (number / item) % 1 == 0:
			radical = number/item
			highest_sqr = item

#   below comments were from previous testing
#	print ("HIGHEST SQUARED")
#	print (highest_sqr)
#	print ("RADICAL")
#	print (radical)
	left = int(math.sqrt(highest_sqr))
	if (left == 1):
		# meaning the input could not be simplified
		print("simplified: √%s" % (int(radical)))
	else:
		print ("simplified: %s√%s" % (left,int(radical)))
	print ("float =", math.sqrt(number))
print ("runtime: %f sec" % (time.time() - start))
