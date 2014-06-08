
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class HtmlResultCreator(object):

    def __init__(self, template_path):
        self.template = JINJA_ENVIRONMENT.get_template(template_path)

    def create(self, html_path):

        template_values = {
            'first': self.first_web_page,
            'second': self.second_web_page,
            'categories': self.text_similarity,
            'images': self.image_similarity,
        }
        html = self.template.render(template_values)
        with open(html_path, "w") as text_file:
            text_file.write(html)
