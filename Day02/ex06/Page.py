
from os import write
from elements import *

class Page:
	def __init__(self, element) -> None:

		#NOTE: Elem을 상속받는 클래스 인스턴스를 인자로 받아와야 합니다.
		if isinstance(element, Elem):
			self.element = element

		else:
			raise Elem.ValidationError


	def is_valid(self):
		return self.__is_valid_recursive(self.element)


	def __is_valid_recursive(self, elem):

		if not elem or type(elem) == Text:
			return True

		if type(elem) == Html:
			type_list = list(map(type, elem.content))
			if Head not in type_list or Body not in type_list:
				return False
			if type_list.index(Head) > type_list.index(Body):
				return False
			for t in type_list:
				if t != Head and t != Body:
					return False



		for c in elem.content:
			if type(c) not in Elem.__subclasses__() + [Text]:
				return False

			if type(c) == Head:
				type_list = list(map(type, c.content))
				if type_list.count(Title) != 1:
					return False

			if type(c) == Body or type(c) == Div:
				type_list = list(map(type, c.content))
				available = [H1, H2, Div, Table, Ul, Ol, Span, Text]
				for t in type_list:
					if t not in available:
						return False

			if type(c) in [Title, H1, H2, Li, Th, Td]:
				type_list = list(map(type, c.content))
				if type_list.count(Text) > 1:
					return False

			if type(c) == P:
				type_list = list(map(type, c.content))
				for t in type_list:
					if t != Text:
						return False

			if type(c) == Span:
				type_list = list(map(type, c.content))
				available = [P, Text]
				for t in type_list:
					if t not in available:
						return False

			if type(c) == Ol or type(c) == Ul:
				type_list = list(map(type, c.content))
				if type_list.count(Li) < 1:
					return False
				for t in type_list:
					if t != Li:
						return False

			if type(c) == Tr:
				type_list = list(map(type, c.content))
				if Th in type_list and Td in type_list:
					return False
				if type_list.count(Th) < 1 and type_list.count(Td) < 1:
					return False
				for t in type_list:
					if t != Th and t != Td:
						return False

			if type(c) == Table:
				type_list = list(map(type, c.content))
				for t in type_list:
					if t != Tr:
						return False

			if self.__is_valid_recursive(c) == False:
				return False

		return True

	def __str__(self) -> str:
		if type(self.element) == Html:
			# print("==================")
			# print(Text(self.element))		#NOTE: Text 의 __str__ 메소드는, Text 의 인스턴스인 채로 출력할때만 적용!
			# print("==================")
			return Text("<!DOCTYPE html>\n") + Text(self.element)		#NOTE: Text 를 씌워도 출력하지 않는 이상 값이 바뀐게 아니니까, 제값이 들어감. Page 로서 출력하면 ㄱㅊ!
		else:
			return Text(self.element)


	def write_to_file(self, file_name:str):
		if type(self.element) != Html:
			return
		file = open(file_name, 'w')
		file.write("<!DOCTYPE html>\n")
		file.write(Text(self.element))


if __name__ == '__main__':
	head = Head([Title(Text("Hello grodund")), Elem(tag="style", content=Text(".dummy {\n    font-size:50px; color:red;\n  }"))])
	div = Div(([Text("Hello grodund")]), {"class":"dummy"})
	body = Body((Text("ABC")))
	table = Table([Tr([Th(Text("Name")), Th(Text("Surname")), Th(Text("Age"))]), Tr([Td(Text("Minkyu")), Td(Text("Shin")), Td(Text("500"))])])
	html = Html(attr={"lang": "en"})

	html.add_content([head,body])
	body.add_content(div)

	page = Page(html)
	head.add_content(Meta({"charset":"utf-8"}))
	# print(page.is_valid())
	# print(page)
	page.write_to_file("abc.html")
