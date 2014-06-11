#!/usr/bin/env python
"""
.. module:: main
    :synopsis: This module shows example usage
"""

import fix_path
import os
import webbrowser
from similarity import WebPage
from utils import (
    TemplateData,
    create_result_as_html,
)


if __name__ == '__main__':
    w1 = WebPage(
        url="http://automotive.about.com/b/2012/06/14/how-to-become-a-new-car-dealer.htm"
    )
    w2 = WebPage(
        url="http://ipod.about.com/od/KidsiPhoneiPodTouch/tp/Roadtrips-With-Iphone-And-Apps.htm"
    )

    text_similarity = w1.get_text_similarity(w2)

    image_similarity = w1.get_image_similatiry(w2)

    template_data = TemplateData(
        template_path="template.html",
        first_web_page=w1,
        second_web_page=w2,
        text_similarity=text_similarity,
        image_similarity=image_similarity,
        html_path="./Output.html")

    create_result_as_html(template_data)

    current_dir = os.path.dirname(os.path.realpath(__file__))
    webbrowser.open_new("file://{}/Output.html".format(current_dir))
