from collections import Counter
# string = "ABAB"

# k = 2

# print( len(string) - Counter(string).most_common()[0][1]) 

# print(len(string))


def characterReplacement(s: str, k: int) -> int:
    i , j = 0 , 0
    max_len = 0
    curr_count = 0
    table = { x:0 for x in range(26) }

    last_count = 0
    while j < len(s):
    	string = s[i:j+1]
    	
    	curr_count = len(string) 

    	table[ ord(s[j]) - 65 ] += 1

    	most_common = max(table.values())

    	check =  curr_count - most_common    
    	
    	if check <= k:
    		max_len = max(max_len , curr_count)
    		j += 1
    	else:
	    	table[ ord(s[i]) - 65 ] -= 1
	    	table[ ord(s[j]) - 65 ] -= 1

    		i += 1

    return max_len

if __name__ == "__main__":
	# print(characterReplacement("ABAB" , 1))	
	print(characterReplacement("AABABBA" , 1))
	# print(characterReplacement("AJAAAJD" , 3))


# 1
# 2
# 2
# 3
# 3
# 3
# 4
# 4
# 4
# 5
# [Finished in 38ms]