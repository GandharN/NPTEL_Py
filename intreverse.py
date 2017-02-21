def intreverse(n):
	n=int(n)
	m=0
	while n>0:
		x=n%10
		m=m*10+x
		n=n//10
	return(m)

intreverse(368)
intreverse(798798)
intreverse(7)
