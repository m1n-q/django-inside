def my_var():
	i = 42
	s1 = "42"
	s2 = "quarante-deux"
	f = 42.0
	b = True
	l = [42]
	d = {42:42}
	t = (42,)
	s = set()
	print(i, "has a type", type(i))
	print(s1, "has a type", type(s1))
	print(s2, "has a type", type(s2))
	print(f, "has a type", type(f))
	print(b, "has a type", type(b))
	print(l, "has a type", type(l))
	print(d, "has a type", type(d))
	print(t, "has a type", type(t))
	print(s, "has a type", type(s))


if __name__ == '__main__':
	my_var()
