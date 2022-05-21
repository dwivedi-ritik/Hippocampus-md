from collections import Counter
n = 1000000

t = int(input())

prime = [True for i in range(n + 1)]
p = 2
while (p * p <= n):
    if (prime[p] == True):
        for i in range(p ** 2, n + 1, p):
            prime[i] = False
    p += 1

prime[0]= False
prime[1]= False

prime_set = []

last_prime = 2

for x in range(n+1):
	if prime[x]:
		last_prime = x
		prime_set.append(x)
	else:
		prime_set.append(last_prime)

result_set = []

count = 0
for i  , el in enumerate(prime_set[:-1]):
	if el+2 == prime_set[i+1]:
		count += 1
	result_set.append(count)

for _ in range(t):
	n = int(input())
	print(result_set[n-1])
# i = 5
# while i < 1000000:
# 	result.append(gen(i))
# 	i += 1


# print(gen(n))