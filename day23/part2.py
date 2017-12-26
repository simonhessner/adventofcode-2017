a = lb = ub = d = e = is_prime = g = not_prime_count = 0
lb = 106500
ub = 123500

for d in range(lb, ub+1, 17):
	is_prime = 1
	for e in range(2, d):
		if d % e == 0:
			is_prime = 0
	not_prime_count += (1-is_prime)

print(not_prime_count)