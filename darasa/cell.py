def cell(x,y):
	anchor = (2*x)*(x-1) + 1
	det = x - 1;
	
	if(x + y) <= 100001 or (x + y) < 2:
		if(x == y):
			return anchor
		elif(x < y):
			for i in range (x , y):
				x_var = i + det;
				anchor += x_var;
			return anchor;

		elif (x > y):
			for i in range (y , x):
				x_var = i + det;
				anchor -= x_var;
			return anchor;
	else:
		print('Too huge')

