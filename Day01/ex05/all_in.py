from posixpath import splitext
import sys


def search_all(arg: str) -> None:
	strs = list(map(lambda x : x.strip(), arg.split(',')))
	states = {
    	"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	new_dict = dict()
	for k, v in states.items():
		if v in capital_cities:
			new_dict[k] = capital_cities[v]

	for s in strs:
		if not s:
			continue
		s2 = ' '.join(s.split())
		for state, captial in new_dict.items():
			if s2.lower() == state.lower() or s2.lower() == captial.lower():
				print(captial, "is the capital of", state)
				break
		else:
			print(s, "is neither a capital city nor a state")


def main():
	if len(sys.argv) != 2:
		return
	search_all(sys.argv[1])

if __name__ == '__main__':
	main()
