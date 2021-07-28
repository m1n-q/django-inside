def print_numbers():
	file = open('numbers.txt')
	nums = file.readline().rstrip().split(',')
	for num in nums:
		print(num)


if __name__ == '__main__':
	print_numbers()
