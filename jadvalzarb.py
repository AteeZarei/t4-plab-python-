def jadval_zarb(rows, columns):
	for i in range(1,rows+1):
		for j in range(1,columns+1):
			#print(i*j, end=' ')
			print('{:>4}'.format(i* j), end=' ')
		print()


while True:
	rows = int(input("Enter rows:"))
	columns = int(input("Enter columns:"))
	jadval_zarb(rows, columns)
	