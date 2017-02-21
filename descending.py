def descending(l):
	if l==[]:
		return(True)
	for i in range(len(l)-1):
		if l[i]<l[i+1]:
			return(False)
		if i==len(l)-2:
			return(True)

	