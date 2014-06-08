
import jinja2
import os
from collections import namedtuple

TemplateData = namedtuple('TemplateData', 'first_web_page second_web_page text_similarity '
                                          'image_similarity template_path html_path')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def create_result_as_html(template_data):
    """
        Generates html file containing results of web pages comparison
        :param template_data: Contains data required to create html file.
        :type template_data: TemplateData.
    """

    template = JINJA_ENVIRONMENT.get_template(template_data.template_path)
    template_values = {
        'first': template_data.first_web_page,
        'second': template_data.second_web_page,
        'categories': template_data.text_similarity,
        'images': template_data.image_similarity,
    }
    html = template.render(template_values)
    with open(template_data.html_path, "w") as text_file:
        text_file.write(html)
