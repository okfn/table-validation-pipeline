# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from jsontableschema import Field
from goodtables import checks


# Test

def test_non_matching_header():
    errors = []
    columns = [
        {'number': 1,
         'header': 'name1',
         'field': Field({'name': 'name1'})},
        {'number': 2,
         'header': 'name2',
         'field': Field({'name': 'name2'})},
        {'number': 3,
         'header': 'name3'},
    ]
    checks.non_matching_header(errors, columns)
    assert len(errors) == 0
    assert len(columns) == 3


def test_non_matching_header_problem(log):
    errors = []
    columns = [
        {'number': 1,
         'header': 'name1',
         'field': Field({'name': 'name2'})},
        {'number': 2,
         'header': 'name2',
         'field': Field({'name': 'name1'})},
        {'number': 3,
         'header': 'name3'},
    ]
    checks.non_matching_header(errors, columns)
    assert log(errors) == [
        (None, 1, 'non-matching-header'),
        (None, 2, 'non-matching-header'),
    ]
    assert len(columns) == 1
