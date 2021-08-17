import local_lib.path

if __name__ == '__main__':
	new_dir = local_lib.path.Path('new_dir')
	new_dir.mkdir()
	new_dir.cd()
	new_file = local_lib.path.Path('new_file')

	f = new_file.open('w+')
	f.write("new message\nnew line\nnew paragraph\n")
	f.seek(0)
	print(f.read())

