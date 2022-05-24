def loop_fib(n):
	p1 = 0
	p2 = 1

	if n == 1:
		print(p1)

	elif n == 2:
		print(p2)

	else:
		while n > 2:
			res = p1 + p2
			p1 = p2
			p2 = res
			n -= 1

		print(res)
	
res = loop_fib(int(input('Qual posição da sequência? ')))
