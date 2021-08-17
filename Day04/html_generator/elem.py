#!/usr/bin/python3
import sys

class Text(str):

    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:


    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):

        if not tag:
            raise Elem.ValidationError
        if type(attr) != dict:
            raise Elem.ValidationError
        if tag_type != 'double' and tag_type != 'simple':
            raise Elem.ValidationError
        if type(content) != list and content != None and \
            not (isinstance(content, Text)) and not (isinstance(content, Elem)):
            raise Elem.ValidationError
        self.tag=tag
        self.attr=attr
        self.tag_type=tag_type
        self.content = []


        if content == None or content == Text(''):
            self.content = []

        elif type(content) == list:
            for c in content:
                if not (isinstance(c, Text)) and not (isinstance(c, Elem)):
                    raise Elem.ValidationError
            self.content += content

        elif isinstance(content, Elem) or type(content) == Text:
            self.content.append(content)

    def __str__(self):

        attr = self.__make_attr()
        content = self.__make_content()

        if self.tag_type == 'double':
            result = "<" + self.tag + attr + ">" + content + "</" + self.tag + ">"
        elif self.tag_type == 'simple':
            result = "<" + self.tag + attr + " />"
        return result


    def __make_attr(self):

        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result


    def __make_content(self):

        if len(self.content) == 0:
            return ''


        result = '\n'
        for elem in self.content:
            if elem == Text(''):
                continue

            if isinstance(elem, Elem):
                for e in Text(elem).split('\n'):
                    result += '  ' + Text(e) + '\n'

            elif type(elem) == Text:
                result += '  ' + elem + '\n'

            # elif type(elem) == list:
            #     for e in elem:
            #         if e != Text(''):
            #             result += '  ' + Text(e) + '\n'


        if result == '\n':
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError

        if isinstance(content, Elem):
                self.content.append(content)

        elif type(content) == list:
            for elem in content:
                if elem != Text(''):
                    self.content.append(elem)

        elif content != Text(''):
            self.content.append(content)


    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

    class ValidationError(Exception):
        def __init__(self):
            super().__init__("Validation Error")


if __name__ == '__main__':
    print(Text(sys.argv[1]))
