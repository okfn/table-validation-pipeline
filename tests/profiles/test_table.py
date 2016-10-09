# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from goodtables import profiles


# Test

def test_table():
    errors = []
    tables = []
    profiles.table(errors, tables, 'data/valid.csv')
    assert len(errors) == 0
    assert len(tables) == 1
