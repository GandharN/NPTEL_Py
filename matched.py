def matched(s):
	(c1,c2)=(0,0)
	bracket=[]
	for i in range(0,len(s)):
		if s[i]=='(' or s[i]==')':
			bracket.append(s[i])
	

	l=len(bracket)
	if int(l)%2!=0:
		return(False)
	

	i=0
	count=0


	for i in range(0,len(bracket)):
		if bracket[i]=='(' and bracket[len(s)-i]==')':
			count=+1
	if count==len(bracket)/2:
		return(True)	
