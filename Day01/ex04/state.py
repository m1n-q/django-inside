import sys


def search_state(arg: str) -> None:
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
	for region_code, capital in capital_cities.items():
		if capital == arg:
			for region, code in states.items():
				if region_code == code:
					print(region)
					break
			break
	else:
		print("Unknown capital city")

def main():
	if len(sys.argv) != 2:
		return
	search_state(sys.argv[1])

if __name__ == '__main__':
	main()
