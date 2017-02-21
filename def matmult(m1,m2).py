def matmult(m1,m2):
	result=[[0 for row in range(len(m1))] for col in range(len(m2[0]))]
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			for k in range(len(m2)):
				result[i][j]=result[i][j]+m1[i][k]*m2[k][j]

	return(result)