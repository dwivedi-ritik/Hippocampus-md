

#I will write a recursive algorithm to solve this problem

def longestPalin(i , j , x , obj):
	if i <= j:
		if i == j:
			return 1
		
		if obj.get((i , j)):
			return obj[(i , j)]

		if x[i] == x[j]:
			obj[(i , j)] = 2 + longestPalin(i+1 , j-1 , x , obj)
			return obj[(i , j)]
		else:
			obj[(i , j)] =  max(longestPalin(i+1 , j , x , obj) , longestPalin(i , j-1 , x , obj))
			return obj[(i,j)]
	return 0


word = "subsequenceisasequencethatcanbederivedfromanothersequencebydeletingsomeornoelementswithoutchangingtheorderoftheremainingelements"

print(longestPalin(0 , len(word) - 1 , word , {}))