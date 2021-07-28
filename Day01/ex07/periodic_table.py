def txt_to_list() -> dict:
	txt = open("periodic_table.txt")
	elems = txt.readlines()
	elems = list(map(lambda x : x.split(','), elems))
	elem_attrs = list()
	for elem in elems:
		name_and_pos = elem[0].split('=')
		elem.insert(1, name_and_pos[1])
		elem[0] = name_and_pos[0]
		attrs_dict = dict()
		for attr in elem:
			if ':' in attr:
				l = attr.split(':')
				if 'number' in l[0] or 'position' in l[0]:
					attrs_dict[l[0].strip()] = (int)(l[1].strip())
				else:
					attrs_dict[l[0].strip()] = l[1].strip()
			else:
				attrs_dict["name"] = elem[0].strip()
		elem_attrs.append(attrs_dict)
		elem_attrs.sort(key=lambda x : x["number"])
	return elem_attrs


def init_html(lang: str=''):
	page = open("periodic_table.html", 'w')
	page.write("<!DOCTYPE html>\n")
	page.write("<html")
	if not lang:
		page.write(">\n")
	else:
		page.write(" lang=")
		page.write("\"")
		page.write(lang)
		page.write("\">\n")
	return page


def close_html(page):
	page.write("</html>")

def write_content(page, tabs: int, content: str):
	page.write("\t" * tabs)
	page.write(content)
	page.write("\n")

def set_title(page, tabs: int, title: str):
	page.write("\t" * tabs)
	page.write("<title>")
	page.write(title)
	page.write("</title>\n")

def open_style_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("<style>\n")

def close_style_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</style>\n")

def set_tag_style(page, tabs, tag, style):
	page.write("\t" * tabs)
	page.write(tag)
	page.write(" {\n")
	style_list = style.split(";")
	for st in style_list:
		if not st:
			continue
		page.write("\t" * (tabs + 1))
		page.write(st)
		page.write(";\n")
	page.write("\t" * tabs)
	page.write("}\n")


def open_head_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("<head>\n")
	page.write("\t" * (tabs + 1))
	page.write('<meta charset="UTF-8">\n')

def close_head_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</head>\n")

def open_body_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("<body>\n")

def close_body_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</body>\n")

def open_table_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("<table>\n")

def close_table_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</table>\n")

def	open_tr_tag(page, tabs: int, style: str=''):
	page.write("\t" * tabs)
	if not style:
		page.write("<tr>\n")
	else:
		page.write("<tr style=\"")
		page.write(style)
		page.write("\">\n")

def	close_tr_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</tr>\n")

def	open_td_tag(page, tabs: int, style: str=''):
	page.write("\t" * tabs)
	if not style:
		page.write("<td>\n")
	else:
		page.write("<td style=\"")
		page.write(style)
		page.write("\">\n")

def	close_td_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</td>\n")

def	open_th_tag(page, tabs: int, style: str=''):
	page.write("\t" * tabs)
	if not style:
		page.write("<th>\n")
	else:
		page.write("<th style=\"")
		page.write(style)
		page.write("\">\n")

def	close_th_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</th>\n")

def	write_h4_tag(page, tabs: int, content: str):
	page.write("\t" * tabs)
	page.write("<h4 style=\"margin-top:0px;margin-bottom:0px;\">")
	page.write(content)
	page.write("</h4>\n")

def	open_ul_tag(page, tabs: int, style: str=''):
	page.write("\t" * tabs)
	if not style:
		page.write("<ul>\n")
	else:
		page.write("<ul style=\"")
		page.write(style)
		page.write("\">\n")

def	close_ul_tag(page, tabs: int):
	page.write("\t" * tabs)
	page.write("</ul>\n")

def write_li_tag(page, tabs: int, content: str, style: str=''):
	page.write("\t" * tabs)
	if not style:
		page.write("<li>")
	else:
		page.write("<li style=\"")
		page.write(style)
		page.write("\">")
	page.write(content)
	page.write("</li>\n")


def make_elem_box(page, attrs: dict):
	row_leading_number = [1, 3, 11, 19, 37, 55, 87]
	row_trailing_number = [2, 10, 18, 36, 54, 86, 118]
	if attrs["number"] in row_leading_number:
		open_tr_tag(page, 3, "position:relative;")
		open_th_tag(page, 4, "border: 1px solid black;")
		write_content(page, 5, str(row_leading_number.index(attrs["number"]) + 1))
		close_th_tag(page, 4)


	open_td_tag(page, 4, "border: 1px solid black; position:absolute; left:%dpx;" %(((attrs["position"] + 1) * 100)))
	write_h4_tag(page, 5, attrs["name"])
	open_ul_tag(page, 6, "text-align:left;")
	write_li_tag(page, 7, "No. " + str(attrs["number"]))
	write_li_tag(page, 7, attrs["small"], "font-weight:bold; font-style:italic;")
	write_li_tag(page, 7, attrs["molar"])
	write_li_tag(page, 7, attrs["electron"])
	close_ul_tag(page, 6)
	close_td_tag(page, 4)
	if attrs["number"] == 1:
		for i in range(2, 18):
			open_td_tag(page, 4, "border: 1px solid black; position:absolute; left:%dpx;" %(i * 100))
			close_td_tag(page, 4)
	if attrs["number"] == 4 or attrs["number"] == 11:
		for i in range(3, 13):
			open_td_tag(page, 4, "border: 1px solid black; position:absolute; left:%dpx;" %(i * 100))
			close_td_tag(page, 4)
	if attrs["number"] == 56 or attrs["number"] == 88:
		open_td_tag(page, 4, "border: 1px solid black; position:absolute; left:%dpx;" %(3 * 100))
		close_td_tag(page, 4)
	if attrs["number"] in row_trailing_number:
		close_tr_tag(page, 3)



def write_on_page(title: str):
	page = init_html(lang="en")

	open_head_tag(page, 1)
	set_title(page, 2, title)

	open_style_tag(page, 2)
	set_tag_style(page, 3, "ul", "font-size: 12.5px;padding-left:0px")
	set_tag_style(page, 3, "li", "list-style-type: none;")
	set_tag_style(page, 3, "table", "border-spacing:0px;")
	set_tag_style(page, 3, "tr", "height: 100px;")
	set_tag_style(page, 3, "th", "height: 100px;width: 100px;padding:0px")
	set_tag_style(page, 3, "td", "height: 100px;width: 100px;padding:0px;")


	close_style_tag(page, 2)
	close_head_tag(page, 1)


	open_body_tag(page, 1)
	open_table_tag(page, 2)
	open_tr_tag(page, 3, "position:relative;")
	open_th_tag(page, 4, "border: 1px solid black;height: 100px;width: 100px;")
	write_content(page, 5, "period\group")


	close_th_tag(page, 4)

	for i in range(1, 19):
		open_td_tag(page, 4, "border: 1px solid black; position:absolute; left:%dpx;" %(i * 100))
		write_content(page, 5, str(i))
		close_td_tag(page, 4)


	elems = txt_to_list()
	for elem in elems:
		make_elem_box(page, elem)


	close_table_tag(page, 2)
	close_body_tag(page, 1)
	close_html(page)


if __name__ == '__main__':
	write_on_page("Day01 - ex07")
