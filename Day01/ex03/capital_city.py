import sys

def search_capital_city(arg: str) -> None:
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
	if arg not in states.keys():
		print("Unknown state")
		return
	print(capital_cities[states[arg]])
	return

def main():
	if len(sys.argv) != 2:
		return
	search_capital_city(sys.argv[1])

if __name__ == '__main__':
	main()
