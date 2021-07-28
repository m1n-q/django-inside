import settings
import sys
import os


def load_template(arg):

	try:
		template = open(arg, 'r')
	except FileNotFoundError:		#os.file.isfile
		return -1
	except PermissionError:		 	#os.access('my_file', os.R_OK)
		return -2
	except IsADirectoryError:		#os.file.isdir
		return -3
	return template


def render_template(template):

	text = "".join(template.readlines())
	settings_dict = { k : v for k, v in vars(settings).items() if not k.startswith('__') }
	for k, v in settings_dict.items():
		pattern = "{" + k + "}"
		text = text.replace(pattern, v)

	return text


def export_html(file_name, text):
	f = open(file_name + ".html", 'w')
	f.write(text)


def main():
	if len(sys.argv) != 2:
		print("Error : 인자 개수")
		return

	file_name = os.path.splitext(sys.argv[1])[0]
	file_ext = os.path.splitext(sys.argv[1])[1]
	if file_ext != ".template":
		print("Error : 확장자")
		return
	template = load_template(sys.argv[1])
	# if load_template(sys.argv[1]) < 0:
	# 	print("Error")
	text = render_template(template)
	export_html(file_name, text)

if __name__ == '__main__':
	main()






'''
잘못된 파일 확장자, 존재하지 않는 파일 또는 잘못된 인자값 개수 등의 예외는 알맞게 처리되어야 합니다.
여러분은 myCV.template 파일을 제출해야 하고,
해당 파일은 HTML로 변환되었을 때 최소한 html과 이력서의 기본 구조
(doctype, head, body, 페이지의 title, 이력서 작성자의 이름과 성씨, 나이와 직업) 를 포함해야 합니다.
물론, 이러한 정보들은 .template 파일에 직접적으로 표시되진 않을 것입니다.
'''

