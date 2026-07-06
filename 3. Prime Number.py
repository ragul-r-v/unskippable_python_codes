n = 79
if n<=1:
	print(f"{n} is not a prime number")
else:
	is_prime = True 
	for I in range(2,int(n**0.5)+1):
		if n % I ==0:
			is_prime = False
			break
	print(f"{n} is prime" if is_prime else f"{n} is not a prime")

