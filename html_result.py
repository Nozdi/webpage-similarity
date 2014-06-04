
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HtmlResultCreator(object):

    def __init__(self, template_path):
        self.template = JINJA_ENVIRONMENT.get_template(template_path)
        self.first = "dupa"
        self.second = "kupa"
        self.categories = {'a': (1, 2), 'b': (3, 4), 'c': (5, 6)}
        self.images = {}

    def createm(self, html_path):
        template_values = {
            'first': self.first,
            'second': self.second,
            'categories': self.categories,
            'images': self.images,
        }
        html = self.template.render(template_values)
        print html
        with open(html_path, "w") as text_file:
            text_file.write(html)

if __name__ == '__main__':
    dupa = HtmlResultCreator(template_path="template.html")
    dupa.createm()
