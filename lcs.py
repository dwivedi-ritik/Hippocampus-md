

# From my point of view i prefer recurstion compare to tabulation
# Tabulation is kind diffcult to undertand 

# take two pointer i point to s1 and j  point to s2

def lcs(s1 , s2 , i , j , obj):
	if i < len(s1) and j < len(s2):
		if obj.get((i , j)):
			return obj[(i , j)]
		if s1[i] == s2[j]:
			obj[(i , j)] =  1 + lcs(s1 , s2 , i+1 , j + 1 , obj)
			return obj[(i , j)]
			
		else:
			obj[(i , j)] = max(lcs(s1 , s2 , i + 1 , j , obj) , lcs(s1 , s2 , i , j+1 , obj))	
			
			return obj[(i , j)]
	return 0


s1 = "abcde"
s2 = "abde"

print(lcs(s1 ,s2 , 0 , 0 , {}))


