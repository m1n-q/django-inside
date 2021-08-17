import sys
import local_lib.requests
import local_lib.dewiki


def get_wiki(keyword):


	if len(keyword) == 0:
		return -1

	keyword = keyword.replace(' ', '_')

	s = local_lib.requests.Session()
	url = "https://fr.wikipedia.org/w/api.php"
	params = {
		"action" : "parse",
		"page" : keyword,
		"redirects" : True,
		"prop" : "wikitext",
		"formatversion" : 2,
		"format" : "json"
	}

	res = s.get(url = url, params=params)
	if not res.status_code:
		return 0
	elif res.status_code != 200:
		return res.status_code

	data = res.json()
	text = local_lib.dewiki.from_string(data['parse']['wikitext'])

	f = open(keyword + '.wiki', 'w')
	f.write(text)
	f.close()
	return res.status_code

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Required 1 argument")
	else:
		res = get_wiki(sys.argv[1])
		if res == 200:
			print('File saved as : ' + sys.argv[1].replace(' ', '_') + '.wiki')
		else:
			print('Error')
