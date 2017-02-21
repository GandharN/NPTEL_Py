def alternate(l):
	if l==[]:
		return(True)
	for i in range(1,len(l)-1):
		if l[i]>l[i+1] and l[i]>l[i-1]:
			continue
		if l[i]<l[i+1] and l[i]<l[i-1]:
			continue
		else:
			return(False)
	if i==len(l)-2:
		return(True)