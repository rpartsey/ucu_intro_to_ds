# -*- coding: utf-8 -*-
"""
    This module contains helper functions to parse coursera GET request response with courses data.
"""


def process_coursera_batch(batch):
    courses = batch['data']['CatalogResultsV2Resource']['browseV2']['elements'][0]['courses']['elements']
    for course_data in courses:
        #pprint(course_data)

        course_rating_data = course_data['courseDerivativesV2']
        skills_data = course_rating_data['skillTags'] or []

        skills = [
            {
                'relevanceScore': skill['relevanceScore'],
                'skillName': skill['skillName'],
            } for skill in skills_data
        ]

        partneres_data = course_data['partners']['elements']
        partners = [
            {
                'partner_name': partner['name']
            } for partner in partneres_data
        ]

        yield {
            'averageFiveStarRating':    course_rating_data['averageFiveStarRating'],
            'avgLearningHoursAdjusted': course_rating_data['avgLearningHoursAdjusted'],
            'commentCount':             course_rating_data['commentCount'],
            'ratingCount':              course_rating_data['ratingCount'],

            'skills': skills,

            'course_id':       course_data['id'],
            'course_level':    course_data['level'],
            'course_name':     course_data['name'],
            'course_slug':     course_data['slug'],
            'course_workload': course_data['workload'] ,

            'partners': partners,
        }



def process_json_batches(json_batches_list):
    for batch in json_batches_list: 
        yield from process_coursera_batch(batch[0]) # batch is a list containing one element with metadata and courses data
