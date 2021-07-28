def var_to_dict() -> dict:
	d = [
		('Hendrix', '1942'),
		('Allman', '1946'),
		('King', '1925'),
		('Clapton', '1945'),
		('Johnson', '1911'),
		('Berry', '1926'),
		('Vaughan', '1954'),
		('Cooder', '1947'),
		('Page', '1944'),
		('Richards', '1943'),
		('Hammett', '1962'),
		('Cobain', '1967'),
		('Garcia', '1942'),
		('Beck', '1944'),
		('Santana', '1947'),
		('Ramone', '1948'),
		('White', '1975'),
		('Frusciante', '1970'),
		('Thompson', '1949'),
		('Burton', '1939')
	]
	dic = dict()
	for t in d:
		if t[1] in dic:
			dic[t[1]].append(t[0])
		else:
			dic[t[1]] = [t[0]]
	return dic


def print_dict(d : dict):
	for k, v in d.items():
		print(k, ':', end='')
		for elems in v:
			print(' ', end='')
			print(elems, end='')
		print()


if __name__ == '__main__':
	print_dict(var_to_dict())
