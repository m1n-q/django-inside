#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    # [...]

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        self.tag=tag
        self.attr=attr
        self.tag_type=tag_type


        if type(content) != list and content != None and \
            not (isinstance(content, Text)) and not (isinstance(content, Elem)):
            raise Elem.ValidationError
        if content == None or content == Text(''):
            self.content = ['']
        elif type(content) == list:
            for c in content:
                if not (isinstance(c, Text)) and not (isinstance(c, Elem)):
                    raise Elem.ValidationError
            self.content = content
        else:
            self.content = Text(content).split('\n')

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        attr = self.__make_attr()
        content = self.__make_content()
        if self.tag_type == 'double':
            result = "<" + self.tag + attr + ">" + content + "</" + self.tag + ">"
        elif self.tag_type == 'simple':
            # [...]
            pass
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''

        result = '\n'
        for elem in self.content:
            if elem == Text(''):
                continue
            result += '  ' + Text(elem) + '\n'
        if result == '\n':
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif isinstance(content, Elem):
            tmp = Text(content).split('\n')
            for elem in tmp:
                self.content.append('  ' + Text(elem))
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

    elem = Elem()
    elem2 = Elem("body", content=Elem("div"))

    elem.add_content(Elem("body",content=Elem("sector", content=Elem("table", attr = {"style":"border:1px black solid;"},content=Elem("td",content=Text(''))))))
    # elem2 = Elem("body",content=Elem("sector", content=Elem("table", attr = {"style":"border:1px black solid;"},content=Elem("td",content=Text('')))))

    elem.add_content(elem2)
    print(elem)
