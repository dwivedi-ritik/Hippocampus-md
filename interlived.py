s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

#two string will inlived with each other if and only if i removed first strinng in s second string should appear in s3
def check(s1 , s2, s3):
	temp = ""
	for i , el in enumerate(s3):
		for j ,el_s1 in enumerate(s1):
			if el == el_s1:
				s3[i] = "0"
				s1.pop(j)
				break
	
	resulted = "".join([x for x in s3 if x != "0"])

	if len(s1):
		return False

	if "".join(sorted(resulted)) == "".join(sorted(s2)):
		return True
	return False
print(check(list(s1) , list(s2) , list(s3)))


