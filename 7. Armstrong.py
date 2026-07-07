num = 123
s=str(num)
power = len(s)
arm_sum = sum(int(d)**power for d in s)
print(f"{num} is Armstrong? {arm_sum == num}")

