s = list("dcab")

pairs = [[0,3],[1,2]]

n = len(s)

i = 0

while i < len(pairs):
	m , n = pairs[i]
	if s[m] > s[n]:
		s[m] , s[n] = s[n] , s[m]
	else:
		i += 1

print(s)