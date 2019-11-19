# -*- coding: utf-8 -*-
"""
    This module contains helper functions to parse coursera course html page.
"""


def parse_course_raw_html(soup):
    about_course_divs = soup.find_all("div", {"class": "rc-TogglableContent about-section collapsed"})
    about_course = about_course_divs[0].p.get_text()

    syllabus_section_headers = []
    syllabus_section_paragraphs = []

    week_divs = soup.find_all("div", {"class": "Row_nvwp6p SyllabusWeek m-b-3"})
    for week_div in week_divs:
        syllabus_divs = week_div.find_all('div', {'class': 'Col_i9j08c-o_O-xsCol12_1m1ceo5-o_O-mdCol10_1eb21lj-o_O-lgCol10_ra5osh p-b-1 border-bottom'})
        for syllabus_div in syllabus_divs:
            for section in syllabus_div.children:
                syllabus_section_headers.append(section.find_next('h2').get_text())
                syllabus_section_paragraphs.append(section.find_next('p').get_text())

    week_divs = soup.find_all("div", {"class": "Row_nvwp6p SyllabusWeek"})
    for week_div in week_divs:
        syllabus_divs = week_div.find_all('div', {'class': 'Col_i9j08c-o_O-xsCol12_1m1ceo5-o_O-mdCol10_1eb21lj-o_O-lgCol10_ra5osh'})
        for syllabus_div in syllabus_divs:
            for section in syllabus_div.children:
                syllabus_section_headers.append(section.find_next('h2').get_text())
                syllabus_section_paragraphs.append(section.find_next('p').get_text())

    return ' '.join([about_course, *syllabus_section_headers, *syllabus_section_paragraphs])