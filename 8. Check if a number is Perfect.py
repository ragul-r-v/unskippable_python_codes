n = 28
div_sum=0
for i in range(1,n//2+1):
	if n%i == 0:
		div_sum += i
print(f"{n} is perfect? {div_sum == n}")

