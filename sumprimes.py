def sumprimes(l):
	primes=[]
	for i in range(0,len(l)):
		if l[i]>0:
			for j in range(2,l[i]):
				if l[i]%j==0:
					break
			if j==l[i]-1:
				primes.append(l[i])
		else:
			continue		
	s=sum(primes)
	return(s)