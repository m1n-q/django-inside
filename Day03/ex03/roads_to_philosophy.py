import sys
from bs4 import BeautifulSoup
from local_lib import requests

def find_philo(keyword, road):

	if (keyword == 'Philosophy'):
		road.append(keyword)
		return True
	if (keyword in road):
		print("It leads to an infinite loop!")
		return False

	s = requests.Session()
	url = "http://en.wikipedia.org"

	res = s.get(url=url + '/wiki/' + keyword)
	if res.status_code != 200:
		print(keyword)
		print(res)
		return False
	html = res.text
	soup = BeautifulSoup(html, 'html.parser')
	div_content = soup.find("div", class_="mw-parser-output")
	p = div_content.find('p')

	link = None
	for a in p.find_all('a'):
		if a.has_attr('href'):
			if not a['href'].startswith('#'):
				link = a['href']
				break

	if not link:
		print("It's Dead End!")
		return False

	else:
		road.append(keyword)
		return find_philo(link.split('/')[-1], road)


def parser_caller(keyword):

	road = []
	if find_philo(keyword, road) == True:
		for r in road:
			print(r)
		print( len(road), "roads from " + keyword + " to Philosophy" )
	else:
		return


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("require 1 argument")
	else:
		parser_caller(sys.argv[1])
