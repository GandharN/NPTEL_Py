def matched(s):
	(c1,c2)=(0,0)

	for i in range(0,len(s)):
		if s[i]=='(':
			c1=c1+1
		if s[i]==')':
			c2=c2+1
		if c2>c1:
			return False

	if c1==c2:
		return True
	else:
		return False