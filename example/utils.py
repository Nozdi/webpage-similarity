import jinja2
import os
from collections import namedtuple
from operator import itemgetter


TemplateData = namedtuple(
    'TemplateData',
    ['first_web_page', 'second_web_page',
     'text_similarity', 'image_similarity',
     'template_path', 'html_path']
)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
JINJA_ENVIRONMENT.globals.update(zip=zip)


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
        'first_terms': sorted(
            template_data.first_web_page.content.terms_membership.iteritems(),
            key=itemgetter(1), reverse=True
        )[0:10],
        'second_terms': sorted(
            template_data.second_web_page.content.terms_membership.iteritems(),
            key=itemgetter(1), reverse=True
        )[0:10]
    }
    html = template.render(template_values)
    with open(template_data.html_path, "w") as text_file:
        text_file.write(html)


def print_sorted_dict(dictionary, name):
    print name
    sdict = sorted(dictionary.iteritems(), key=itemgetter(1), reverse=True)
    for key, value in sdict:
        print str(key), ":", value
